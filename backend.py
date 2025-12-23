import os 
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)

api_key = os.getenv('GEMINI_API_KEY')

GEMINI_URL = 'https://generativelanguage.googleapis.com/v1beta/openai/'

client = OpenAI(base_url=GEMINI_URL, api_key=api_key)   

zero_shot_prompt=''' 
Your helpful Assitent
Task: {User_input}
Give Clear and Consise Answer'''

one_shot_prompt = """ 
Your helpfull Assient
Task:Explain what is LLM?
Answer: LLM stands for Large-language-Model.They are trained on huge amount of data.They Recieved the tokens
as input and predict most likly token that have higher probability amoung the tokens. 
"""

few_shot_prompt =""" 
Your Helpfull Assient
Example : 1
Task : Explain what is LLM? 
Answer: LLM stands for Large-language-Model.They are trained on huge amount of data.They Recieved the tokens
as input and predict most likly token that have higher probability amoung the tokens.

Example :2 
Task : what is Science?
Answer : Science is replicable Concept . The concept wil work for different environments  but having the same 
concept. 

Example : 3
Task :  what is consonents in english ?
Answer : Consonants are speech sounds made by partially or fully blocking airflow in the vocal tract.
English has 21 consonant letters and about 24 consonant sounds, represented by single letters or combinations like “sh.” 
Consonants usually combine with vowels to form syllables and give structure and clarity to speech.
"""
def call_llm(user_input, prompt_type):
    if prompt_type == 'Zero-shot':
        prompt = zero_shot_prompt
    elif prompt_type == 'One-shot':
        prompt = one_shot_prompt
    else: 
        prompt = few_shot_prompt


    response = client.chat.completions.create(
        model = 'gemini-2.5-flash',
        messages = [
                {'role' :'system', 'content': prompt},
                {'role' : 'user','content':user_input}
            ]
        )            
    return response.choices[0].message.content