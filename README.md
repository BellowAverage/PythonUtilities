install
```
pip install git+https://github.com/BellowAverage/PythonUtilities.git@main
```

example:
```
from OpenAIAPI import ChatGPT

APIKey = "your openai api key"

res = ChatGPT.singleConv("Morning", APIKey)

print(res)
```