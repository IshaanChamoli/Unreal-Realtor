import os
from dotenv import load_dotenv

from openai import OpenAI # type: ignore

load_dotenv()
client = OpenAI()

def agent1(client, input_text):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a business analyst."},
            {"role": "user", "content": input_text}
        ]
    )
    output = completion.choices[0].message.content
    return output


def agent2(client, input_text):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a financial analyst."},
            {"role": "user", "content": input_text}
        ]
    )
    output = completion.choices[0].message.content
    return output


def agent3(client, input_text):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a market analyst."},
            {"role": "user", "content": input_text}
        ]
    )
    output = completion.choices[0].message.content
    return output

# Initial input for the first agent
initial_input = "Analyze the current market trends for AI tools in real estate"

# Passing the output of one agent as input to the next
output1 = agent1(client, initial_input)
output2 = agent2(client, output1)
final_output = agent3(client, output2)

print(final_output)
