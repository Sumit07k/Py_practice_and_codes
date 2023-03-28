if __name__ == '__main__':
    s = input()
    alnum = alpha = digit = lower = upper = 'False'
    for i in s:
        if i.isalnum() == True:
            alnum = 'True'
        if i.isalpha() == True:
            alpha = 'True'
        if i.isdigit() == True:
            digit = 'True'
        if i.islower() == True:
            lower = 'True'
        if i.isupper() == True:
            upper = 'True'
    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)
