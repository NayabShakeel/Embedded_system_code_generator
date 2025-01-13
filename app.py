


import gradio as gr

# Set up the API key
api_key = "demo_api",


# Initialize the client
client = Groq(api_key= "demo_api")

# Function to interact with the Groq API
def chat_with_groq(user_input):
    try:
        # Generate a chat completion
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": user_input}
            ],
            model="llama3-8b-8192",  # Replace with a valid model name if needed
        )
        # Return the response
        return chat_completion.choices[0].message.content
    except Exception as e:
        # Handle errors
        return f"An error occurred: {e}"

# Create a Gradio interface
interface = gr.Interface(
    fn=chat_with_groq,
    inputs=gr.Textbox(label="Enter your message"),
    outputs=gr.Textbox(label="Server Response"),
    title="Groq Chatbot",
    description="Type a message to interact with the Groq API.",
)

# Launch the interface
interface.launch()
