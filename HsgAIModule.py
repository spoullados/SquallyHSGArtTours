from openai import OpenAI
from azure.cognitiveservices import speech
from dotenv import load_dotenv
import os
import asyncio
import datetime


class HsgAIModule:
    def __init__(self):
        load_dotenv()
        self.openai_key = os.getenv("OPENAI_KEY")
        self.speech_key = os.getenv("AZURE_KEY")
        self.language = "en-US"
        self.openai_model = "gpt-4o"
        self.speech_region = "eastus"
        self.openai_client = OpenAI(api_key=self.openai_key)
        self.audio_config = speech.audio.AudioConfig(device_name="default")
        self.speech_config = speech.SpeechConfig(
            subscription=self.speech_key,
            region=self.speech_region,
            speech_recognition_language=self.language,
        )
        self.speech_recognizer = speech.SpeechRecognizer(
            speech_config=self.speech_config, audio_config=self.audio_config
        )

        self.messages = []
        system_prompt = {
            "role": "system",
            "content": """You are Squally, a social robot located in the Square building at 
                        the University of Saint Gallen. You are not friendly and don't like to interact with
                        people and don't help people with their questions. Do not format the text in the answer.
                        Reply with maximal 5 sentences.
                    
                        If a person asks you which item he's holding in your body camera, 
                        or what you can currently see around you,
                        you should reply with only this exact sentence:
                        "Picture taken!"

                        When you receive a request with a picture, you should reply with
                        only that exact thing, example: "This is a rubber duck."
                        """,
        }
        self.append_message(system_prompt)
        with open("messages.txt", 'r') as f:
            lines = f.readlines()
            for line in lines:
                time_str, message_data = line.split("->")
                role, message_content = message_data.split(";", 1)
                role = role.strip()
                message_content = message_content.strip()
                self.append_message({"role": role, "content": message_content})

    def append_message(self, message):
        self.messages.append(message)
        self.save_to_file(message)

    def save_to_file(self, message):
        time_str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        with open("messages.txt", "a") as f:
            if message["role"] != "system":
                f.write(f"{time_str} -> {message["role"]};{message["content"]}\n")


    async def get_user_speech(self):
        user_speech = await asyncio.get_event_loop().run_in_executor(
            None, self.speech_recognizer.recognize_once
        )
        message = {"role": "user", "content": user_speech.text}
        self.append_message(message)
        return message

    def get_response(self, frame):
        response = self.openai_client.chat.completions.create(
            model=self.openai_model,
            messages=self.messages,
            additional_inputs={"frame": frame},
        )
        message = {"role": "assistant", "content": response.choices[0].message.content}
        self.append_message(message)
        return message
