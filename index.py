import random

roll_count = 0  # Counter for number of rolls

while True:
    choice = input('Roll the dice? (y/n): ').lower()

    if choice == 'y':
        try:
            num_dice = int(input("How many dice do you want to roll? "))
            if num_dice <= 0:
                print("Please enter a positive number of dice.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        roll_count += 1
        results = [random.randint(1, 6) for _ in range(num_dice)]
        print(f'Roll {roll_count}: {tuple(results)}')

    elif choice == 'n':
        print(f'Thanks for playing! You rolled the dice {roll_count} times.')
        break

    else:
        print('Invalid choice!')
