my_list = [-15, -26, 15, 1, 23, -64, 23, 76]
new_list = []

while my_list:
    min = my_list[0]  
    for x in my_list: 
        if x < min:
            min = x
    new_list.append(min)
    my_list.remove(min)    

print(new_list)

#note : sorting arry , list in python also can be done by sort() function a once