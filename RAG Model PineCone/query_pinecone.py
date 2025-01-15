import os
import pinecone
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

# Load environment variables
load_dotenv()

class PineconeQuery:
    def __init__(self):
        # Initialize Pinecone client
        self.pc = pinecone.Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        self.index = self.pc.Index("paalana2")

        # Load model to create embeddings
        self.model = SentenceTransformer('all-MiniLM-L6-v2') #384 embedding

    def search(self, query_text, top_k=3):
        """
        Search Pinecone database and return text excerpts as answers.
        
        Args:
            query_text (str): The search query.
            top_k (int): Number of results to return.
        
        Returns:
            list: List of document excerpts as answers.
        """
        # Generate embedding for the query
        query_embedding = self.model.encode(query_text).tolist()

        # Search Pinecone
        results = self.index.query(
            vector=query_embedding,
            top_k=top_k,
            include_metadata=True
        )
        
        # Extract and return the content from metadata
        answers = [match['metadata'].get('content', 'No content available') for match in results['matches']]
        return answers

# Example usage
if __name__ == "__main__":
    query_system = PineconeQuery()
    query = "Where is paalana?"  # Example query
    answers = query_system.search(query)

    print(f"\nAnswers to: '{query}'\n")
    for i, answer in enumerate(answers, 1):
        print(f"Answer {i}: {answer}")
        print("-" * 50)
