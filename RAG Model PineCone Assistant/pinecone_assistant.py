import os
from dotenv import load_dotenv
from pinecone import Pinecone

# Load environment variables
load_dotenv()

# Initialize Pinecone
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
ASSISTANT_NAME = "paalana-assistant"
from pinecone import Pinecone
from pinecone_plugins.assistant.models.chat import Message

pc = Pinecone(api_key=PINECONE_API_KEY)

assistant = pc.assistant.Assistant(assistant_name="paalana-assistant")

your_question=input("Enter your question:")
msg = Message(content=your_question)

# resp = assistant.chat(messages=[msg])
# print(resp["message"]["content"])

# With streaming
chunks = assistant.chat(messages=[msg], stream=True)

for chunk in chunks:
    if chunk:
        # Ensure chunk is a dictionary and process content
        if chunk.get("type") == "content_chunk":
            # Extract and print the content
            content = chunk["delta"].get("content", "")
            print(content, end="", flush=True)  # Print without a newline and flush the output
