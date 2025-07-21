# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "invalid input"
#     first_name =f_name.title()
#     last_name = l_name.title()
#     return f" Result: {first_name} {last_name}"
#
# formatted_string = format_name(input("What is your first name: ?"), input("What is your last name: ?"))
# print(formatted_string)

def format_name(f_n, l_n):
    f_name = f_n.title()
    l_name = l_n.title()
    return f"{f_name} {l_name}"
output = format_name("aNUsHRi", "jAIn")
print(output)