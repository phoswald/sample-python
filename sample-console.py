import time

def clear_console():
    #print("\033c", end='')
    #print("")
    print("\033c")

def read_münze():
    while True:
        str = input("Münze? ")
        if str == "exit":
            return -1
        try:
            wert = float(str)
            if wert == 0.05 or wert == 0.1 or wert == 0.2 or wert == 0.5 or wert == 1 or wert == 2 or wert == 5:
                return wert
            print("Keine gültige Münze! Probier nochmal.")
        except ValueError:
            print("Nicht mal eine Zahl, du Affe! Probier nochmal, oder 'exit' um aufzugeben.")

name = input("Wer bist du? ")

clear_console()
print(f"Hello, {name}!")
time.sleep(0.5)

clear_console()
time.sleep(0.5)

clear_console()

wert = read_münze() # liefert einen Wert oder -1 um zu beenden
if wert != -1:
    print(f"OK, CHF {wert}")

print("Adieu")
