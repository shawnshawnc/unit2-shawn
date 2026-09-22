""" bill = float(input("Input the amount of the bill."))
tip = int(input("Input the amount of the tip."))
total = bill + tip
print(f"Your bill is ${total}.") """

""" #create sentence variable
sentence = input("Please type a sentence!")
#split the users sentence
word = sentence.split()
#establish counter variable
counter = 0
#create for loop the runs for the amount of words in sentence
for words in word:
    #increase the counter by one for every word in user sentence
    counter += 1
#print final result
print(f"The number of words in your sentence is {counter}.") """

""" num = float(input("Input a number."))
r = num%2
if r == 0:
    print("Your number is even.")
else:
    print("Your number is odd.") """

""" bill = float(input("Input the amount of the bill."))
service = input("How was the service? 1 for bad, 2 for okay, 3 for good, 4 for great.")
poor = 0
almostpoor = bill*0.15
middleclass = bill*0.20
mrbeast = bill*0.25
if service == "1":
    print(f"We reccomend you to give them a 0% tip ({poor})")
elif service == "2":
    print(f"We reccomend you to give them a 15% tip ({almostpoor})")
elif service == "3":
    print(f"We reccomend you to give them a 20% tip ({middleclass})")
elif service == "4":
    print(f"We reccomend you to give them a 25% tip ({mrbeast})")
else:
    print("YOU GAVE ME A WRONG NUMBER") """

#number = int(input("Input a number"))



def factor(n):
    a = 1
    c = []
    while a != n + 1:
        if n % a == 0:
            c.append(a)
        a += 1
    return c

n1 = int(input("Input a number"))
n2= int(input("Input another number"))

def gcf(x,y):
    listx = factor(x)
    listy = factor(y)
    print(listx,listy)
    gcfs = []
    if listx and listy:
        gcfs += listx
    gcfs.remove(1)
    return gcfs
print(gcf(n1,n2))