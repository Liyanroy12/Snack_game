import random


def choose_snack():
    snacks = ['Chips', 'Chocolate', 'Fruit', 'Popcorn', 'Cookies']
    return random.choice(snacks)


def main():
    print("Welcome to the Snack Game!")

    while True:
        input("Press Enter to choose a snack...")

        snack = choose_snack()

        print(f"You got: {snack}!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()
