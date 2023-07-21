f = open("my-file.txt", "w") # a = attach, w= write , r= read

f.write("hola\n")
f.write("soy El Barba")

f.close()

f = open("my-file.txt", "r")

text = f.readline()
print(f.readline())
f.close()
print(text)

f = open("my-file.txt", "r")
for i in f.read().splitlines():
    print(i)
f.close()

with open ("algo.txt", "w") as f:
    f.write("algo")