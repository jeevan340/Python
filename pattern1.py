num_rows = 5

for i in range(num_rows):
    for j in range(num_rows - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print("* ", end="")
    print()
