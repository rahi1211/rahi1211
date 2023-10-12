import pickle

with open("45.pickle.txt", "rb") as file:
    finaldata = pickle.load(file)
    print(finaldata)
for a in finaldata:
    print(a)


