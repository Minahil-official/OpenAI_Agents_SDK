from agents import Agent,Runner,OpenAIChatCompletionsModel,
from dotenv import load_dotenv
import os
load_dotenv

model = OpenAIChatCompletionsModel(
    
)



My_agent = Agent(
    name="second_agent",
    instructions="You are a Asistance. You are a helpful assistant. You will answer the user query",
)

response = Runner.run_sync(
    starting_agent =My_agent,
    input ="What is the capital of France?",
    
)
print(response)