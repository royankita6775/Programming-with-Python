from typing import Counter


filename = "names.txt"
names = [""]
try:
    file = open(filename, "rt")
    names = file.readlines()
except:
    print("Failed to read file: " + filename)
finally:
    file.close()

sorted_names = sorted(names)
for name in sorted_names:
    print("{}".format(name.strip()))
    print(sorted_names.count(name))
c = Counter(sorted_names)
print(sum(c.values()))
