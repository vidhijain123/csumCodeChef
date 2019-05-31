#name:vidhijain
#date:30/05/19
#Problem Statement:check if there exist any pair of index i,j such that Ai+Aj=K and i≠j
#author:vidhijain123
'''
Algorithm:
1. Start 
2. Read number of testcases
3. For each testcase read an number of integer and an integer k
4. Read an array
5. loop i and j such that i<j
6. if a[i]+a[j]==k
7. Change the value of flag
8. Print the yes and no
9. Stop
'''

t=int(input("Enter t"))
p=0
arr=[]
i=0
j=i+1
flag=0
for p in range (t):
    n=int(input("Enter n"))
    k=int(input("Enter k"))
    arr=list(map(int,input().split()))
    for i in range (n):
        for j in range (i,n):
            if (arr[i]+arr[j]==k):
                flag=1
    if(flag==1):
      print("Yes")
    else:
        print("No")