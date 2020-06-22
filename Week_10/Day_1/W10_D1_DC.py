from googletrans import Translator

def f():
    translator = Translator()
    french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
    transl = []
    translation = translator.translate(french_words, src="FR", dest="EN")

    for x in translation:
        transl.append(x)
    # return transl

    tr = {french_words[t]:transl[t] for t in range(4)}
    print(tr)
f()