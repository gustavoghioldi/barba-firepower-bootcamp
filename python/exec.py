di = {}
print("-- inicio del programa ---")
print(di)

try:
    int("asjkdhjkash")
    print(di["coco"])
except KeyError:
    print("error de llave")
except ValueError:
    print("no puedo convertir a int")
except Exception:
    print("Fallo y no se porque ")

print("-- fin del programa ---")
