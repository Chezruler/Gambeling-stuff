import random

def spin_row():
    numberoutcome = random.randint(0, 26)
    print(numberoutcome)
    return numberoutcome

def getpayout(num, number_input, bet):
    if num == number_input:
        return bet * 2
    return 0

def main():
    balance = 100

    print("**************************************************")
    print("Welcome to the roullette place! have fun gambling!")
    print("**************************************************")
    while balance > 0:
        bet = input("Place your bet!: ")
        if not bet.isdigit():
            print("Thats not a bet! please add a bet")
            continue

        bet = int(bet)

        if bet < 0:
            print("Please place a bet!")
            continue
        elif bet > balance:
            print("You are to broke to afford that, place a lower bet!")
            continue

        balance -= bet

        number_input = int(input("Bet placed, what number do you go for? (1/99): "))

        
        print("spinning... \n")

        result = spin_row()
        payout = getpayout(result, number_input, bet)

        if getpayout(result, number_input, bet) == True:
            balance += bet

        

        print(f"Your balance is now {balance},")
        replay_input = input("Wanna play again?: ")

        if replay_input.upper != "Y":
            print("Game over! Have fun next time.")
            break

if __name__ == "__main__":
    main() 

