# E.g. word_count("I do not like it Sam I Am") gets back a dictionary like:
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}
# Lowercase the string to make it easier.

# def word_count(str_input):
#     str_tolist = str_input.lower().split(" ")
#     dic = {}
#     for s in str_tolist:
#         if s in dic.keys():
#             dic[s] += 1
#         else:
#             dic[s] = 1
#     return dic
#
# print(word_count("I do not like it Sam I Am How it doesn't work am i?"))

# words.count() learn from other leraner
# def word_count2(st):
#     my_dict = {}
#     words = st.lower().split(" ")
#     for word in words:
#         if word != " ":
#             my_dict.update({word: words.count(word)})
#     return my_dict
# print(word_count2("I do not like it   Sam I Am How it doesn't work am i?"))

# def word_count(str_input):
#     str_tolist = str_input.lower().split()
#     dic = {}
#     print(str_tolist)
#     for word in str_tolist:
#         # if word.isalpha():
#             dic.update({word: str_tolist.count(word)})
#     return dic
#
# print(word_count("I do not like    it!, ,  \nok i?"))

def courses(teacher_dic):
    courses = []
    for k in teacher_dic.keys():
        courses += teacher_dic[k]
    return courses
t = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
    'Kenneth Love': ['Python Basics', 'Python Collections']}
print(courses(t))
