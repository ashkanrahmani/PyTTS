from gtts import gTTS
import os
some_text = "This is dummy text to create TTS content."
language = "en"
file_name = "tts_file.mp3"
obj = gTTS(text=some_text, lang=language, slow=False)
obj.save(file_name)
os.system("mpg123 "+file_name)
