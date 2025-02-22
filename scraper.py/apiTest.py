from openai import OpenAI


client = OpenAI(api_key="sk-029717928e81416497940488cfac18dd", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are an expericed web scrapper, also restrict your answer to 100 words"},
        {f"role": "user", "content": "hi, how are you"},
    ],
    stream=False
)

print(response.choices[0].message.content)