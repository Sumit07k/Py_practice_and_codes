def print_rangoli(size):
    # your code goes here
    x = 4 * size - 3
    strr = 'abcdefghijklmnopqrstuvwxyz'
    L = []
    for i in range(size):
        y = '-'.join(strr[i:size])
        L.append((y[::-1]+y[1:]).center(x,'-'))
    print('\n'.join((L[:0:-1]+L)))
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)