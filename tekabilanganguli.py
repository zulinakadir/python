
#!/usr/bin/env python

import random

def main():
    """Mula atur cara meneka bilangan guli."""

    print("*******************")
    print("Teka bilangan guli")
    print("*******************")
    print("** Nota: bilangan guli antara 20 hingga 50")
    print("** dan anda hanya diberi 3 cubaan sahaja")

    """mengambil nilai secara rawak antara 20 hingga 50."""
    x = random.randint(20, 50)
    
    """menetapkan nilai percubaan"""
    max_trials= 3
    trial=0
    guess = None
    
    #print(x)
    while trial<max_trials:
        guess = int(input("Berapakah bilangan guli yang ada? "))
        
        if x == guess:
            print(f"Tahniah tekaan anada betul!".format(guess))
            break
        else:
            print(f"Maaf...Tekaan anda salah.".format(guess))
            max_trials -= 1
            print(f"anda ada {max_trials} kali cubaan lagi.")
            
        if max_trials == 0:
            print(f"cubaan tamat. bilangan guli yang ada ialah {x}.".format(guess))
        43
main()
