def Average(lst):
	try:
		if not lst:
			print("The list is empty")
			return None
		return sum(lst) / len(lst)
		# if str in lst:
		# 	print("Invalid elements in the list")
		# 	return None
	except TypeError:
		return None

# lst = [1, 2, 'l']
# print(Average(lst))