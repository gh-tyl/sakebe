# import speech_recognition as sr

# def get_voice_output_letter(path):
#     r = sr.Recognizer()
#     with sr.AudioFile(path) as source:
#         audio = r.record(source)
#     try:
#         text = r.recognize_google(audio, language='ja-JP')
#     except:
#         text = "読み込みに失敗しました。"
#     return text