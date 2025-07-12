import streamlit as st
import requests

# Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

# Streamlit UI
st.title("💬 Chat with Ollama (LLaMA 3)")

user_input = st.text_input("Enter your prompt:")

if st.button("Generate"):
    if user_input:
        payload = {
            "model": "mistral",
            "prompt": user_input,
            "stream": False
        }

        with st.spinner("Generating response..."):
            try:
                response = requests.post(OLLAMA_URL, json=payload)

                if response.status_code == 200:
                    json_response = response.json()
                    result = json_response.get("response", "No response received.")
                    st.success(result.strip())
                else:
                    st.error(f"Error {response.status_code}: {response.text}")
            except Exception as e:
                st.error(f"Failed to connect to Ollama: {e}")
