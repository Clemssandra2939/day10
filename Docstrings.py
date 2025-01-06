# Docstrings
# Docstrings are basically a way for us to create little bits of documentation 
# as we are coding along in our functions or in our other blpcks of code 
# 
#  
# Storing output in a variable
formatted_name = format_name(input("Your first name: "),input("Your last name:" ))
print(formatted_name)
# or printing output directly
print(format_name(input("Your first name: "),input("Your last name:" )))

# Already used functions with output 
length = len(formatted_name)

# Return as an early exit

def format_name(f_name,l_name):
    """ Take a first and a last name and format it to 
    return the tittle case version of the name"""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    formated_f_name = (f_name.title())
    formated_l_name = (l_name.title())
    return f"Reult:{formated_f_name} {formated_l_name}"

format_name()

# unlike the normal string you can't continue it in another line but 
# docstring made that possible to do so

# Docstrings = """ """(it comes with 3 each quotation commas from the first to the end)