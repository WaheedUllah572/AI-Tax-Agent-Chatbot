import os
import streamlit as st
from dotenv import load_dotenv
from utils.tax_agent_chain import get_tax_agent_response

# Environment overrides
os.environ["STREAMLIT_SERVER_ENABLECORS"] = "false"
os.environ["STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION"] = "false"

# Load environment variables
load_dotenv()

# Streamlit page settings
st.set_page_config(page_title="💰 AI Tax Agent Chatbot", layout="wide")
st.markdown("<h1 style='color:#FFD700;'>💰 AI Tax Agent Chatbot</h1>", unsafe_allow_html=True)
st.markdown("##### Choose your AI model backend:")

# ✅ Model selection now includes GPT-4
model_choice = st.selectbox("Model:", ["OpenAI GPT-4", "OpenAI GPT-3.5", "Groq Mixtral"], key="model")

# Tax query
st.markdown("##### Ask a tax-related question:")
query = st.text_input("Ask here:", key="question")

# Get and show response
if query:
    try:
        with st.spinner("💬 Generating response..."):
            response = get_tax_agent_response(query, model_choice)
        st.markdown(f"**AI Tax Agent:** {response}")
    except Exception as e:
        st.error(f"❌ Error generating answer: {str(e)}")

# Clear memory
if st.button("🧹 Clear Memory"):
    st.cache_data.clear()
    st.success("🧠 Conversation memory cleared.")
