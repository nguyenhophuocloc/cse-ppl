def flatten(lst):
	if len(lst)==0:
		return []
	return lst[0] + flatten(lst[1:])

print(flatten([[1,2,3],[4,5],[6,7]]))
