import openai

def singleConv(prompt, api_key, role='You are an assistant.', model='gpt-3.5-turbo', max_tokens=50, temperature=0.7, top_p=1, frequency_penalty=0, presence_penalty=0, timeout=60):
    openai.api_key = api_key

    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": role},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            timeout=timeout  # Timeout setting in seconds
        )
        return response['choices'][0]['message']['content'].strip()
    
    except openai.error.Timeout as e:
        return f"Request timed out after {timeout} seconds."

if __name__ == '__main__':
    prompt_text = "Write a summary of the Python language."
    api_key = "your_openai_api_key"
    print(singleConv(prompt_text, api_key, max_tokens=100, timeout=30))  # Timeout set to 30 seconds
