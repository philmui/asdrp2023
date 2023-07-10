#
# Using Embeddings with simple GPT Vector Index
#
# GPTVectorStoreIndex = simple dictionary
#

from pathlib import Path
import sys
from llama_index import (
    GPTVectorStoreIndex, 
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage
)
DATA_DIR = "../data"
STORAGE_DIR = "storage"

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_index():
    index = None

    if Path(STORAGE_DIR).exists():   
        # if exists already, just load it
        storage_context = StorageContext.from_defaults(persist_dir=STORAGE_DIR)
        index = load_index_from_storage(storage_context)
    else:
        # read data files
        docs = SimpleDirectoryReader(DATA_DIR).load_data()
        
        # chunk the local files (or from APIs) & index them
        index = GPTVectorStoreIndex.from_documents(docs)
        
        # safe the index locally so that we don't need to do this again
        index.storage_context.persist(persist_dir=STORAGE_DIR)

    return index
        
def get_response(query):
    index = get_index()
    query_engine = index.as_query_engine()
    return query_engine.query(query)

if __name__ == '__main__':

    while True:
        query = input("What question do you have? ('quit' to quit) ")
        if "quit" in query: break
        response = get_response(query)
        print(response)
