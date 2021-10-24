import register_voice
import get_voice_output_letter
import get_voice_volumn
import letter_classification

register_voice.register_voice()
speak_text = get_voice_output_letter.get_voice_output_letter()
speak_score = get_voice_volumn.get_voice_volumn()
speak_text_topic = letter_classification.letter_classification(speak_text)
