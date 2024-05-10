from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0.7)

def get_restaurant_and_menu_items(cuisine):
    prompt_name = PromptTemplate(
        input_variables = ['cuisine'],
        template = "I want to open a restauarant for {cuisine} food. Suggest me a good and fancy name for this."
    )
    name_chain = LLMChain(llm=llm, prompt = prompt_name, output_key = 'restaurant_name')

    menu_items = PromptTemplate(
        input_variables = ['restaurant_name'],
        template = "Suggest some menu items for {restaurant_name}. Return it in to a comma seperated string."
    )
    menu_chain = LLMChain(llm=llm, prompt = menu_items, output_key="menu_items")

    chain = SequentialChain(
        chains = [name_chain, menu_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
    )

    response = chain({"cuisine": cuisine})
    return response

