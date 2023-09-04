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