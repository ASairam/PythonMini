def collatz(number):
    if number%2==0:
        print(number//2)
        return number//2
    else:
        print(number*3+1)
        return number*3+1
print("Enter an integer")
try:
    n= int(input())
except:
    print("Enter *INTEGER* value")
while(n!=1):
 n=collatz(n)
