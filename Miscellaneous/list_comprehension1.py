fruits = ["apple", "pear", "banana"]

for index, fruit in enumerate(fruits):
    
    if fruit == "apple":

        fruits[index] = fruit + " - " + "red-fruit"

print(fruits)