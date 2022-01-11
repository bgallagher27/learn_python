bicycles = ["trek", "cannondale", "redline", "specialized",]
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])   # returns the last item in the list
print(bicycles[-2])   # returns the second item from end of list
print(bicycles[-3])   # returns the third item from end of list, etc...
                      # list[-n] will return nth item from end of the list

message = f"My first bicycle was a {bicycles[0].title()}"
print(message)