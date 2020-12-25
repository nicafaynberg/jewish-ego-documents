from os import read

import stanza
import spacy
from spacy import displacy
from spacy_stanza import StanzaLanguage


# stanza.download('ru')
snlp = stanza.Pipeline(lang="ru")
nlp = StanzaLanguage(snlp)

with open("Kheyfets.txt") as k:
    jews = str(k.readlines())

# text = open("raisabaraz.txt").readlines()
doc = nlp(jews)
ent_page = displacy.render(doc, style="ent")
# locations_kheyfets =
# reg_loc = re.findall("(\w+)}", ent_page)
