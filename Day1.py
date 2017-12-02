def summatch(digits):
    if digits[0] == digits[-1]:
        sum = int(digits[0])
    else:
        sum = 0
    for i in range(len(digits)-1):
        if digits[i] == digits[i+1]:
            sum += int(digits[i+1])
    return sum

def summatch2(digits):
    sum = 0
    step = len(digits) // 2
    for i in range(len(digits)):
        if digits[i] == digits[(i + step) % len(digits)]:
            sum += int(digits[i])
    return sum