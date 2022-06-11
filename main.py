from translate import Translator

translator = Translator(to_lang='fr')

with open('orig.txt') as original:
    text = original.read()
    new_text = translator.translate(text)
    with open('translated.txt', mode='r+') as new:
        new.truncate(0)
        new.write("new_text")
        new.seek(0)
        print(new.read())










