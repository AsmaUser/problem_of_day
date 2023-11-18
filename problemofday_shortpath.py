list1 = [7, 8, 3, 1, 6, 22, 10, 25, 9, 15, 1]
list2 = [2, 11, 0, 6, 3, 20, 7, 25, 6, 7]

path_1 = sum(list1)
path_2 = sum(list2)


if path_1 < path_2:
    shortes_path= list1
    Total=path_1
    #print(f"list1 is the shortest path: {list1}")
    #print("Total =", path_1) 
else:
    shortes_path= list2
    Total=path_2
    #print(f"list2 is the shortest path: {list2}")
    #print("Total =", path_2)
print("The shortest path is:", shortes_path)
print("Total= ", Total)
