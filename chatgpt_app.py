from openai import OpenAI


# Set your OpenAI GPT-3 API key
client = OpenAI(api_key='')

# Set your OpenAI GPT-3 API key

def chat_with_gpt(prompt):
    response = client.completions.create(engine="text-davinci-002",  # You can experiment with different engines
    prompt=prompt,
    max_tokens=150,  # Adjust based on your desired response length
    n=1,  # Number of completions to generate
    stop=None)

    return response.choices[0].text.strip()

if __name__ == "__main__":
    print("Welcome to ChatGPT!")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Goodbye!")
            break

        prompt = f"You: {user_input}\nChatGPT:"
        response = chat_with_gpt(prompt)
        print(response)
