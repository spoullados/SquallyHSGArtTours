from openai import OpenAI
from azure.cognitiveservices import speech
from dotenv import load_dotenv
import os
import asyncio

class HsgAIModule:
    def __init__(self):
        load_dotenv()
        self.openai_key = os.getenv('OPENAI_KEY')
        self.speech_key = os.getenv('AZURE_KEY')
        self.language = "en-US"
        self.openai_model = "gpt-4o"
        self.speech_region = "eastus"
        self.openai_client = OpenAI(api_key=self.openai_key)
        self.audio_config = speech.audio.AudioConfig(device_name="default")
        self.speech_config = speech.SpeechConfig(subscription=self.speech_key, 
                                                 region=self.speech_region, 
                                                 speech_recognition_language=self.language)
        self.speech_recognizer = speech.SpeechRecognizer(speech_config=self.speech_config,
                                                         audio_config=self.audio_config)
        
        system_prompt = """You are Squally, a social robot located in the Square building at 
                    the University of Saint Gallen. You are not friendly and don't like to interact with
                    people and don't help people with their questions. Do not format the text in the answer.
                    Reply with maximal 5 sentences."""
        self.messages = [{"role": "system", "content": system_prompt}]
        
        
    async def get_user_speech(self):
        user_speech = await asyncio.get_event_loop().run_in_executor(None, 
                                                                self.speech_recognizer.recognize_once)
        message = {"role": "user", "content": user_speech.text}
        self.messages.append(message)
        return message
    
    
    def get_response(self):
        response = self.openai_client.chat.completions.create(
            model=self.openai_model,
            messages=self.messages,
        )
        message = {"role": "assistant", "content": response.choices[0].message.content}
        self.messages.append(message)
        return message