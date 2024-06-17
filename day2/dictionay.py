# my_dict = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }
# (1,2,3)
# # [1]
# my_dict_second = {
#     "name1": "John",
#     "age1": 30,
#     "city1": "New York"
# }

# new_dict={**my_dict,**my_dict_second}
# print(new_dict)
# new_dict.pop('"name1"')
# # del new_dict['name1']


# set

# list, dict, tuple
# set-> unique el


set1={'val', True, True,'val', False, 0 }
set2={'val', True, True,'val', False, 0 }
print(set1)
set1.add('newvalue')
set1.remove('newvalue')
set1.intersection(set2)
# truthy and faslsy value
# 0, None, False,...


# set, list 
# list vs tuple, dict
# why tuple preffered over list
# dict, 
# extend vs append 
# mutable vs immutable
# if {}

new_list=[1,1,2,2,33]
new_list1=[]



# for i in new_list:
#     if i in new_list1:
#         pass
#     else:
#         new_list1.append(i)

# print('unique elemnt', new_list1)
    


for i in new_list:
    if i not in new_list1:
        new_list1.append(i)
        

print('unique elemnt', new_list1)

# unique= set(new_list)
# print(unique)

# a=2
# float(a)
# print unique element only

# in operator->membership test 
# print(33 in new_list)
# print(4 in new_list)

# if "condition":
#     pass
# elif "condition":
#     pass
# else:
#     pass
