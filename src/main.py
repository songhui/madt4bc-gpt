import yaml
import os
import openai

def loadCredential():
    with open("../openai.credential", 'r') as stream:
        credential_data = yaml.safe_load(stream)
    openai_config = credential_data['openai']
    openai.api_type = "azure"
    openai.api_base = openai_config['endpoint']
    openai.api_version = "2023-03-15-preview"
    openai.api_key = openai_config["key"]

def testChatGPT():
    loadCredential()
    response = openai.ChatCompletion.create(
        engine="gpt-35",
        messages = [
            {"role":"system", "content":"You are development mentor, teaching non-technical people to write Cypher queries"},
            {"role":"user","content":"How to query all the Books writen by Albert Einstein?"}
        ],
        temperature=0,
        max_tokens=80,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    print(response)

if __name__ == "__main__":
    testChatGPT()