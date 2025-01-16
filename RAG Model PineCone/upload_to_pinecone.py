import os
import pinecone
# from openai import OpenAI
from markdown import markdown
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

load_dotenv()

# Initialize API keys
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = SentenceTransformer('all-MiniLM-L6-v2')  # Small, fast and good quality model
pinecone_api_key = os.getenv("PINECONE_API_KEY")


# Initialize Pinecone and connect to existing index
pc = pinecone.Pinecone(api_key=pinecone_api_key)
index = pc.Index("paalana2")

def read_markdown_file(file_path):
    """Convert markdown file to plain text."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    html_content = markdown(content)
    plain_text = BeautifulSoup(html_content, "html.parser").get_text()
    return plain_text.strip()

# def get_text_embedding(text):
#     """Generate embedding using OpenAI API."""
#     response = client.embeddings.create(
#         input=text,
#         model="text-embedding-3-small"
#     )
#     return response.data[0].embedding

def get_text_embedding(text):
    """Generate embedding using Sentence Transformers."""
    embedding = model.encode(text)
    return embedding.tolist()  # Convert numpy array to list for Pinecone


def upload_markdown_to_pinecone(directory_path):
    """Process markdown files and upload to Pinecone."""
    if not os.path.exists(directory_path):
        print(f"Directory not found: {directory_path}")
        return

    for file_name in os.listdir(directory_path):
        if file_name.endswith(".md"):
            try:
                # Process file
                file_path = os.path.join(directory_path, file_name)
                print("Reading the markdown file..")
                text_content = read_markdown_file(file_path)
                
                # Generate vector
                print("Generating vector..")
                vector = get_text_embedding(text_content)
                
                print("Uploading to pinecone..")
                # Upload to Pinecone
                index.upsert(
                    vectors=[(
                        file_name,  # ID
                        vector,     # Vector
                        {"file_name": file_name, "content": text_content}  # Store content in metadata
                    )],
                    namespace="paalana-website"  # Specify the namespace
                )
                print(f"Processed: {file_name}")
                
            except Exception as e:
                print(f"Error processing {file_name}: {str(e)}")

# Run the upload process
try:
    upload_markdown_to_pinecone("./Dataset/")
    print("Upload completed successfully!")
except Exception as e:
    print(f"An error occurred: {str(e)}")