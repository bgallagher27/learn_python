motorcycles = ["Honda", "Yamaha", "Suzuki"]
print(motorcycles)

motorcycles[0] = "Ducati"
print(motorcycles)

motorcycles.append("ducati")
print(motorcycles)

append_motorcycles = []

append_motorcycles.append("honda")
append_motorcycles.append("yamaha")
append_motorcycles.append("suzuki")

print(append_motorcycles)

append_motorcycles.insert(0, "ducati")
print(append_motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned}")

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned}")

motorcycles.remove("ducati")
print(motorcycles)

too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(f"A {too_expensive} is too expensive for me.")