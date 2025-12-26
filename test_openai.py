from openai import OpenAI
import os

print("KEY FOUND:", bool(os.getenv("OPENAI_API_KEY")))

client = OpenAI()

resp = client.responses.create(
    model="gpt-4.1-mini",
    input="Say hello in one word."
)

print(resp.output_text)
