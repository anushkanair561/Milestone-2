import os
import openai
import streamlit as st
from PIL import Image
import requests
from openai import OpenAI
from pathlib import Path

st.markdown("## Park Vision Image Generation")
st.sidebar.markdown("# Page 2: Park Vision Image Generation")


openai.api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI()

def download_image(filename, url):
   response = requests.get(url)
   if response.status_code == 200:
       with open(filename, 'wb') as file:
           file.write(response.content)
   else:
       print("Error downloading image from URL:", url)


def filename_from_input(prompt):
   alphanum = "".join(character if character.isalnum() or character == " " else "" for character in prompt)
   words = alphanum.split()[:3]  # Limit to first three words
   return "images/" + "_".join(words)


# Generate an image based on user input text
def get_image(prompt, model="dall-e-2"):
   image = client.images.generate(
       prompt=prompt,
       model=model,
       n=1,
       size="1024x1024"
   )
   filename = Path(__file__).parent / (filename_from_input(prompt) + ".png")
   download_image(filename, image.data[0].url)
   return filename


with st.form(key="park_vision_form"):
   prompt = st.text_input('Describe your ideal vision for the park:')
   submitted = st.form_submit_button("Generate Image")
      
   if submitted:
       image_path = get_image(prompt)
       image = Image.open(image_path)
       st.image(image, caption='Your Vision of the Park')