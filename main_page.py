import streamlit as st
import pandas as pd
import numpy as np
import time

st.markdown("## Welcome to the Parks & Recreational Center Informational Assistant!")
st.sidebar.markdown("# Welcome Page")

message = "#### If you are someone who enjoys the outdoors and is located in the Bay Area, I can help! "
st.write(message)

st.image("https://www.cuddlynest.com/blog/wp-content/uploads/2023/04/guide_to_yosemite_yosemite_falls.jpg")

st.divider()
message = "##### Do you want to discover new places just for you? Click below!"
st.write(message)
st.link_button("Parks & Rec in the Bay Area", "https://www.yelp.com/search?find_desc=Parks+And+Recreation&find_loc=San+Francisco+Bay+Area%2C+CA")


st.divider()
message = "#### Watch the video below to learn some tips to keep in mind when planning your visit"
st.write(message)
VIDEO_URL = "https://www.youtube.com/watch?v=60V7n3nKxvI"
st.video(VIDEO_URL)

st.subheader('Additional Assisant Features', divider='grey')
col1, col2, col3 = st.columns(3)
with col1:
   st.page_link("main_page.py", label="Welcome", disabled=True)

with col2:
   st.page_link("pages/pages_1.py", label="Ideal Park Visualizaer")

with col3:
   st.page_link("pages/pages_2.py", label="Parks & Rec Article Summarizer")