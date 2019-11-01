"""Generate funny names by randomly combining names from 2 separate lists"""
import sys
import random

def main():
    """Choose names at random from 2 tuples of names and print to screen."""
    print("Welcome to the Psych 'Sidekick Name Picker.'\n")
    print("A name just like Sean would pick for Gus:\n\n")

    first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill, 'Beenie-Weenie'")

    last = ('Appleyart', 'Bigmeat', 'Littlemeat', 'Bloominshine', 'Boogerbottom', 'Clutterbuck', 
    'Cocktoasten', 'Jefferson','Jingley-Schmidt')

    while True:
        first_Name = random.choice(first)
        last_Name = random.choice(last)

        print("\n\n")
        print("{} {}".format(first_Name, last_Name), file=sys.stderr)
        print("\n\n")

        try_again = input("\n\nTry again?  (Press Enter else n to quit)\n ")
        if try_again.lower() == "n":
            break

    input("\nPress Enter to Exit.")

if __name__ == "__main__":
    main()