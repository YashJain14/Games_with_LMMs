from openai import OpenAI
client = OpenAI()
import sglang as sgl

sgl.set_default_backend(sgl.OpenAI("gpt-4-turbo", is_chat_model=True))

@sgl.function
def image_qa(s, image_path, question):
    s += sgl.user(sgl.image(image_path) + question)
    s += sgl.assistant(sgl.gen("answer", max_tokens=1, temperature=0, choices=["jump", "duck"]))


def single():
    state = image_qa.run(
        image_path="dino1.png",
        question="What should be the next action in the game?"
        )

    print(state)



single()

