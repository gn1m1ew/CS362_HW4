def Full_name(fname, lname):
	try:
		return fname + " " + lname
	except TypeError:
		return None


# fname_input = input("Enter the first name: ")
# lname_input = input("Enter the last name: ")

# full_name_result = Full_name(fname_input, lname_input)

# print("The full name is: ", full_name_result)