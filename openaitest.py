import openai
from config import apikey

openai.api_key = apikey

messages = [
    {"role": "user", "content": "write context on attack on titan"}
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response)

'''
{
  "id": "chatcmpl-7f0D3SK9YOcQkrckiXPC3w3Axhbo3",
  "object": "chat.completion",
  "created": 1690006609,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Attack on Titan is a gripping Japanese manga series written and illustrated by Hajime Isayama. Set in a post-apocalyptic world, the story revolves around humanity\u2019s last remnants struggling against the Titans, gigantic humanoid creatures that devour humans seemingly without reason or remorse. The narrative primarily follows the journey of Eren Yeager, Mikasa Ackerman, and Armin Arlert, three young soldiers who join the fight against the Titans.\n\nThe series is set in a walled city called Paradis, which is divided into three concentric walls: Wall Maria, Wall Rose, and Wall Sheena. Humanity has been living peacefully within these walls for over a century, protected from the Titans that roam the outside world. However, this relative peace is shattered when a colossal Titan breaches Wall Maria, allowing smaller Titans to enter and kill countless humans. This catastrophic event, known as the \"Fall of Wall Maria,\" sets the stage for the ensuing human struggle against the Titans.\n\nDriven by the desire for revenge against the Titans, Eren Yeager enlists in the military, along with his childhood friends Mikasa and Armin. Within the military, their skills and determination are put to the test as they join the elite Survey Corps, a division focused on reclaiming lost territory and gathering information"
      },
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 13,
    "completion_tokens": 256,
    "total_tokens": 269
  }
}

'''