def countdown(start):
    numbers = []
    while start > 0:
        numbers.append(start)
        start -= 1
        print(numbers)
countdown(5)