import os
import chainlit as cl
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(".env"))

from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

text="My phone number is 212-555-5555"


# Set up the engine, loads the NLP module (spaCy model by default) 
# and other PII recognizers
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

SOLICITATION = "Tell me something involving PII."    
@cl.on_message  
async def main(message: str):
    # Call analyzer to get results
    results = analyzer.analyze(text=message,
                                language='en')

    anonymized_text = anonymizer.anonymize(
        text=message,
        analyzer_results=results
    )
    await cl.Message(
        content=f"analysis: {results}\n\n" +
                f"anonymized:  {anonymized_text.text}"
    ).send()


@cl.on_chat_start
async def start():
    await cl.Message(
        content=SOLICITATION
    ).send()
