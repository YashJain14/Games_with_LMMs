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


def next_action(image):
  response = client.chat.completions.create(
    model=model,
    messages=[
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "What should be the next keypress in the game"},
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
  print(response.choices[0].message.content)
  return response



model="gpt-4-turbo"
actions=["up","down","right","left"]
logit_bias= tokenize_words_with_count(actions, model)


image_paths = ["pacman1.png","pacman2.png","pacman2.png","pacman4.png"]

for image_path in image_paths:
  base64_image = encode_image(image_path)
  next_action(base64_image)

