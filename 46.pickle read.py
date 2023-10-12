import pickle

file=open("45.pickle.txt", "rb")

l=pickle.load(file)
print(l)