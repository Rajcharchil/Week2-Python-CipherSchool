# function inside function
def new_greatest(a,b,c):
    # bigger = greater(a,b)
    return max(max(a,b),c)
print(new_greatest(10,20,30))