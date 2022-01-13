names = ["Adam", "Nick", "Jeremy"]
print(names[0])
print(names[1])
print(names[2])

print(f"Hello: {names[0]}")
print(f"Hello: {names[1]}")
print(f"Hello: {names[2]}")

makes = ["Volkswagen", "Audi", "BMW"]
models = ["Tiguan", "Atlas", "A7", "A5"]
print(f"I would like to own a {makes[0]} {models[1]}.")
print(f"I would like to own a {makes[1]} {models[2]}.")

dinner_guests = ["David Ortiz", "George Washington", "Ragnar Lothbrook"]
print(f"Dear {dinner_guests[0]}, you are officially invited to dinner at my humble abode!")
print(f"Dear {dinner_guests[1]}, you are officially invited to dinner at my humble abode!")
print(f"Dear {dinner_guests[2]}, you are officially invited to dinner at my humble abode!")

print(f"Unfortunately, {dinner_guests[2]} can't make it to dinner. We will have to invite someone else.")
del dinner_guests[2]
dinner_guests.append("Dustin Pedroia")
print(f"Dear {dinner_guests[0]}, you are still officially invited to dinner at my humble abode!")
print(f"Dear {dinner_guests[1]}, you are still officially invited to dinner at my humble abode!")
print(f"Dear {dinner_guests[2]}, you are officially invited to dinner at my humble abode!")

print("Good news! We found a bigger dinner table so we can invite more guests!")
dinner_guests.insert(0, "Patrice Bergeron")
dinner_guests.insert(2, "Brad Marchand")
dinner_guests.append("Obi-Wan Kenobi")
print(f"Dear {dinner_guests[0]}, you are officially invited to dinner at my humble abode!")
print(f"Dear {dinner_guests[1]}, you are officially invited to dinner at my humble abode!")
print(f"Dear {dinner_guests[2]}, you are officially invited to dinner at my humble abode!")
print(f"Dear {dinner_guests[3]}, you are officially invited to dinner at my humble abode!")
print(f"Dear {dinner_guests[4]}, you are officially invited to dinner at my humble abode!")
print(f"Dear {dinner_guests[5]}, you are officially invited to dinner at my humble abode!")

print("Bad news. Amazon is backed up so the new dinner table won't arrive in time. We can only invite two guests.")
print(f"Sorry, {dinner_guests.pop(0)}. You didn't make the cut")
print(f"Sorry, {dinner_guests.pop()}. You didn't make the cut")
print(f"Sorry, {dinner_guests.pop()}. You didn't make the cut")
print(f"Sorry, {dinner_guests.pop(1)}. You didn't make the cut")
print(f"Congratulations, {dinner_guests[0]} and {dinner_guests[1]}! You're still invited to dinner!")
del dinner_guests[0]
del dinner_guests[0]
print(dinner_guests)