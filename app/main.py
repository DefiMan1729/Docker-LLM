from typing import Union
from fastapi import FastAPI
import os

from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain
# OPENAI_API_KEY = input('enter key')
os.environ["OPENAI_API_KEY"]="your key"

llm = ChatOpenAI()
app = FastAPI()

@app.get("/feedback/{feedback}")
def read_item(feedback: str):
    template1 = "give me a summary of this employee's performance\n{review}"
    prompt1 = ChatPromptTemplate.from_template(template1)
    chain1 = LLMChain(llm=llm,prompt=prompt1,output_key='review_summary')

    template2 = "identify the employee's weaknesses\n {review_summary}"
    prompt2 = ChatPromptTemplate.from_template(template2)
    chain2 = LLMChain(llm=llm,prompt=prompt1,output_key='weakness')

    template3 = "provide a improvement plan for the employee based on\n {weakness}"
    prompt3 = ChatPromptTemplate.from_template(template3)
    chain3 = LLMChain(llm=llm,prompt=prompt1,output_key='recommendation')

    seq_chain = SequentialChain(chains = [chain1,chain2,chain3],
                                input_variables=['review'],
                                output_variables=['review_summary','weakness','recommendation'])

    result = seq_chain(feedback)
    return {"summary": result}
