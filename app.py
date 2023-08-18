from dotenv import load_dotenv, find_dotenv
from transformers import pipeline
from langchain import PromptTemplate, LLMChain
from langchain.llms import HuggingFaceTextGenInference
import streamlit as st

import requests
import os



load_dotenv(find_dotenv())

API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
API_TOKEN = os.getenv("API_TOKEN")
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def img_to_text(img_path):
    model_pipeline = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

    text = model_pipeline(img_path)[0]["generated_text"]

    #print(text)
    return text




def text_to_story(context):

   
    prompt = PromptTemplate.from_template(
    """
    You are a storyteller. You can generate a short story based on a simple narrative. The story should be around 100 words long.
    CONTEXT: {context}
    """
    )
    
    #llm = LLMChain(llm=HuggingFacePipeline.from_model_id(model_id = "tiiuae/falcon-7b-instruct", task="text-generation"), prompt=prompt, verbose=True)
    llm = HuggingFaceTextGenInference(
       inference_server_url=API_URL,
       server_kwargs={"headers": headers}
   )


    llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=True)

    story = llm_chain.predict(context=context)
    
    print(story)
    return story






def main():
    st.title("Image to Story")
    st.write("This app generates a story based on an image. Upload an image and click the button below to try it out!")
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    if uploaded_file is not None:
        image = uploaded_file.getvalue()
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        

        img_name = uploaded_file.name

        with open(img_name, "wb") as f:
            f.write(image)

        with st.spinner("Generating story..."):
            prompt = img_to_text(img_name)
            story = text_to_story(prompt)
            
            story = story.rsplit('User', 1)[0]

            with st.expander("Prompt"):
                st.write(prompt)
            with st.expander("Story"):
                st.markdown(story, unsafe_allow_html=True)
        #st.write("Done!")

if __name__ == "__main__":
    main()