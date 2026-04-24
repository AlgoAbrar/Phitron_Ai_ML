from google import genai
from dotenv import load_dotenv
import os
from gtts import gTTS
import io

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
    return response.text

# response = client.models.generate_content(
#     model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
# )
# print(response.text)


def audio_transcription(text):
    
    speech= gTTS(text,lang='en', slow=False)
    audio_buffer= io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer


def quiz_generator(image,difficulty):

    prompt = f"Generate 3 quizzes based on the {difficulty}. Make sure to add markdown to differentiate the options. Add correct answer at last of the quiz so we can self evaluate"

    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents=[image,prompt]
    )

    return response.text