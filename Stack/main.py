from functions import display, menu, pop, push


def main() -> None:
    mystack = []

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            number = int(input("Enter a number: "))
            push(mystack, number)

        elif choice == "2":
            if len(mystack) == 0:
                print("Stack is empty")
                continue

            number = pop(mystack)
            print("Popped number:", number)

        elif choice == "3":
            if len(mystack) == 0:
                print("Stack is empty")
                continue

            display(mystack)

        elif choice == "4":
            print("Goodbye")
            break

        else:
            print("Invalid choice")


main()
