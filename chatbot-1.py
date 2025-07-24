import chainlit as cl
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


@cl.on_chat_start
async def on_chat_start():
    # 모델 초기화
    llm = ChatOpenAI(model="gpt-4.1")


    # 1. 단순화된 프롬프트 (대화 기록 부분이 없음)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "당신은 사용자의 질문에 간결하게 답변하는 AI 비서입니다."),
        ("human", "{input}"),
    ])


    # 2. 단순화된 LCEL 체인
    # 프롬프트, 모델, 출력 파서를 파이프(|)로 연결합니다.
    chain = prompt | llm | StrOutputParser()


    # 체인을 사용자 세션에 저장
    cl.user_session.set("chain", chain)


    await cl.Message(content="안녕하세요! 무엇이든 물어보세요.").send()


@cl.on_message
async def on_message(message: cl.Message):
    # 세션에서 체인 가져오기
    chain = cl.user_session.get("chain")


    # 3. 단순해진 체인 호출 (config 불필요)
    response = await chain.ainvoke({"input": message.content})


    # StrOutputParser 덕분에 response가 바로 문자열이므로 .content 없이 전송
    await cl.Message(content=response).send()
