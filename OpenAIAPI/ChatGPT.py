import openai

def singleConv(prompt, api_key, model='gpt-3.5-turbo', max_tokens=50, temperature=0.7, top_p=1, frequency_penalty=0, presence_penalty=0):
    openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )

    return response['choices'][0]['message']['content'].strip()

if __name__ == '__main__':
    prompt_text = "Write a summary of the Python language."
    api_key = "your_openai_api_key"
    print(singleConv(prompt_text, api_key, max_tokens=100))
