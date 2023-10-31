import re

def check_for_words_in_transcription(transcribed_text):
    # Use regular expressions to split the text into words
    transcribed_text = transcribed_text.lower()
    words = re.findall(r'\b\w+\b', transcribed_text)
    words_to_check = [
   "vazhai pazham", "police", "doctor", "fan", "phone", "kappal", "table", "pattam", "kuzhandhai", 
   "maadu", "banana", "pazham", "kaval karar", "inspector", "maruthuvar", "min visiri", "mobile", 
   "cell phone", "alaipesi", "ship", "mesai", "kathadi", "kite", "papa", "baby", "cow", "pasu maadu"]
    
    present_words = [word for word in words_to_check if word in words]

    if present_words:
        print(f"Words present in the transcription: {', '.join(present_words)}")
    else:
        print("No specified words are present in the transcription.")
