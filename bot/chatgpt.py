import os
import sys

import openai
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma
import prompt 
import Levenshtein
import constants

os.environ["OPENAI_API_KEY"] = constants.APIKEY
prompt = prompt.SYSTEM

def findFile(input):
    min_distance = float('inf')
    min_file_path = None
    
    for file_name in os.listdir("./files/"):
        if file_name.endswith(".txt"):
            distance = Levenshtein.distance(input.lower(), file_name.lower())
            
            if distance < min_distance:
                min_distance = distance
                min_file_path = os.path.join("./files/", file_name)
    
    return min_file_path


query = None
interviewee = findFile(input("Who would you like to interview?\n"))

chat_history = []
loader = TextLoader(interviewee) # Use this line if you only need data.txt
index = VectorstoreIndexCreator().from_loaders([loader])

chain = ConversationalRetrievalChain.from_llm(
  llm=ChatOpenAI(model="gpt-4", temperature=0.9),
  retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
)

start = True 
botCommand = False
while True:
  if start: 
    query = prompt
    start = False
  if not query:
    query = input("Input: ")
  if query in ['quit', 'q', 'exit']:
    sys.exit()
  if query in ['change interviewee']:
    interviewee = input("Who would you like to interview?\n")
    loader = TextLoader(findFile(interviewee))
    index = VectorstoreIndexCreator().from_loaders([loader])
    chain = ConversationalRetrievalChain.from_llm(
      llm=ChatOpenAI(model="gpt-4", temperature=0.9),
      retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
    )
    botCommand = True
    

  if not botCommand:
    result = chain({"question": query, "chat_history": chat_history})
    print(result['answer'])
    chat_history.append((query, result['answer']))

  query = None
  botCommand = False
