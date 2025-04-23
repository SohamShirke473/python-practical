
with open("input.txt", "r") as file:
    cities = file.readlines()
    cities = [city.strip() for city in cities]
    cities.sort()

with open("output.txt", "w") as sorted_file:
    for city in cities:
        sorted_file.write(city + "\n")

print("City names sorted and written to output.txt.")

