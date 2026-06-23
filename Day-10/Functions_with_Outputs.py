#function with input 
def format_name(f_name, l_name):
    full_name = f"{f_name} {l_name} ".title()
    return full_name

    
    


formated_name = format_name(f_name= input("What is your name?\n"), l_name= input("What is last name?\n"))
length = len(formated_name)
# formated_name = (format_name("sumit", "SHEORAN"))
print(formated_name)




#mutiple return values

# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return ("You did not provide valid inputs")
#     else:
#         full_name = f"{f_name} {l_name} ".title()
#         return full_name

    
    


# formatted_name = format_name(f_name= input("What is your name?\n"), l_name= input("What is last name?\n"))
# # formated_name = (format_name("sumit", "SHEORAN"))
# print(formatted_name)
# length = len(formatted_name)


