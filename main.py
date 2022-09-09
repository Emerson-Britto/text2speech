from gtts import gTTS
import re

text = input("Type something or enter 'from::FILE_PATH': ")

if "from::" in text:
	text = re.sub(r"\'|from::", '', text)
	with open(text, "r") as f:
		text = f.read()

language = "en"

tts = gTTS(text=text, lang=language, slow=False)
nameInput = input("Type a specific file name? (Or use default): ")
filename = nameInput if nameInput else re.sub(r'\W', '-', text)
fileformat = "mp3"
filepath = f"voices/{filename[0:70]}.{fileformat}"
tts.save(filepath)
print(f"The file was saved ({filepath})")