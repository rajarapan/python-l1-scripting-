Given a list of strings, return the count of the number of strings where the string length is 2 or more and the first and last chars of the string are the same.  

list1=['axa', 'xyz', 'gg', 'x', 'yyy']
list2=['x', 'cd', 'cnc', 'kk']
list3=['bab', 'ce', 'cba', 'syanora']
def specialStringCount(tlist):
	sCount=0
	for ele in tlist:
		if ( len(ele)>=2 ) and ( ele[0] == ele[-1] ):
			sCount+=1
	return sCount

print specialStringCount(list1)
print specialStringCount(list2)
print specialStringCount(list3)