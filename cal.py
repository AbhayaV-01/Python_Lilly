def take_sal():
    sal=int(input('Enter sal\n'))
    return sal

def hra(s):
    print("HRA:",(0.2*s)+s)

def da(s):
    print("DA:",(0.4)*s+s)

def bon(s):
    s=s+(0.1*s)
    print("Bonus:",s)
