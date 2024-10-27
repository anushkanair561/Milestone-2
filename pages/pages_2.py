import streamlit as st
import requests
from bs4 import BeautifulSoup
import openai
from openai import OpenAI
import os


# Create a text input for the URL


st.header("Learn more about Parks & Recreation in your community and beyond :evergreen_tree:")
st.subheader("Summarize Parks & Recreational News that interest you!")
st.subheader("Here is a list of news sources to choose from:")




st.text('Local & Global News')


st.link_button("National Park Service News", "https://www.nps.gov/aboutus/news/news-releases.htm#sort=Date_Released%20desc&fq[]=Date_Released%3A[NOW-29DAYS%20TO%20NOW]")
st.link_button("National Geographic News", "https://www.nationalgeographic.com/pages/topic/latest-stories")
st.link_button("CNN Travel News", "https://www.cnn.com/travel")
st.link_button("City of San Jose Trails", "https://www.americantrails.org/organizations/city-of-san-jose")


url = st.text_input('Enter a URL of an article')


def get_web_content(url):
   # Fetch the webpage
   web_content = ""
   response = requests.get(url)


   # Parse the HTML
   soup = BeautifulSoup(response.text, 'html.parser')


   # Display the title of the webpage
   st.write('Webpage Title:')
   st.write(soup.title.string)


   # Display the text of the webpage
   st.write('Webpage Text:')
   article_tags = soup.find_all('article')
  
   for article in article_tags:
       paragraphs = article.find_all('p')
       for p in paragraphs:
           web_content = web_content + str(p.get_text()) + '\n'


   return web_content


# Takes the transcription of the meeting and returns a summary of it via text completions
def abstract_summary_extraction(transcription):
   response = client.chat.completions.create(
       model="gpt-3.5-turbo",
       temperature=0,
       messages=[
           {
               "role": "system",
               "content": "You are a highly skilled AI trained in language comprehension and summarization. I would like you to read the following text and summarize it into a concise abstract paragraph and provide me with the important points in bullet format that could help a person understand the main points of the discussion without needing to read the entire text. Please avoid unnecessary details or tangential points."
           },
           {
               "role": "user",
               "content": transcription
           }
       ]
   )
   return response.choices[0].message.content


openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI()


# Create a button to fetch the content
if st.button('Fetch Content'):
   display_content = get_web_content(url)
   st.write(abstract_summary_extraction(display_content))