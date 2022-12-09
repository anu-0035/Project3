def findMissingNumbers(n):
    numbers = set(n)
    length = len(n)
    output = []
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
    print(output)
    
l = list(eval(input("enter more than one numbers seperated by ','")))
findMissingNumbers(l)
