answer = 0

for pwd in range(372304, 847060+1):
    digits = [int(x) for x in str(pwd)]
    has_pair = any([
        (i == 0 or digits[i] != digits[i-1]) and
        digits[i] == digits[i+1] and
        (i == len(digits)-2 or digits[i] != digits[i+2]) for i in range(len(digits)-1)])
    never_decreases = any([digits[i] > digits[i+1]
                           for i in range(len(digits)-1)])

    if has_pair and not never_decreases:
        answer += 1

print(answer)
