# Tuples Exercise
month = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
m = input("Input your birthday in format DD-MM-YYYY: ")
index = int(m[3:5]) - 1
bd_month = month[index]
print("You were born in", bd_month)

# List Exercise
waiting_list = ["John", "Mary", "Moon"]
name = input("Please input your name to join the waiting list: ")
waiting_list.append(name)
print("Updated waiting list:", waiting_list)