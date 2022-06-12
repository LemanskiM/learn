filename = "c:\\python\\artur.txt"

line = "Europe"

cities = ["12","212","saw"]

file = open(filename, "a")

file.write(line)
file.write("\n")
#file.writelines(cities)
for city in cities:
    file.write("\n"+city)

file.close()
