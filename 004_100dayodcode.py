# Learning Python
# IF, ELSE, and print() with color code


print("--Pokemon adventure--")
print(
    """Welcome to the world of pokemon!
My name is Professor Oak.
People call me the pokemon professor.
This world is inhabited by creatures called pokemon.
For some people, pokemon are pets.
Others use them for fights.
Myself...
I study pokemon as a profession.
But we're here to give you a Pokemon.
So let's start with it.
Wich pokemon would you choose?""", "\033[32m \n 1.Venasaur, the grass pokemon",
    "\033[31m \n 2.Charmander, the fire pokemon",
    "\033[34m \n 3.Squirtle, the water pokemon \033[0m")

myPokemon = input("Wich pokemon do you choose?  ")
print("Excellent!")

print("Now it's time to go into your first battle!")
print("You are challenged by a wild pikachu!")

myAction = input("FIGHT or RUN?  ")
if (myAction == "FIGHT"):
    myAttack = input("What attack do you use? TACKLE or SPLASH?   ")

    if (myAttack == "TACKLE"):
        print(myPokemon, " used ", myAttack, "! It's super effective!")
        print("Pikachu fainted!")
        print("You win!")
    else:

        print(myPokemon, " used ", myAttack, "! But nothing happened")
        print("Pikachu used THUNDERBOLT!")
        print(myPokemon, " fainted!")
        print("You lose!")

else:
    print("You ran away safely!")
