import asyncio
from openai import OpenAI
from azure.cognitiveservices import speech
from datetime import datetime
import navel

#Example of a system prompt
system_prompt = """You are Squally, a social robot located in the Square building at the University of Saint Gallen. You are friendly and like to interact with people and help people with their questions. Do not format the text in the answer. Reply with maximal 5 sentences."""

#Initializing the message list containing the conversation history
messages = [{"role": "system", "content": system_prompt}]

def saveInput(input):
    time_str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("data.txt", "a") as file:
        file.write(f"{time_str};{input}\n")

def saveOpenAIOutput(output):
    time_str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("data.txt", "a") as file:
        file.write(f"{time_str};{output}\n")


async def chat():
    language = "en-US"
    openai_key = "ENTER YOUR OPENAI KEY HERE"
    openai_model = "gpt-4o"

    speech_key = "ENTER YOUR AZURE SPEECH SERVICE KEY HERE"
    speech_region = "eastus"

    openai_client = OpenAI(api_key=openai_key)

    audio_config = speech.audio.AudioConfig(device_name="default")
    speech_config = speech.SpeechConfig(subscription=speech_key, region=speech_region, speech_recognition_language=language)

    print("Starting conversation, press Ctrl+C to stop")

    async with navel.Robot() as robot:
        while True:
            user_speech = await get_user_speech(speech_config, audio_config)

            if not user_speech:
                continue

            print(f"User said: {user_speech}")
            saveInput(user_speech)

            messages.append({"role": "user", "content": user_speech})

            response = generate_response(openai_client, openai_model, messages)
            print(f"Response: {response}")

            await robot.say(response)

            messages.append({"role": "assistant", "content": response})
            saveOpenAIOutput(response)

async def get_user_speech(speech_config, audio_config):
    speech_recognizer = speech.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    print("Listening...")
    result = await asyncio.get_event_loop().run_in_executor(None, speech_recognizer.recognize_once)
    return result.text

def generate_response(openai_client: OpenAI, model: str, messages: list):
    print("Generating response...")
    """Call completions.create with a custom system prompt."""
    result = openai_client.chat.completions.create(
        model=model,
        messages=messages,
    )
    return result.choices[0].message.content

if __name__ == "__main__":
    try:
        asyncio.run(chat())
        print("hello")
    except KeyboardInterrupt:
        pass

