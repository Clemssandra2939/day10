# def format_name(f_name,l_name):
#     formated_f_name = (f_name.title())
#     formated_l_name = (l_name.title())
#     return (f"{formated_f_name} {formated_l_name}")

# print(format_name("SanDRA","CLEMS"))

# when the return keyword is excuted,it is like the defult way of saying that that line is the end of the function
def format_name(f_name,l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    formated_f_name = (f_name.title())
    formated_l_name = (l_name.title())
    return (f"{formated_f_name} {formated_l_name}")

print(format_name(input(" What is yor first name?"),
 input ("What is your last name?")))