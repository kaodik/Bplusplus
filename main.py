n = int(input())
def print_hi(n):
    x = 0
    output = 0
    while x < n:
        val = input()
        if val == '++X' or val == 'X++':
            output +=1
        elif val == '--X' or val == 'X--':
            output -=1


        x +=1

    print(output)
if __name__ == '__main__':
    print_hi(n)

