import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

print("Chatbot ready! Type 'exit' to quit.")

conversation_history = [
    {"role": "system", "content": "You are a helpful assistant. Remember everything the user tells you during this conversation."}
]

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Bye!")
        break
    
    conversation_history.append({"role": "user", "content": user_input})
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation_history
    )
    
    bot_reply = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": bot_reply})
    
    print("Bot:", bot_reply)
    print()