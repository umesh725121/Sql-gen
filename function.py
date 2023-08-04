from langchain import LLMMathChain, OpenAI, SerpAPIWrapper, SQLDatabase, SQLDatabaseChain
from langchain.chat_models import ChatOpenAI
import os
import panel as pn
import openai
import streamlit as st

from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI

from langchain.sql_database import SQLDatabase
from langchain.agents import *
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.chat_models import ChatOpenAI



# Setup Keys and DB connection 
os.environ['OPENAI_API_KEY'] = ''
db = SQLDatabase.from_uri("postgresql://postgres:postgres@localhost:5432/HR")




llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")

# The agent builds off of SQLDatabaseChain and is designed to answer more general questions about a database
#  as well as recover from errors.
toolkit = SQLDatabaseToolkit(db=db,llm=llm)

def sql_gen(question):
    agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)
    return agent_executor.run(question)

#integrate with Sreamlit
st.write(sql_gen(st.text_input("enter the")))
