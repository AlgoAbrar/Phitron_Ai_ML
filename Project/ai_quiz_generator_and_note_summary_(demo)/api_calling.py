from google import genai
from dotenv import load_dotenv
import os


# load env
load_dotenv()

my_api_key= os.getenv("GEMINI_API_KEY")

# initializing client
client = genai.Client(api_key=my_api_key)

# Note Generator
def note_generator(images):
    prompt= """Summarize the picture in note format at max 200 words,
    make sure to add necessary markdown to differenciate different section"""
    response= client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, prompt] #multimodal capability image, so we will send it as list
    )
    return response.txt

# response = client.models.generate_content(
#     model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
# )
# print(response.text)


