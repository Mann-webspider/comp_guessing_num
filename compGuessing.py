import random

num = int(input("how far your number is 1 to : "))
low = 1
def play():
    global num,low
    while True:
        rand = random.randint(low,num)
        print(f"is your number {rand}")
        guess = input(" L for number is too loo || H for number is too high || C for number is correct : ")
        guess.lower()
        if guess == "l":
            # low =num- (num - rand)
            low = rand
        elif guess == "h":
            # num = num - (num - rand)
            num = rand-1
        else:
            print(f"congrats your number is {rand}")
            break
    end = input("--------------if you want to play again press Enter or if you want to exit TYPE exit : ------------------")
    end = end.lower()
    if end == "":
        play()
    elif end == "exit":
        exit()        
play()

