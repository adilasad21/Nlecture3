people = [
    {"name": "Harry", "house": "Islb"},
    {"name": "Aadil", "house": "Sialkot"},
    {"name": "Osama", "house": "Lahore"},
    {"name": "Kaneez", "house": "Oakville"},
    {"name": "Z.Ali", "house": "karachi"},
]

#option1: define a function and sort it
def f(person):
    #return person["name"] #to sort by name
    return person["house"] #to sort by house

people.sort(key=f)

#option2: sort it in one line by using lambda
#people.sort(key=lambda person: person["name"])

print(people)