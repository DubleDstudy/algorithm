import itertools

def dfs(i):
    global ans
    global sum
    for j in range(1,len(i)):
        sum+=abs(int(i[j])-int(i[j-1]))
        if ans<sum:
            ans=sum
    return sum


n=int(input())
A=[]
sum=0
ans=0
A=list(map(str,input().split()))

for i in list(itertools.permutations((A),n)):
    sum=dfs(i)
    sum = 0

print(ans)
