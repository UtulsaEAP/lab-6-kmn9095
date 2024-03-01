def food_input():
    while True:
        user_input = input()
        tokens = user_input.split()
        if tokens[0] == "quit":
            break
        else:
            food = tokens[0]
            quantity = int(tokens[1])
            print(f"Eating {quantity} {food} a day keeps you happy and healthy.")

if __name__ == "__main__":
    food_input()
