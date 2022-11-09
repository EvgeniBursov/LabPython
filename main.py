import random
def bin(num):
    for i in range(num):
        print(f'{random.randint(0,256):08b}')

def dec(num):
    return set(f'{num:.0f}')


def sqrt(num):
    for i in range(1,num+1):
        if (i*i)==num:
            return i
    return False


def positive():
    arr=[]
    while True:
        num=int(input("Enter num: "))
        if num>=0:
            arr.append(num)
        else:
            return arr
            break


