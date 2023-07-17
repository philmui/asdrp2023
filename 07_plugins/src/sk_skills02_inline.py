import os
import chainlit as cl
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(".env"))
LLM_MODEL_NAME = "text-davinci-003"         # OpenAI
SKILL_DIR        = "../skills"
SKILL_COLLECTION = "FunSkill"

import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAITextCompletion

kernel = sk.Kernel()
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
OPENAI_ORG_ID = os.environ["OPENAI_ORG_ID"]

# add text completion service 
kernel.add_text_completion_service(
    service_id="dv", 
    service=OpenAITextCompletion(
        LLM_MODEL_NAME, 
        OPENAI_API_KEY, 
        OPENAI_ORG_ID
    )
)

# need to create an inline prompt
# // TODO

SOLICITATION = "Type in some text for me to summarize!"

# add text completion service 

@cl.on_message  
async def main(message: str):
    response =  # // TODO
    await cl.Message(
        content=f"{response}"
    ).send()

@cl.on_chat_start
async def start():
    await cl.Message(
        content=SOLICITATION
    ).send()
