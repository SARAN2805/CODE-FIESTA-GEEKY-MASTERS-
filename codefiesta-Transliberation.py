from googletrans import Translator 

translator = Translator()
language = {
    "hi": "Hindi",
    "ta": "Tamil", 
    'pa': 'punjabi',
    'te': 'telugu',
    'ur': 'urdu',
    'gu': 'gujarati',
    'kn': 'kannada',
    'ml': 'malayalam',
    'mr': 'marathi',
    'en' : 'english'
}

default = 'en'
string = input("\nWrite the text you want to translate: ")
translated = translator.translate(string , dest=default)
print(f"\n{language[default]} translation: {translated.text}")