import os

from flask_restful import Api, Resource, reqparse


import openai
from langchain import OpenAI
from langchain import SQLDatabase
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent

openai.api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(
    openai_api_key=openai.api_key,
    temperature=0,
    model_name="text-davinci-003"
)

db = SQLDatabase.from_uri("sqlite:///./SAPDatabase.db")

agent_executor = create_sql_agent(
    llm=llm,
    toolkit=SQLDatabaseToolkit(db=db, llm=llm),
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    max_iterations=5
)

sql_tool = Tool(
    name='SQL tool',
    func=agent_executor.run,
    description='use this tool for running SQL queries on database'
)

tools = [sql_tool]

memory = ConversationBufferMemory(memory_key="chat_history")

conversational_agent = initialize_agent(
    agent='conversational-react-description', 
    tools=tools, 
    llm=llm,
    verbose=True,
    max_iterations=10,
    memory=memory,
)


class ConvApiHandler(Resource):
  # def get(self, place):
  def post(self):
    print("got request in ConvApiHandler")
    parser = reqparse.RequestParser()
    parser.add_argument('question', type=str)

    args = parser.parse_args()

    print(args)

    return {
      'resultStatus': 'SUCCESS',
      'message': conversational_agent(args['question'])
    }

  