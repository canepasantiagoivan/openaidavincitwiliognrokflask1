from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import openai

account_sid = 'xxxx'
auth_token = 'xxxx'
num_c='whatsapp:xxxx'
num_prosp='xxxx'
client = Client(account_sid, auth_token)

openai.api_key = 'xxxxx'

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

from flask import Flask, request

app = Flask(__name__)

@app.route('/bot', methods=['GET', 'POST'])
def bot():
    user_msg = request.values.get('Body', '').lower()

    print(f"Received message: {user_msg}")
    
    response = generate_response(user_msg)

    print(f"OpenAI response: {response}")
    
    message = client.messages.create(
        from_= num_c,
        body=(f"OpenAI response: {response}"),
        to=num_prosp
    )
    


   


if __name__ == '__main__':
    app.run(debug=True)
