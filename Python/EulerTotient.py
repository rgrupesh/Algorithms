def euler_totient(num):
    arr=[]
    for count in range(num + 1):
        arr.append(count)
        
    for count in range(2, num + 1):
        if arr[count] == count:                    
            for j in range( count ,num + 1 ,count):
                arr[j] -= (arr[j] / count)  
                    
    return int(arr[num])  
    
    
print("Enter a number : ")
num = int(input())                       
if(num < 0):                   
    print("invalid input")
else:
    print(euler_totient(num))
    
'''sample input
if num = 4, the numbers less than 4 that are relatively prime to 4 are: 1,3. Hence, result=2.
Similary, if num = 6, the numbers less than 6 that are relatively prime to 6 are: 1,5. Hence, result=2.
 '''
