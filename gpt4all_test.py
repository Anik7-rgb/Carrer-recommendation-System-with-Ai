from gpt4all import GPT4All

# Load or download the model (first time it will download ~4GB)
model = GPT4All("mistral-7b-openorca.Q4_0.gguf")

# Start a chat session
with model.chat_session() as session:
    response = session.generate("Suggest a career path for someone skilled in Python, SQL, and Flask.")
    print("\n🤖 AI Assistant Says:\n", response)
