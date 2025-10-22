import random

def get_choice_name(choice):
    return ["Snake 🐍", "Water 💧", "Gun 🔫"][choice]

def check(comp, user):
    if comp == user:
        return 0
    if (comp == 0 and user == 1) or (comp == 1 and user == 2) or (comp == 2 and user == 0):
        return -1
    return 1

user_score = 0
comp_score = 0

print("🎮 Welcome to Snake 🐍 Water 💧 Gun 🔫 Game!")
print("Instructions: Enter 0 for Snake, 1 for Water, 2 for Gun")

while True:
    comp = random.randint(0, 2)
    try:
        user = int(input("\nYour turn (0-Snake, 1-Water, 2-Gun): "))
        if user not in [0, 1, 2]:
            print("⚠️ Invalid input. Please enter 0, 1, or 2.")
            continue
    except ValueError:
        print("⚠️ Please enter a number.")
        continue

    print(f"You chose: {get_choice_name(user)}")
    print(f"Computer chose: {get_choice_name(comp)}")

    score = check(comp, user)

    if score == 0:
        print("🤝 It's a draw!")
    elif score == -1:
        print("😞 You Lose!")
        comp_score += 1
    else:
        print("🎉 You Won!")
        user_score += 1

    print(f"📊 Score => You: {user_score} | Computer: {comp_score}")

    play_again = input("Play again? (y/n): ").lower()
    if play_again != 'y':
        print("👋 Thanks for playing!")
        break





