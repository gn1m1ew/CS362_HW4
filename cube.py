def Cube(num):
	try:
		return num ** 3
	except TypeError:
		return None

# number = 3
# cube_result = Cube(number)

# print("The volume of the cube is: ", cube_result)