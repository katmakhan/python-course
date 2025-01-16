import os

# Set the environment variable to disable parallelism warning
os.environ["TOKENIZERS_PARALLELISM"] = "false"  # Disable parallelism to avoid deadlocks


from sentence_transformers import SentenceTransformer
import pinecone
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Retrieve API keys
pinecone_api_key = os.getenv("PINECONE_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize Pinecone and connect to the index
pc = pinecone.Pinecone(api_key=pinecone_api_key)
index = pc.Index("paalana2")

print("Initialising the transformer model")
# Initialize the SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Query text
query_text = "who is the doctor in neuro surgery?"
query_embedding = model.encode(query_text).tolist()

print("Performing query on pinecone..")
# Perform the query
result = index.query(
    vector=query_embedding,
    top_k=1,
    include_metadata=True,
    metric="cosine",
    namespace="paalana-website"

)

# Process and display results
# print("Query Results:")
# for match in result.get('matches', []):
#     print(f"ID: {match['id']}, Score: {match['score']}, Metadata: {match.get('metadata', {})}")

print("Sending the result to groq to process the information retrieved.")
# Extract results into a summary format
raw_results = [
    {
        "id": match['id'],
        "score": match['score'],
        "metadata": match.get('metadata', {})
    }
    for match in result['matches']
]

# Format results for GPT
formatted_results = "\n".join(
    f"ID: {item['id']}, Score: {item['score']:.2f}, Metadata: {item['metadata']}"
    for item in raw_results
)

# print(formatted_results)

# Initialize Groq client
client = Groq(api_key=groq_api_key)


try:
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
        {
            "role": "user",
            "content": f"Here is the query result:\n\n{formatted_results}\n\nPlease provide a direct response to the user's question: '{query_text}'"
        }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
    )
    # Convert response to JSON
    response_json = completion.to_dict()

    # Print results
    print("\n\n")
    print(response_json["choices"][0]["message"]["content"])
    print("\n")
    print("Total Tokens used:", response_json["usage"]["total_tokens"])
except Exception as e:
    print("Error during Groq API call:", e)
