from bs4 import BeautifulSoup
import lxml
import re

with open("templates/kheyfets_page.html", "r") as kheyfets:
    contents = kheyfets.read()

soup = BeautifulSoup(contents, 'lxml')
# f = open("tags_kheyfets.txt", "w")
# for tag in soup.find_all(re.compile('padding')):
    # print(tag.text)
    # f.write(tag.text)
# f.close()

with open ('tags_kheyfets.txt', "r") as tags:
    entities = tags.readlines()

converted_entities = []
for element in entities:
    if element:
        converted_entities.append(element.strip("\\\n''"))
fin_entities = list(filter(None, converted_entities))

print(fin_entities)

d1 = {}
for i in range(0, len(fin_entities), 2):
    item = fin_entities[i+1]
    tag = fin_entities[i]
    d1[item] = tag
print(d1)

edit = tuple(fin_entities)
# n = tuple(edit)
# d1={[x[0]]:[x[1]] for x in n}
# print(d1)

# типа n = 0, слово = список[n], тег = список[n+1]
