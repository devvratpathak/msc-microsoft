
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

#WHEN YOU TAKE INPUT FORM USER IN WEBSITE JUST RUN THIS FUCNTUION WITH THE INOPUT!!! main()
def main():
    
    print("Bliss: Hello!What's Up?")

    while True:
        #INPUT FROM WEBSITE GOES HEREEEE
        user_input = input("You: ")
        mood_inp = "what is the mood of the given message give me a reply ONLY from these categories [sad,joyful,angry,neutral,satisfied,grateful,depressed,disgusted,surpised,a pervert]  :" + user_input
        
        if user_input.lower() == 'exit':
            print("Bliss: Goodbye! Take care.")
            break
        

        bot_response = send_message(mood_inp)
        print("Bliss: You are", bot_response)


if __name__ == "__main__":
    main()
