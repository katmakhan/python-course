import os
import streamlit as st
from sentence_transformers import SentenceTransformer
import pinecone
import os
import streamlit as st
from sentence_transformers import SentenceTransformer
import pinecone
from dotenv import load_dotenv
from groq import Groq

# Page configuration
st.set_page_config(
    page_title="AI Chat Assistant",
    page_icon="💬",
    layout="centered"
)

st.markdown("""
    <style>
    /* Light mode styles */
    :root {
        --user-message-bg-light: #e8f0fe;
        --assistant-message-bg-light: #f8f9fa;
        --input-bg-light: #ffffff;
        --input-border-light: #ccc;
    }

    /* Dark mode styles */
    @media (prefers-color-scheme: dark) {
        :root {
            --user-message-bg-dark: #1e3a8a; /* Navy-like blue */
            --assistant-message-bg-dark: #374151; /* Gray-like tone */
            --input-bg-dark: #1f2937;
            --input-border-dark: #4b5563;
        }
    }

    .stTextInput > div > div > input {
        padding: 15px;
        font-size: 16px;
        border-radius: 10px;
        background-color: var(--input-bg-light);
        border: 1px solid var(--input-border-light);
        color: black;
    }

    @media (prefers-color-scheme: dark) {
        .stTextInput > div > div > input {
            background-color: var(--input-bg-dark);
            border: 1px solid var(--input-border-dark);
            color: white;
        }
    }

    .stButton > button {
        width: 100%;
        padding: 10px;
        border-radius: 10px;
    }

    .chat-message {
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
    }

    .user-message {
        background-color: var(--user-message-bg-light);
    }

    .assistant-message {
        background-color: var(--assistant-message-bg-light);
    }

    @media (prefers-color-scheme: dark) {
        .user-message {
            background-color: var(--user-message-bg-dark);
            color: white;
        }
        .assistant-message {
            background-color: var(--assistant-message-bg-dark);
            color: white;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Set the environment variable to disable parallelism warning
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'initialized' not in st.session_state:
    st.session_state.initialized = False

@st.cache_resource
def initialize_environment():
    """Initialize environment variables and return API keys"""
    load_dotenv()
    pinecone_api_key = os.getenv("PINECONE_API_KEY")
    groq_api_key = os.getenv("GROQ_API_KEY")
    
    if not pinecone_api_key or not groq_api_key:
        raise ValueError("API keys not found in environment variables")
    
    return pinecone_api_key, groq_api_key

@st.cache_resource
def initialize_sentence_transformer():
    """Initialize SentenceTransformer model"""
    return SentenceTransformer('all-MiniLM-L6-v2')

@st.cache_resource
def initialize_groq(api_key):
    """Initialize Groq client"""
    return Groq(api_key=api_key)

@st.cache_resource
def initialize_pinecone(api_key):
    """Initialize Pinecone client"""
    pc=pinecone.Pinecone(api_key=api_key)
    return pc.Index("paalana2")

# Initialize clients with progress tracking
try:
    progress_bar = st.progress(0, text="Initializing environment variables...")
    pinecone_api_key, groq_api_key = initialize_environment()
    
    progress_bar.progress(33, text="Initializing Pinecone...")
    index = initialize_pinecone(pinecone_api_key)
    
    progress_bar.progress(66, text="Initializing SentenceTransformer...")
    model = initialize_sentence_transformer()
    
    progress_bar.progress(90, text="Initializing Groq...")
    client = initialize_groq(groq_api_key)
    
    progress_bar.progress(100, text="Initialization complete!")
    progress_bar.empty()
    
except Exception as e:
    st.error(f"Failed to initialize clients. Please check your API keys and try again. Error details: {str(e)}")
    st.stop()



def handle_submit():
    """Handle the submit button click"""
    if st.session_state.user_input.strip():
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": st.session_state.user_input})
        
        # Get bot response
        with st.spinner("Processing your query..."):
            response = process_query(st.session_state.user_input)
            st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Clear the input
        st.session_state.user_input = ""

# Main title
st.title("💬 Paalana AI Chat Assistant")
st.markdown("Ask me anything about our services!")


# Display chat history
for message in st.session_state.messages:
    with st.container():
        st.markdown(f"""
            <div class="chat-message {'user-message' if message['role'] == 'user' else 'assistant-message'}">
                <b>{'You' if message['role'] == 'user' else 'Assistant'}:</b> {message['content']}
            </div>
            """, unsafe_allow_html=True)

# Chat input
user_query = st.text_input("Your message:", key="user_input", placeholder="Type your message here...", on_change=handle_submit)

def process_query(user_query):
    """Process the user query and return the response"""
    try:
        # Generate query embedding for the user's latest query
        query_embedding = model.encode(user_query).tolist()
        
        # Query Pinecone
        result = index.query(
            vector=query_embedding,
            top_k=1,
            include_metadata=True,
            metric="cosine",
            namespace="paalana-website"
        )
        
        # Format results from Pinecone
        raw_results = [
            {
                "id": match['id'],
                "score": match['score'],
                "metadata": match.get('metadata', {})
            }
            for match in result.get('matches', [])
        ]

        if raw_results:
            formatted_results = "\n".join(
                f"ID: {item['id']}, Score: {item['score']:.2f}, Metadata: {item['metadata']}"
                for item in raw_results
            )

            # Prepare the full conversation history for Groq
            # Retain only last 3 converstations
            conversation_history = [
                {"role": message["role"], "content": message["content"]}
                for message in st.session_state.messages[-3:]
            ]
            
            # Add the formatted Pinecone results to the history
            conversation_history.append({
                "role": "assistant",
                "content": f"Here are the relevant results from Pinecone:\n\n{formatted_results}"
            })

            # Add the user's latest query for context
            conversation_history.append({
                "role": "user",
                "content": f"Now, please answer my question directly without any appologies: '{user_query}'"
            })

            # print("The question for groq is ",conversation_history)

            # Query Groq with full conversation history
            completion = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=conversation_history,
                temperature=1,
                max_tokens=1024,
                top_p=1,
                stream=False,
            )
            
            response_json = completion.to_dict()
            return response_json["choices"][0]["message"]["content"]
        
        return "I couldn't find any relevant information to answer your question. Please try rephrasing your query."
    
    except Exception as e:
        st.error(f"Error details: {str(e)}")
        return "I apologize, but I encountered an error while processing your request. Please try again later."

user_query = ""