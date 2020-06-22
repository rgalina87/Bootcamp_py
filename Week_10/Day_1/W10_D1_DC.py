from translate import Translator

def f():
    french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
    transl = []

    translator = Translator(from_lang="FR", to_lang="EN")
    translation = translator.translate()

    for x in translation:
        transl.append(x)

    tr = {french_words[t]:transl[t] for t in range(4)}
    return tr

print(f())