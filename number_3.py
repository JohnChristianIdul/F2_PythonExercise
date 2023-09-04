# count number of digit in given integer
a = int(input("Please enter a number: "))
smallest = 100;
highest = 0;
count = 0;
while(a!=0):
    b = a%10
    if(b <= smallest):
        smallest = b;
    if(b >= highest):
        highest = b;
    count+=1
    a//=10;

print("Number of digits in a given number is: ", count)
print("Smallest number is: ", smallest)
print("Highest number is: ", highest)

# sum of all numbers from 1 to input
a = int(input("Enter a number: "))
i = 1
sum = 0
count = 1
while(count <= a):
    sum += i
    i+=1
    count += 1
    print("i: ",i)
    print("sum: ",sum)
    print("count: ",count)
print(sum)