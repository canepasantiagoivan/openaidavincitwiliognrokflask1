from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import openai

# Configure Twilio client
account_sid = 'xxxx'
auth_token = 'xxxx'
num_c='whatsapp:xxxx'
num_prosp='xxxx'
client = Client(account_sid, auth_token)

# Configure OpenAI client
openai.api_key = 'xxxxx'

# Define function to generate response using OpenAI
def generate_response(query):
    prompt = f"Answer the following question: {query}\n\nAnswer:"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text.strip()

# Define Flask app
from flask import Flask, request

app = Flask(__name__)

# Define endpoint for Twilio to send messages to
@app.route('/bot', methods=['GET', 'POST'])
def bot():
    # Get user message
    user_msg = request.values.get('Body', '').lower()

    # Log user message
    print(f"Received message: {user_msg}")
    
    # Generate response using OpenAI
    response = generate_response(user_msg)

    # Log OpenAI response
    print(f"OpenAI response: {response}")
    
    # Send response using Twilio
    message = client.messages.create(
        from_= num_c,
        body=(f"OpenAI response: {response}"),
        to=num_prosp
    )
    


   


if __name__ == '__main__':
    app.run(debug=True)
