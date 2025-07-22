import openai
from dotenv import load_dotenv
import os
client = openai.OpenAI()
load_dotenv(verbose=True)
api_key = os.getenv("OPENAI_API_KEY") 
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate


message_template = """
당신은 여자친구에게 감동적이고 특별한 메시지를 대신 써주는 따뜻한 연인 역할입니다.
다음 정보를 참고해 여자친구에게 전달할 메시지를 3가지 제안해 주세요.




- 보내는 사람: {your_name}
- 받는 사람: {girlfriend_name}
- 상황/주제: {occasion}
- 메시지 분위기: {tone_manner}
- 함께한 추억: {memorable_memory}
- 꼭 포함할 단어/문구: {keyword}




각 메시지는 2~3줄 분량으로 자연스럽게 작성해 주세요.
"""
llm = ChatOpenAI(
    temperature=0,
    model_name='gpt-4.1'
)








prompt = PromptTemplate(
    input_variables=[
        "your_name",
        'girlfriend_name',
        'occasion',
        'tone_manner',
        'memorable_memory',
        'keyword'
    ],
    template=message_template
)


prompt_text = prompt.format(
    your_name='철수',
    girlfriend_name='영희',
    occasion='1주년',
    tone_manner='데이트',
    memorable_memory='강남역',
    keyword='알라뷰'
)




messages = [
    {'role' : 'system', 'content' : prompt_text},
    {'role' : 'user', 'content' : "이성에게 보낼 감동적인 사랑스러운 메시지 3개 만들어"}
]




llm.invoke(messages).content





import streamlit as st


st.set_page_config(page_title='이성에게 메시지 생성')
st.header("메시지 생성기")
st.markdown("----")




col1 , col2 = st.columns(2)


with col1:
    your_name = st.text_input("당신 이름 입력")
    girlfriend_name = st.text_input("이성 친구 이름")
    occasion = st.text_input("메시지 주제/상황")
with col2:
    tone_manner = st.text_input("톤/ 분위기 입력")
    memorable_memory = st.text_area("문구에 들어갈 추억", height=100)
    keyword = st.text_input("필수 포함 단어 {선택}")


if st.button("메시지 생성"):
    llm.invoke(messages).content
    pass
