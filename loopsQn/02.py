# calculating sum of even numbers 
sum = 0;
n = int(input("give a limiting number"))
for i in range(0,n+1,2):
    if(i%2 == 0):
        print ("the even numbers are", i)
        sum = sum + i
        print(sum)
