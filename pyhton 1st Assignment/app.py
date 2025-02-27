# hello world in python
print("hello world")

# string
name = "ahmer"
print(f'welcome {name} to the python world')

# interger 
Age = 18
print(f" age :{Age}")
# float 
weight = 49.00 
print(f'weight : {weight}')


# Boolean value indicating programmer status
is_programmer = True  
print("programmer:", is_programmer)


# making a age function and using if-else condition in this 
def CheckAge(age):
    if age >=18:
        return 'you are eligible for IDcard'
    else:
        return 'you are not eligible for IDcard'
    
print(CheckAge(19))



# dictionary example
personal_details_ = {
    "name": "Ahmer abbasi",
    "age": 19,
    "ID_number": 4743790,
    "profession" : "Web developer"
}
print(personal_details_)

# list example
friends_list = ["umer", "ali" , "usman" , "asif"]
print(f' friends_list :  {friends_list}')
# using loop
for friend_loops in friends_list:
    print(f'{friend_loops} is my best friend')


# tuple example 
fav_dishes =("biryani","korma" ,"karhae","niahri","pulao")
print(f"fav_dishes : {fav_dishes}")

