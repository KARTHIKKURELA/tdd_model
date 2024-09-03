def add(numbers):
    if not numbers:
        return 0
    nums = numbers.split(",")
    total = 0
    for num in nums:
        total += int(num)

    return total
