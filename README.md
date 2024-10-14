#### Description
This package provides quick access to talk to the wonderful ChatGPT model by OpenAI.

#### Install
```
pip install git+https://github.com/BellowAverage/PythonUtilities.git@main
```

#### Example:
```
from OpenAIAPI import ChatGPT

APIKey = "your openai api key"

res = ChatGPT.singleConv("Morning", APIKey)

print(res)
```