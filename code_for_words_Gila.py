import pymorphy2
import re
import string
from os import read

import stanza
import spacy
from spacy import displacy
from spacy_stanza import StanzaLanguage


# stanza.download('ru')
snlp = stanza.Pipeline(lang="ru")
nlp = StanzaLanguage(snlp)

morph = pymorphy2.MorphAnalyzer()

with open("list_of_words") as f:
    key_words = f.read().split()

lex_list = []
for word in key_words:
    lex = morph.parse(word)
    for l in lex:
        lex2 = l.lexeme
        for w in lex2:
            lex3 = w.word
            lex_list.append(lex3)
print(lex_list)


with open("Kheyfets.txt") as k:
    jews = str(k.readlines())

r = open(r'raisabaraz.txt', encoding="UTF-8")
text = r.read()

raisa_tagged = []
for entry in text.split():
    if entry not in lex_list:
        raisa_tagged.append(entry)
    else:
        a = '<button type="button" class="btn btn-primary btn">' + entry + '</button>'
        raisa_tagged.append(a)
s = ' '
end_raisa = s.join(raisa_tagged)

doc2 = nlp(end_raisa)
ent_page2 = displacy.render(doc2, style="ent")
f = open("raisa_page.html", "w")
f.write(ent_page2)
f.close()

# kheyfets_tagged = []
# for entry in jews.split():
#     if entry not in lex_list:
#         kheyfets_tagged.append(entry)
#     else:
#         a = '<button type="button" class="btn btn-primary btn">' + entry + '</button>'
#         kheyfets_tagged.append(a)
# print(kheyfets_tagged)
# s = ' '
# end_kheyfets = s.join(kheyfets_tagged)
#
# doc = nlp(end_kheyfets)
# ent_page = displacy.render(doc, style="ent")
# f = open("kheyfets_page.html", "w")
# f.write(ent_page)
# f.close()
