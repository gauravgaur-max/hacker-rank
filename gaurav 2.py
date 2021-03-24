num=eval(input('enter the number'))
c=0
i=2
while(i<=num/2):
    if(num%i==0):
        c=c+1
        break
    i=i+1
    
if(c==0 and num!=1):
     print('it is prime')
else:
     print('number is not prime')
     
