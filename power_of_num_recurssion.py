## power of given number using recurssion 
## Author: Lince
## Date: 11Feb 2023

def power_of_num_rec(base,pwr):
    if pwr ==0:
        return 1
    
    if base == 0:
        return 0
    
    if pwr<0:
        return "Invalid Power"
    return base*power_of_num_rec(base,pwr-1)


##Input base and power
base =int(input())
pwr = int(input())

power_of_num_rec(base,pwr)
