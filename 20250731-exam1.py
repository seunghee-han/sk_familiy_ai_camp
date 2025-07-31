import os 
import streamlit as st 
from openai import OpenAI
import openai 


client = OpenAI()

st.title("문장을 mp3 파일 생성")

options = ['alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer']
selected_option = st.selectbox("성우 선택", options)
print(selected_option)

user_prompt = st.text_area("스크립트 작성", height=300)

if st.button("음성생성"):
    audio = client.audio.speech.create(
        model='tts-1',
        voice= selected_option,
        input = user_prompt,
        speed = 1
    )

    audio_content = audio.content

    with open("tmp.mp3", 'wb') as f:
        f.write(audio_content)
    st.audio("tmp.mp3", format='audio/mp3')