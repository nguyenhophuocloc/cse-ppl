def lessThan(lst,n):
	return list(filter(lambda x: x<n,lst))

print(lessThan([1,2,3,4,5],4))