from openai import OpenAI
import base64
import tiktoken
client = OpenAI()



def tokenize_words_with_count(words, model, count=100):
    tokenizer = tiktoken.encoding_for_model(model)
    tokenized_words = {}
    for word in words:
        token_id = tokenizer.encode(word)[0]  
        tokenized_words[token_id] = count
    return tokenized_words

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')


model="gpt-4-turbo"
image_path = "dino1.png"
base64_image = encode_image(image_path)
logit_bias= tokenize_words_with_count(["jump", "duck"], model)



response = client.chat.completions.create(
  model=model,
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What should be the next action in the game"},
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}",
          },
        },
      ],
    }
  ],
  logit_bias=logit_bias,
  max_tokens=1,
)




print(response.choices[0])