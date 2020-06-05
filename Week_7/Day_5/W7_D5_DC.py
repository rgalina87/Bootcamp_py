def integer_number(num, bit_size):
    binary = bin(num)
    reverse = binary[-1:1:-1]
    reverse = reverse + (bit_size - len(reverse))*'0'
    print(int(reverse,2))
if __name__ == '__main__':
    num = int(input("Enter a num\n>>>"))
    bit_size = 32
    integer_number(num, bit_size)