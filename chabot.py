import openai
import time


openai.api_key = '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'

def send_message(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        messages=[
            {"role": "system", "content": "You are a chatbot."},
            {"role": "user", "content": message}
        ],
        max_tokens=100,  
        temperature=0.7  
    )
    return response['choices'][0]['message']['content']

def main():
    
    print("Bliss: Hello! I'm here to chat with you and make you happy. How are you feeling today?")

    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Bliss: Goodbye! Take care.")
            break
        

        bot_response = send_message(user_input)
        print("Bliss:", bot_response)
        time.sleep(1)  

if __name__ == "__main__":
    main()
