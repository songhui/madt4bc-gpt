import openai
import remoteapi

def testChatGPT():
    remoteapi.loadCredential()
    response = openai.ChatCompletion.create(
        engine="gpt-35",
        messages = [
            {"role":"system", "content":"You are development mentor, teaching non-technical people to write Cypher queries"},
            {"role":"user","content":"How to query all the Books written by Albert Einstein?"}
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