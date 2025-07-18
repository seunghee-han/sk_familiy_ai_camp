from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import discord

tokenizer2 = AutoTokenizer.from_pretrained("nlp04/korean_sentiment_analysis_kcelectra")
model2 = AutoModelForSequenceClassification.from_pretrained("nlp04/korean_sentiment_analysis_kcelectra")
# Use a pipeline as a high-level helper
pipe2 = pipeline("text-classification", model="nlp04/korean_sentiment_analysis_kcelectra")

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if "감상문: " in message.content:
        message.content = message.content.split("감상문: ")[1]
        print(message.content)
        x =  pipe2(message.content)[0]['label']
        y = "{:.2f}".format(pipe2(message.content)[0]['score']) 
        answer = '감성분석: ' + x +'신뢰도: ',y
        await message.channel.send(answer)
        # await message.channel.send("pipe2(message.content)")

client.run("내 token 넣기")