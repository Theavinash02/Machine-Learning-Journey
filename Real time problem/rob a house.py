lis = [1,2,3,4,1]
hou1=[]
hou2=[]
rob1,rob2 = 0,0
i,j =0,1
while i < len(lis):
    rob1 = lis[i] + rob1
    hou1.append(lis[i])
    i +=2
while j < len(lis):
    rob2 = lis[j] + rob2
    hou2.append(lis[j])
    j +=2
    
if (rob1>rob2):
    print("The best house to rob is : " + str(hou1)[1:-1] + " and the loot is" , rob1 )
    
else:
    print("The best house to rob is : " + str(hou2)[1:-1] + " and the loot is " , rob2)
