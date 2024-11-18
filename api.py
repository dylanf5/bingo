from groq import Groq

client = Groq(api_key="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")

# Initialize conversation history
conversation_history = []

while True:
    # Get input from the user
    user_input = input("Enter your message: ")

    # If user types 'exit', break the loop and end the program
    if user_input.lower() == 'exit':
        print("Ending the conversation.")
        break

    # Add the user's input to the conversation history
    conversation_history.append({"role": "user", "content": user_input})

    # Send the conversation history to the Groq API and get a response
    completion = client.chat.completions.create(
        model="llama-3.2-90b-vision-preview",  # Ensure this model is valid for Groq
        messages=conversation_history,  # Pass the full conversation history
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    # Initialize the response content
    response = ""

    # Get the response from the model and add it to the response content
    for chunk in completion:
        response += chunk.choices[0].delta.content or ""

    print(response)

    # Add the model's response to the conversation history
    conversation_history.append({"role": "assistant", "content": response})

    print("\n---")  # Add a separator after each response
