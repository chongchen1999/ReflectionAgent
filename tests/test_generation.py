import os
from pprint import pprint
from groq import Groq
from dotenv import load_dotenv
from IPython.display import display_markdown

# Remember to load the environment variables. You should have the Groq API Key in there :)
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

generation_chat_history = [
    {
        "role": "system",
        "content": "You are a skilled programmer tasked with generating high quality programming code."
        "Your task is to Generate the best content possible for the user's request. If the user provides critique," 
        "respond with a revised version of your previous attempt."
    }
]

generation_chat_history.append(
    {
        "role": "user",
        "content": "Generate a C++ implementation of the Quick Sort algorithm"
    }
)

mergesort_code = client.chat.completions.create(
    messages=generation_chat_history,
    model="llama3-70b-8192"
).choices[0].message.content

generation_chat_history.append(
    {
        "role": "assistant",
        "content": mergesort_code
    }
)

print(mergesort_code)
# display_markdown(mergesort_code, raw=True)
