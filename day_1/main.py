file = open("numbers", "r")
numbers = []
answer = 0
for line in file:
    numbers.append(int(line))
while numbers:
    compare = numbers.pop()
    for number in numbers:
        if number + compare == 2020:
            answer = number * compare
            print(f"The answer is {answer}")
            break
    if answer:
        break
