import os
from dotenv import load_dotenv
import streamlit as st
from pinecone import Pinecone
from pinecone_plugins.assistant.models.chat import Message

# Load environment variables
load_dotenv()

# Initialize Pinecone
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
ASSISTANT_NAME = "paalana-assistant"

if not PINECONE_API_KEY:
    st.error("Pinecone API Key is not set. Please add it to your .env file.")
    st.stop()

pc = Pinecone(api_key=PINECONE_API_KEY)
assistant = pc.assistant.Assistant(assistant_name=ASSISTANT_NAME)

# Streamlit Page Configuration
st.set_page_config(page_title="Pinecone Chat Assistant", layout="centered", page_icon="🤖")

# Custom Styling
st.markdown("""
    <style>
        .chat-container {
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 10px;
            margin: 10px 0;
        }
        .chat-container.user {
            text-align: left;
            background-color: #d1ecf1;
            color: #0c5460;
        }
        .chat-container.assistant {
            text-align: left;
            background-color: #f8d7da;
            color: #721c24;
        }
        .reset-button {
            margin-top: 20px;
            background-color: #dc3545;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .reset-button:hover {
            background-color: #c82333;
        }
    </style>
""", unsafe_allow_html=True)

# Page Header
st.title("🤖 Pinecone Chat Assistant")
st.write("Ask me anything!")

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
st.markdown("### Chat History")
for msg in st.session_state.messages:
    role_class = "user" if msg["role"] == "user" else "assistant"
    st.markdown(f"""
        <div class="chat-container {role_class}">
            <strong>{'You' if msg['role'] == 'user' else 'Assistant'}:</strong>
            <p>{msg['content']}</p>
        </div>
    """, unsafe_allow_html=True)

# Input Form
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Your question:", "")
    submitted = st.form_submit_button("Send")

# Handle User Input
if submitted and user_input.strip():
    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Create message container for streaming
    message_placeholder = st.empty()
    
    # Query Pinecone Assistant
    msg = Message(content=user_input)
    
    try:
        with st.spinner("Thinking..."):
            # Get all previous messages to maintain context
            message_history = [
                Message(content=m["content"]) 
                for m in st.session_state.messages[:-1]  # Exclude the latest message
            ]
            message_history.append(msg)
            
            # Stream Response
            response_content = ""
            # chunks = assistant.chat(messages=message_history, stream=True)
            response_content = assistant.chat(messages=message_history, stream=False)
            response_content=response_content['message']['content']
            # st.error(f"An error occurred: {str(response_content)}")
            # for chunk in chunks:
            #     response_content += chunk  # Accumulate response
            #     # Update placeholder with the partial response
            #     message_placeholder.markdown(f"""
            #         <div class="chat-container assistant">
            #             <strong>Assistant:</strong>
            #             <p>{response_content}</p>
            #         </div>
            #     """, unsafe_allow_html=True)

            message_placeholder.markdown(f"""
                    <div class="chat-container assistant">
                        <strong>Assistant:</strong>
                        <p>{response_content}</p>
                    </div>
                """, unsafe_allow_html=True)
                    
            # Save Assistant Response
            if response_content.strip():
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": response_content
                })
            
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Add Reset Button
if st.button("Reset Chat", key="reset_button", help="Clear chat history"):
    st.session_state.messages = []
    st.experimental_rerun()
