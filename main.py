from pet import Pet

def main():
    pet_name = input("🐾 What is your pet's name? ")
    pet = Pet(pet_name)

    while True:
        print("\n🎮 Choose an action:")
        print("1. 🍖 Eat")
        print("2. 💤 Sleep")
        print("3. 🎾 Play")
        print("4. 🎓 Train")
        print("5. 🤹 Show Tricks")
        print("6. 📋 Get Status")
        print("7. 🚪 Exit")

        choice = input("➡️ Enter your choice (1-7): ")

        if choice == '1':
            pet.eat()
        elif choice == '2':
            pet.sleep()
        elif choice == '3':
            pet.play()
        elif choice == '4':
            trick = input("✨ Enter a trick for your pet to learn: ").upper()
            pet.train(trick)
        elif choice == '5':
            pet.show_tricks()
        elif choice == '6':
            pet.get_status()
        elif choice == '7':
            print(f"👋 Goodbye! {pet.name} will miss you! 🐾")
            break
        else:
            print("❌ Invalid choice, please try again.")

if __name__ == "__main__":
    main()