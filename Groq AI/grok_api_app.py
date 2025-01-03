from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)


msg_content="Which is the stock exchange in india"
completion = client.chat.completions.create(
    # model="gemma-7b-it",
    model="llama3-70b-8192",
    messages=[
        {
            "role": "user",
            "content": msg_content
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
)

# Convert the response to JSON
response_json = completion.to_dict()  # Assuming the client supports `to_dict()`

# Print the JSON response
# print(response_json)
print("Answer: ",response_json["choices"][0]["message"]["content"])
print("Total Tokens used: ",response_json["usage"]["total_tokens"])

