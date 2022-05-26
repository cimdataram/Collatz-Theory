# Search a number that disproves Collatz theory :-D
# Probably an endless loop due to the natural law of the theory
num = 1
test = 1
while num == 1:
    num = test
    while num != 1:
        if num % 2 == 0:
            num = int(num / 2)
        else:
            num = 3 * num +1
        print(test, end=' : ')
        print(num)
    if num == 1:
        test += 1
else:
    print('disprove number: ', test)

