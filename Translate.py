from translate import Translator

translator = Translator(to_lang='ja')

try:
    with open('input.txt', mode='r') as file:
        text = file.read()
        translation = translator.translate(text)

        with open('output.txt', mode='w', encoding='utf-8') as file2:
            file2.write(translation)

except:
    print('Something is not ok')