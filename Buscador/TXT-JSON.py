import json
file_input = open('fileoutput.txt', 'r')
file_input.readline()

diccionario = {}
for row in file_input:
    word,doc_count = row.split('\t')
    for data in doc_count.replace('\n', '').replace(' ', '').replace('(', '').split(')')[0:-1]:
        doc,count = data.split(',')
        if word in diccionario.keys():
            diccionario[word][doc] = int(count)
        else:
            diccionario[word] = {doc:int(count)}

with open("bbdd.json", "w") as outfile:
    json.dump(diccionario, outfile)

with open('bbdd.json', 'r') as openfile:
    json_object = json.load(openfile)

print(list(json_object['years'].keys()))

