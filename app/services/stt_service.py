# श्री राम नाग जी, यह शिव एआई के कान हैं (Speech-to-Text)
import speech_recognition as sr

class SpeechToTextManager:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen_and_convert(self):
        """आवाज़ को सुनकर उसे हिंदी/इंग्लिश टेक्स्ट में बदलना"""
        with self.microphone as source:
            print("सुन रहा हूँ, मालिक...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            # हम इसे हिंदी और इंग्लिश दोनों के लिए कॉन्फ़िगर करेंगे
            text = self.recognizer.recognize_google(audio, language='hi-IN')
            return text
        except Exception as e:
            return ""

stt_port = SpeechToTextManager()

