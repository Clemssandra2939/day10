# Docstrings
# Docstrings are basically a way for us to create little bits of documentation 
# as we are coding along in our functions or in our other blpcks of code  

# Already used functions with output 
length = len(formatted_name)

# Return as an early exit

def format_name(f_name,l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    formated_f_name = (f_name.title())
    formated_l_name = (l_name.title())
    return f"Reult:{formated_f_name} {formated_l_name}"
