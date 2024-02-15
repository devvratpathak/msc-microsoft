
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
    
    print("Bliss: Hello!What's Up?")

    while True:
        user_input = input("You: ")
        mood_inp = "what is the mood of this message, give me a reply in ONLY one word  :" + user_input
        
        if user_input.lower() == 'exit':
            print("Bliss: Goodbye! Take care.")
            break
        

        bot_response = send_message(mood_inp)
        print("Bliss: You are", bot_response)


if __name__ == "__main__":
    main()
