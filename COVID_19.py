#Hey Thala Write Your Code Here:

for i in range(int(input())):
    n,m=map(int,input().split())
    if m>2:
        if m%2==0:
            am=m//2
        else:
            am=(m//2)+1
    else:
        am=1
    
    
    if n>2:
        if n%2==0:
            print((n//2)*am)
        else:
            print(((n//2)+1)*am)
    else:
        print(am*1)
    
   
    