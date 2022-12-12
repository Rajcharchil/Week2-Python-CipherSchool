# ask user a number like 1356
# calculate the sum of digits ---> 1+3+5+6
sum=0
num=input("Enter any number:")
for i in range(0, len(num)):
    sum+=int(num[i])
print(sum)
