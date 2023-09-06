import os

from flask_restful import Api, Resource, reqparse


import openai
from langchain import OpenAI, SQLDatabase, SQLDatabaseChain
from langchain.prompts import PromptTemplate

openai.api_key = os.getenv("OPENAI_API_KEY")

#db = SQLDatabase.from_uri("sqlite:///../Chinook.db")
db = SQLDatabase.from_uri("sqlite:///./SAPDatabase.db")
llm = OpenAI(temperature=0, verbose=True)
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, use_query_checker=True)

class OpenAIApiHandler(Resource):
  # def get(self, place):
  def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument('question', type=str)

    args = parser.parse_args()

    print(args)
    # higher temperature leads to more variation, randomness and creativity
    # temperature between 0.7 and 0.9 is most commonly used if you want to experiment and create many variations quickly
    # llm = OpenAI(temperature=0.9)
    # https://python.langchain.com/en/latest/modules/prompts/prompt_templates.html
    # prompt = PromptTemplate(
    #    input_variables=["place"],  # list of variables
    #    template="What are the 3 best places to eat in {place}?",  # prompt
    # )
    # question = prompt.format(place=place)
    # split() is used to split the items into a list. The llm response will look like:
    # "\n\n1. <first item>.\n\n2. <second item>..."
    return {
      'resultStatus': 'SUCCESS',
      #'message': llm(question).split("\n\n")
      'message': db_chain.run(args['question'])
      }

  