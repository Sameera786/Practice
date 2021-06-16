#Exercise4: Ask a user for name  # Example: John Doe #Print count of each word #Output: J : 1 o : 2 h : 1 n : 1 d : 1 e : 1

name = input("Enter name:")
alphabet_frequency = {}

for alphabet in name:
    if alphabet in alphabet_frequency :
        alphabet_frequency [alphabet] += 1
    else:
        alphabet_frequency [alphabet] = 1

print ("Frequency of Alphabet:\n " ,(alphabet_frequency ))