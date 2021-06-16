#Exercide 2: Ask user to input n numbers and you have to print average of n numbers using string formatting.
#(User should be able to insert n numbers in one line with comma seperated)

print ("Enter no. with ',' as separator")
List = []
List = [int(i) for i in input().split(',')]
print ("Average = " + str(sum(List)/len(List)))