import random
#Nesting dictionary inside a dictionary
#Nesting list inside a list
#Nesting a list inside a dictionary
#Nesting a dictionary inside a list


#Nesting a list inside a dictionary
my_dict = { "France": ["Berlin", "Germany", "Francis"],
            "time": 56,
            "age": [25, 28, 55]
}

# 1) accessing only values using key
# print(my_dict["France"]) # if key doesn't exist > KeyError
# print(my_dict.get("Fran")) # print None- as the program won't crash
# print(my_dict["age"])

# 2) accessing all the values
# for items in my_dict:
#     print(my_dict[items])

# 3) Get the First Key in Dictionary
# (a) convert the all keys in the dictionary into a list using list():
# res = list(my_dict)[1]
# print(res)
# # (b) using for loop
# for k in my_dict:
#     res = k
#     break
# print(res)

# Accessing all keys
# for i in my_dict:
#     print(i)


# 4) printing whole dict including keys and values
# print(my_dict)

# 5) accessing first key-value pair from the dict

# (c1, c2)= list(my_dict.items())[1]
# print(c1,c2)

#Nesting a dictionary inside a list
my_list = [{ 'name': 'Instagram',
            'follower_count': 346,
},
{
'name': 'Facebook',
'follower_count': 2000,
},
{
'name': 'Twitter',
'follower_count': 300,
},]

#Accessing whole list:
#print(my_list)

#Accessing value from this list
#print(my_list[0]["name"])

#all values



#Accessing key from this list

#Accessing one key-value dictionary pair
print(my_list[0])
print(my_list[2])

#Accessing randomly one key-value dictionary pair
# listIndex = random.randrange(len(my_list))
# print(my_list[listIndex]["name"])
# print(my_list[listIndex]["follower_count"])
#
# #return any random element or any one key-value pair from the dictionary inside a list
ranA=random.choice(my_list) #{'name': 'Twitter', 'follower_count': 300}
# print(ranA)
#
# #accessing values
# print(ranA["name"])
# print(ranA["follower_count"])
# #accessing keys
print(list(ranA)[1])