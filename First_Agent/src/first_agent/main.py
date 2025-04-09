from agents import Agent , Runner , OpenAIChatCompletionsModel, AsyncOpenAI,set_tracing_disabled
from dotenv import load_dotenv
load_dotenv()
import os

set_tracing_disabled(True)

provider = AsyncOpenAI(
    api_key = os.getenv("GEMINI_API_KEY"),
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)
model = OpenAIChatCompletionsModel(
    model= "gemini-2.0-flash-exp",
    openai_client = provider
)
def sdk_agent():
    agent = Agent(name = "Asistant", 
                  instructions = "You are a helpful assistant.",
                  model = model, )
    
    
    result = Runner.run_sync(agent,"what is Open AI SDK")
    print(result.final_output)
