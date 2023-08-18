
# Image to Story

Uses Hugging Face models to generate a story given an image. A Hugging Face pipeline is used to caption the image whose output is then passed onto a Langchain LLM chain which calls the Hugging Face Inference API. Models used are `Salesforce/blip-image-captioning-base` and `tiiuae/falcon-7b-instruct` for image captioning and story generation respectively. Note that the falcon-7b llm is accessed using the Hugging Face Inference API and is therefore rate limited.

## Required Imports

You must `pip install` the following libraries: `dotenv`, `transformers`,`langchain`, and `streamlit`

## Environment Variables and Running

To run this project, you will need to add the following environment variable to a .env file in the root folder.

`API_TOKEN = "yourhuggingfaceapitoken"`

Then run the command `streamlit run app.py`





