# Functions with outputs  

def format_name(f_name,l_name):
    print(f_name.title())
    print(l_name.title())
format_name("Sandra","CLEMS") #Sandra 
# Clems

# Output with variable
def format_name(f_name,l_name):
    formated_f_name = (f_name.title())
    formated_l_name = (l_name.title())

    print(f"){formated_f_name}  {formated_l_name}")
format_name("SanDRA","CLEMS")#Sandra  Clems

# How to use result function instead of print statement 
def format_name(f_name,l_name):
    formated_f_name = (f_name.title())
    formated_l_name = (l_name.title())
    return (f"{formated_f_name} {formated_l_name}")

print(format_name("SanDRA","CLEMS"))
