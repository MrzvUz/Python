name = 'Ali'
greeting = f"How are you {name}?"
print(greeting)

name = "Mirzaev"
mirzaev_greeting = f"how are you {name}?"
print(mirzaev_greeting)
print(greeting)

print()

name = 'Ali'
greeting = 'How are you {}?'
ali_greeting = greeting.format(name)
print(ali_greeting)

name = 'Mirzaev'
greeting = greeting.format(name)
print(greeting)

print()

name = "Rolf Smith"
street = "123 No Name Road"
postcode = "PY10 1CP"
 
address = f"""Name: {name}
Street: {street}
Postcode: {postcode}
Country: United Kingdom"""
 
print(address)

