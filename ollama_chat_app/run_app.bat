@echo off
echo ⚙️ Forcing Ollama to use D:\ollama for model storage...
set OLLAMA_MODELS=D:\ollama

echo 🚀 Starting Ollama with mistral...
start cmd /k "ollama run mistral"

timeout /t 6 >nul

echo 🌐 Launching Streamlit app...
start cmd /k "streamlit run app.py"
