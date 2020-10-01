try:  #try catch so that the program does not crash
	arr=[]

	def search(arr, x): 
	  
	    for i in range(len(arr)): 
	  
	        if arr[i] == x: 
	            return i 
	  
	    return -1
		
	  
	    
	while True:
		op = int(input("Press--> 1 to insert integer | 2 to  search element | 3 to exit "))
		if op==1:                                       #to insert an elelment in the queue
			ele = int(input("enter elem to insert "))
			arr.append(ele)
		elif op==2:                                    #to remove an element from the queue
			x=int(input("Enter element to search "))
			a=search(arr,x)
			if a==-1:
				print("Element" ,x," is not present in the list")
			else:
				print("Element " ,x, "is at position ",a)
		else:
			print("invalid option")


except ValueError:
	print("Please enter integer only")                 #If user inputs an alphabet or string the program should not crash
except:
	print("There's been some issue please check the data you've entered")

