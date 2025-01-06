# Days in month
# Instructions

# In the starting code,you will find the solution from the leap year
# challenge.first convert the function is_leap() so that instead of printing 
# printing "leap year" or "Not leap year",it should return True if it is a leap year 
# and return False if it is not a leap year
# You are going to create a function called days_in_month() which will take a year and a month as inputs EncodingWarning
# E.g day_in_month(year=2022,month= 2)

# And it will use this infomation to work out the number of days in the onth,then return that as the output 














# leap year coding char.
# how to know whether any year is a leap year
# on every year that is evenly divisible by 4
# except every year that is evenly divisible by 100
# unless the year is also evenly divisible by 400

# year=int(input("which year do u want to check?"))
# if year % 4:
#     print(f"{year} is a leap year")
# elif year % 100:
#     print(f"{year} is a not leap year")
   
# elif year % 400:
#     print(f"{year} is a leap year")

# else:
#     print(f"{year} is a not leap year")

# else:                                  
   #  print("f{year} is not a leap year")


# year=int(input("which year do u want to check? "))
# if year % 4==0:
#     if year % 100==0:

#         if year % 400==0:
#             print(f"{year} is leap year")
#         else: 
#             print(f"{year} is not leap year")
#     else:
#         print(f"{year} is leap year")

# else:
#     print(f"{year} is not leap year")



# Nesting Lists and Dictionaries

# {
#     key:[list],
#     key2:{Dict},
# }

# Using a list and a dictionary as a value nested on another dictionary{}

# Nesting
capitals ={
 "France":"Paris",
 "Germany":"Berlin",
}

# Nesting a list in a Dictionary
travel_log ={
    "France":["Paris","Lille","Dijon"], #here list is used to mention different state in france because a key should hae one value
    "Germany":["Berlin","Hamburg","stuttgart"],
}

# Nesting Dictionary in a Dictionary and make more easy to understand 

travel_log ={
    "France":{"cities_visited": ["Paris","Lille","Dijon"],"total_visited": 12}, #
    "Germany":{"cities_visited":["Berlin","Hamburg","stuttgart"],"total_visited": 5},
}

# Adding muitiple dictionaries in a list 
 
travel_log = [
    {
        "country" :"France",
        "cities_visited" : ["Paris","Lille","Dijon"],
        "total_visited": 12
    }, 
    {
        "country" :"Germany",
        "cities_visited" :["Berlin","Hamburg","stuttgart"],
        "total_visited": 5
    },
]
 