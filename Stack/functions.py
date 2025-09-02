def menu() -> None:
    print()
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")


def push(stack: list[int], item: int) -> None:
    stack.append(item)


def pop(stack: list[int]) -> int:
    return stack.pop()


def display(stack: list[int]) -> None:
    for item in stack:
        print(item)
