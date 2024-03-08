def food_input():
    while True:
        user_input = input()
        tokens = user_input.split()
        if tokens[0] == "quit":
            break
        else:
            food = tokens[0]
            print(f"Eating {' '.join(tokens[1:])} {food} a day keeps you happy and healthy.")

if __name__ == "__main__":
    food_input()
