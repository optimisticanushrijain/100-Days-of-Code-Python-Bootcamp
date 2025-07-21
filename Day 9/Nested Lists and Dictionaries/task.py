#nested list in dictionary [lists inside dictionary]:
travel_log={
    "France": ["Paris", "Lillie", "Dijon"],
    "Germany": ["Berlin", "Stutport"],
}
list=["Paris", "Lillie", "Dijon"]
# try - print(list[1])

#Accessing item - Lillie from this nested list in dictionary
print(travel_log["France"])

#Accessing item from the nested list only - lists inside lists
nested_list=["A", "B", ["C","D"]]
#print(nested_list[2][1])

#dictionary inside dictionary and lists inside dictionary
#Accessing item- "Stuggart from the nested dictionary and nested list
travel_log ={
    "France": {
        "total_vists": 12,
        "city_visited":["Paris", "Lillie", "Dijon"]
    },
    "Germany":{
        "total_vists": 6,
        "city_visited":["Berlin", "Hamburg", "Stuggart"],
        "fv":["Paris"]
    },
}

#print(travel_log)
print(travel_log["Germany"])

starting_dictionary = {
    "a": 9,
    "b": 8,
}




