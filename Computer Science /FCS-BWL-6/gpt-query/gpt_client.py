# Import the OpenAI package
from openai import OpenAI 

# Replace this with your API key
client = OpenAI(api_key="<insert-your-api-key>")

# Formulate the request and send it
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
		{"role": "system", "content": 'You are a professor of computer science explaining how to use the ChatGPT python API.'},
                        {"role": "user", "content": 'Greet the students who are waiting for their practical exercise!'}
        	      ]
)

# Extract the response
response = completion.choices[0].message.content

# Print it
print(response)