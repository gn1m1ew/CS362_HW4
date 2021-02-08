def Full_name(fname, lname):
	try:
		if (fname.isalpha() == True) and (lname.isalpha() == True) :
			# return None
			return fname + " " + lname
	except :
		return None


# fname_input = input("Enter the first name: ")
# lname_input = input("Enter the last name: ")

# full_name_result = Full_name(fname_input, lname_input)

# print("The full name is: ", full_name_result)