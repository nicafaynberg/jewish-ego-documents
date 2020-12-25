from pymystem3 import Mystem
from string import punctuation
import re

text1 = open("raisabaraz.txt", "r")
my_string = text1.read()
words = open("list_of_words", 'r')
wordlist = words.read()

m = Mystem()
stemmed = m.lemmatize(my_string)
raisa = my_string.split()
#stemmed и raisa - это списки
stemmed1 = ''.join(stemmed)
stemmed2 = stemmed1.split()


keywords = wordlist.split()
nonlemm_tags = []
for word in stemmed2:
    if word not in keywords:
        nonlemm_tags.append(word)
    else:
        a = '<p class="topic">' + word + '</p>'
        nonlemm_tags.append(a)
print(nonlemm_tags)

# print(len(list(enumerate(raisa))))
# print(len(list(enumerate(nonlemm_tags))))


# list3 = []
# for word in raisa:
#     if word in stemmed and wordlist:
#         list3.append(word)
#     else:
#         continue
# output = [word.strip() for word in m.lemmatize(my_string)]
# output_new = [word for word in output if re.search ('[А-ЯЁа-яёA-Za-z]', word) != None]
#
# with open("list_of_words") as f:
#     key_words = f.read().split()
# print(key_words)
# filtered_text = []
# for word in output_new:
#     if word in key_words:
#         filtered_text.append(word)
#     else:
#         continue
# # filtered_text = [word for word in output_new if word in key_words]
# print(filtered_text)
#
# with open('raisabaraz4.txt', 'w') as f:
#     for word in output_new:
#         if word in key_words:
#             f.write('<p class="Ключевое слово">' + word + '</p>')

# with open("list_of_words") as f:
#     content = f.read()
# print(content)
# # # low = str(content).lower()
# # new = str(content).replace('\\n','')
# # print(new)
# #
# with open("raisabaraz.txt") as k:
#     jews = str(k.readlines())
#     raisa = str(jews).replace('\\n', '')
#     raisa2 = str(raisa).replace('\\ufeff', '')
#
# m = Mystem()
# stemmed = m.lemmatize(raisa2)
# # stringstemmed = ''.join(stemmed)
# #
# # stemmed_words = m.lemmatize(''.join(content))
# # print(stemmed_words)
# #
# # clean = []
# # for piece in stemmed:
# #     if piece not in punctuation:
# #         clean.append(piece)
# #     else:
# #         continue
# # print(''.join(clean))
# # print(clean)
# for word in stemmed:
#     if any(word in stemmed for word in content):
#         print(word)
#
# wordlist = []
# for word in stemmed:
#     if word in content:
#         wordlist.append(word)
#     else:
#         continue
#
# print(wordlist)
