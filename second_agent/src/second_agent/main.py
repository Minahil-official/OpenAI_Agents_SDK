from agents import Agent,Runner,OpenAIChatCompletionsModel,AsyncOpenAI,set_tracing_disabled
from dotenv import load_dotenv
import os
import asyncio
load_dotenv()

set_tracing_disabled(True)

provider =  AsyncOpenAI(
         api_key = os.getenv("GEMINI_API_KEY"),
         base_url="https://generativelanguage.googleapis.com/v1beta/openai/"

     )

Model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
     openai_client = provider,
)

async def main():
    My_agent = Agent(
    name="second_agent",
    instructions="You are a Asistance. You are a helpful assistant. You will answer the user query",
    model= Model
)
    response = await Runner.run(
    starting_agent =My_agent,
    input ="tell me about Islam?",
    )
    print(response.final_output)

asyncio.run(main())




    

