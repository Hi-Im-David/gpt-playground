import openai
import base64

# Function to read the API key from the file
def read_api_key(file_path):
    with open(file_path, 'r') as file:
        # Read the line and split by '=' to extract the key
        api_key_line = file.readline().strip()  # Read and remove any surrounding whitespace
        api_key = api_key_line.split('=')[1]  # Get the value after '='
        return api_key

client = openai.OpenAI(api_key = read_api_key("api_key.txt"))

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def interpret_image(path):
  # Getting the base64 string
  base64_image = encode_image(path)

  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "What do you see?"},
          {
            "type": "image_url",
            "image_url": {
              "url":  f"data:image/jpeg;base64,{base64_image}"
            },
          },
        ],
      }
    ],
    max_tokens=300,
  )

  print(response.choices[0])


# completion = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "system", "content": "You are a cooking robot that makes burgers."},
#         {
#             "role": "user",
#             "content": "What's the cheapest robot arm with 6 axis of freedom and large working radius"
#         }
#     ]
# )

# print(completion.choices[0].message)