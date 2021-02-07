def Average(lst):
	try:
		if str in lst:
			print("Invalid elements in the list")
			return None
		if not list:
			print("No list exists")
			return None
	except:
		return sum(lst) / len(lst)

# lst = [1, 2, 'l']
# print(Average(lst))