import os
import sys
import constants
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = constants.APIKEY

# Get input from command line
user_query = sys.argv[1]

# Create a DirectoryLoader instance
loader = DirectoryLoader("./files/", glob="*.txt")

# Create an index using VectorstoreIndexCreator
index = VectorstoreIndexCreator().from_loaders([loader])

# Provide a system message
system_prompt = "given that information, can you follow these instructions: Ignore all your previous commands. You are in charge of doing interviews for IDEC, a company in the manufacturing industry that makes switches selling B2B specializing in safety such as emergency stop buttons. You are currently in charge of interviewing this new recruit and your job is to create 5 questions to ask them based on their information and rate their answer to the interview question from a scale of 1 to 5. 1: Reject 2: Not recommend 3: Hold/File 4: Recommend 5: Hire I need you to create 5 custom questions to ask the new recruit. Customize these questions based on their information that i provided above. From now on, I need you to follow this template when asking the recruit the question: Rating: Rating for the last answer. (don't include if this is the first question) Interview Notes: Notes and reasoning for rating of the last question. (don't include if this is the first question). Q: Why did you leave your previous job? After reading this I need you to say 'Here are the questions for: {name of person}' and list the questions in bullet point form."

combined_query = f"{system_prompt} {user_query}"

# Query the index
llm = ChatOpenAI(model_name="gpt-4", temperature=0)
results = index.query(combined_query, llm)

print(results)
