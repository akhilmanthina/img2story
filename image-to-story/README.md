
# Image to Story

Uses Hugging Face models to generate a story given an image. Models used are `Salesforce/blip-image-captioning-base` and `tiiuae/falcon-7b-instruct` for image captioning and story generation respectively. Note that the falcon-7b llm is accessed using the Hugging Face Inference API and is therefore rate limited.


## Environment Variables

To run this project, you will need to add the following environment variable to a .env file in the root folder

`API_TOKEN = "yourhuggingfaceapitoken"`


