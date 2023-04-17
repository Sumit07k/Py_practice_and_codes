def print_formatted(number):
    # your code goes here
    l = len(bin(number).lstrip('0b')) + 1
    for i in range(1,number+1):
        intt = str(i).rjust(l-1)
        octt = str(oct(i)).lstrip('0o').rjust(l)
        hexx = str(hex(i)).lstrip('0x').upper().rjust(l)
        binn = str(bin(i)).lstrip('0b').rjust(l)
        print(intt + octt + hexx + binn)
    
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)