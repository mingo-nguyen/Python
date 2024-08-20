from openai import OpenAI

api_key = 'sk-FQmaDheE4NOboeTPHEea7sAxh3z46cJi9So6fhXc0vT3BlbkFJyHbnap-7rLgLhxTqCfslboV09EVde5hFV8Cnp_zBIA'
client = OpenAI(api_key=api_key)


completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)
