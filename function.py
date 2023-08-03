from langchain import LLMMathChain, OpenAI, SerpAPIWrapper, SQLDatabase, SQLDatabaseChain
from langchain.chat_models import ChatOpenAI
import os
import panel as pn
import openai
import streamlit as st


from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI

from langchain.vectorstores import Milvus
from langchain.document_loaders import TextLoader
from langchain.agents import load_tools
from langchain.sql_database import SQLDatabase
from langchain.agents import *
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.chat_models import ChatOpenAI


# Setup Keys and DB connection 
os.environ['OPENAI_API_KEY'] = ''
#os.environ['SERPAPI_API_KEY'] = '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'
db = SQLDatabase.from_uri("postgresql://postgres:postgres@localhost:5432/HR")



#llm = ChatOpenAI(model_name="gpt-3.5-turbo")

# setup LLM and SQL toolkit 
#llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")
#toolkit = SQLDatabaseToolkit(db=db,llm=llm)
#agent_executor = create_sql_agent(
 #   llm=llm,
  #  toolkit=toolkit,
   # verbose=True
#)
#response = agent_executor.run('list all employees who work in london')


llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")

toolkit = SQLDatabaseToolkit(db=db,llm=llm)

def sql_gen(question):
    agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)
    return agent_executor.run(question)
#question = "List all the jobs"

#path = st.text_input(question)
st.write(sql_gen(st.text_input("enter the statement")))
