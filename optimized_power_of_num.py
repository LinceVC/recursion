## Program to find power of number using recurssion in optimized manner 


def optim_power(base,pwr):
    
    if pwr == 0:
        return 1
    
    half = optim_power(base,pwr//2)
    
    print(half)
    if pwr%2==0:
        return half*half
    else:
        return base*half*half
    
##Input base and power
base =int(input())
pwr = int(input())

optim_power(base,pwr)
