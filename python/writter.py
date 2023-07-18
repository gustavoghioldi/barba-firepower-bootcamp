class Writer:
    def __init__(self, filename):
        self.__filename = filename

    def write(self, text):
        with open(self.__filename, "w") as f:
            f.write(text)
    
    def read(self):
        with open(self.__filename, "r") as f:
            print(f.read())

    def attach(self, text):
        with open(self.__filename, "a") as f:
            f.write(text)

w = Writer("hola23.txt")
w.write("Hola mundo\n")
w.read()
w.attach("hola de nuevo")
w.read()