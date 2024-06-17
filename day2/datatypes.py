# data types in python



# # premitive and non premitive
# # primitive-> fundamental -> int, foat, char, imgarny
# # non premitive-> list,dict, set, tuple...

# a=45
# print(a, type(a))
# b= 4.5
# print(b, type(b))
# img=2+3j
# print(img, type(img))


# # list


# # -> array-> similar
# # int num[]={1,2,3,4,5}

# li=['name', 3, []]

# # indexing, -ve indexing

# # accessing element
# # wap to accesss last element of list of any size
# # listname=[]
# # print(listname[0])
# num=li[1]
# print(num)

# nested_list=[0,[3,2],'last']
# print(nested_list[1][0])
# print last element of nested list

# slicing
# ":"
# new_list=[12,34,54,12,34,8]
# 
# number_list=[1,2,3,4,5,6,7,8,9,10]
# print all even number form number_list in descending way
# print('"even',number_list[1::2] )
# print("even in descending",number_list[::-2])

# first_three=new_list[:3]
# print("first_three_el", first_three)
# print("last three",new_list[3:])
# print(new_list[::])

# print("new list is:", first_three)
# [starting:endpoint:step]
# by default step is 1
# print('step after 1:', new_list[-1:-6:-2])
# wap to reverse the list using slicing
# -ve 
# step -ve


# method in list
# method -> function
# append

new_list=[12,34,54,12,34,8,[3,4,5]]
new_list=[12,34,54,12,34,8,3,4,5]
# new_list.append(35)
# new_list.append([1,2])
print(new_list)
# insert metthod
new_list.insert(2,'new insert')
new_list.remove(1)
new_list.clear()
to_add=[3,4,5]
# new=new_list.extend(to_add)
print(new_list)
# append inc by1
# exten len list
print(len(new))