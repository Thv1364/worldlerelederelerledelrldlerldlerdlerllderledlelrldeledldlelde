possible_words=["forte", "piano", "septa", "skype", "scant", "lacks", "metro", "clamp", "plumb", "stamp", "sharp", "flats", "prats", "horns", "forts", "forks", "salem", "ogden", "akron", "plano", "quito", "syria", "cairo", "italy", "paris", "milan", "tunis", "lagos", "delhi", "tulsa", "boise", "raton", "havre", "rugby", "fargo", "poway"]




























import random

word = random.choice(possible_words)


#colors
default= '\033[0m'
green= '\033[92m'
yellow= '\033[95m'

def generate_hint(user_guess):
    color=default
    hint=""
    for i in range(5):
        if(user_guess[i]==word[i]):
            color=green
        elif(user_guess[i] in word):
            color=yellow
        else:
            color=default
        hint=hint+color+user_guess[i]+default
    return hint






def gameloop():
    guess=""
    for i in range(6):
        guess=input("what is your guess: ")
        print(generate_hint(guess))
        if guess==word:
            print("gonratuations!")
            break
    if guess!= word:
        print("\n haha you lose idiot")
        print("The word was: " + word)

gameloop()