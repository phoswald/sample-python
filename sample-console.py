import time

def clear_console():
    #print("\033c", end='')
    #print("")
    print("\033c")

name = input("Wer bist du? ")

clear_console()
print(f"Hello, {name}!")
time.sleep(0.5)

clear_console()
time.sleep(0.5)

clear_console()
print("Ciao!")
time.sleep(0.5)

clear_console()
