def segment(text, word_list):
    if not text:
        return True
    
    if not word_list:
        return False
    
    word = word_list[0]
    if word and word in text:
        remaining_text = text.replace(word, "", 1)
        if segment(remaining_text, word_list) or segment(text, word_list[1:]):
            return True
        
    return segment(text, word_list[1:])

inp = input('Enter list[str]: ').split("'")[1::2]
text, language = inp[0], inp[1:]

print(f"text: str = '{text}'")
print(f"lang: list[str] = {language}")
print(f"segment(text, lang) -> {segment(text, language)}")