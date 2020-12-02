def get_answer():
    file = open("numbers", "r")
    numbers = []
    for line in file:
        numbers.append(int(line))
    while numbers:
        compare = numbers.pop()
        for i in range(0, len(numbers) - 1):
            for x in range(0, len(numbers) - 1):
                if numbers[i] == numbers[x]:
                    continue
                if compare + numbers[i] + numbers[x] == 2020:
                    answer = compare * numbers[i] * numbers[x]
                    result = f"The answer is {answer}"
                    file.close()
                    return result


answer = get_answer()

print(answer)
