import streamlit as st
from langchain_core.prompts.few_shot import FewShotPromptTemplate
from langchain_core.prompts import PromptTemplate  
from langchain_openai import ChatOpenAI




llm = ChatOpenAI(
    temperature=0,
    model_name='gpt-4.1'
)




examples = [
       {"question" : "서찬웅이 좋아하는 음식은?" , "answer" : "순대국, 두루치기, 김치찌개, 짜장면, 짬뽕"},
       {"question" : "조태민이 좋아하는 음식은" , "answer" : "김치피자탕수육, 팟타이, 오코노미야끼, 고추바사삭, 베이컨토마토디럭스버거"},
       {"question" : "한승희가 좋아하는 음식은?" , "answer" : "국밥, 마라탕, 짬뽕, 쌀국수, 제육"},
       {"question" : "권주연이 좋아하는 음식은?" , "answer" : "마라탕, 짬뽕, 쌀국수, 초밥, 두루치기"},
       {"question" : "정민철이 좋아하는 음식은" , "answer" : "삼겹살, 닭발, 김치찜, 샤브샤브, 쌀국수"},
       {"question" : "최서린이 좋아하는 음식은" , "answer" : "연어덮밥, 갈비구이, 포케, 타코, 쌀국수"},
       {"question" : "김민규가 좋아하는 음식은" , "answer" : "마라샹궈, 순대볶음, 쌀굯, 제육볶음, 돈까스"},
       {"question" : "권도원이 좋아하는 음식은" , "answer" : "마라샹궈, 햄버거, 타코, 돈까스쫄면, 돈까스냉면"},
       
       
             
]
example_prompt = PromptTemplate.from_template(
    "question:\n{question}\nanswer:{answer}"
)
# print(example_prompt.format(**examples[0]))
prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question:\n{question} \nAnswer:",
    input_variables=['question']
)
chain = prompt | llm
# llm.invoke(prompt.format(question="정민철과 권도원, 김민규하고 같이 식사할때 추천 메뉴 소개해줘")).content




st.title("점심 채봇")


user_input = st.text_input("메시지를 입력:", key='input')




if user_input:
    result = chain.invoke({'question':f"{user_input}"}).content


    st.markdown(f"{result}")
