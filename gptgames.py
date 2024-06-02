from openai import OpenAI
import base64
client = OpenAI()

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "dino1.png"

# Getting the base64 string
base64_image = encode_image(image_path)


response = client.chat.completions.create(
  model="gpt-4-turbo",
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
  logit_bias={44396:100,74070:100},
  max_tokens=1,
)

# 44396 : Token for jump
# 74070 : Token for duck

print(response.choices[0])