from subject_verb_object_extract import findSVOs, nlp
from subject_verb_object_extract import displacy
str1 = "Then there’s a development setback on top of that that pushes you even further back."
str2 = "there is, in fact, a very strong correlation between concepts of topic and subject in English."
str3 = "Seated in Mission Control, Chris Kraft neared the end of a tedious Friday afternoon as he monitored a " \
       "seemingly interminable ground test of the Apollo 1 spacecraft."
str4 = "The man hit the ball and he fractured his finger."

token_list = []

tokens1 = nlp(str1)
svos1 = findSVOs(tokens1)
print("\n1")
print(str1)
print(svos1)
token_list.append(tokens1)

tokens2 = nlp(str2)
svos2 = findSVOs(tokens2)
print("\n2")
print(str2)
print(svos2)
token_list.append(tokens2)

tokens3 = nlp(str3)
svos3 = findSVOs(tokens3)
print("\n3")
print(str3)
print(svos3)
token_list.append(tokens3)

tokens4 = nlp(str4)
svos4 = findSVOs(tokens4)
print("\n4")
print(str4)
print(svos4)
token_list.append(tokens4)

displacy.serve(token_list, style="dep")