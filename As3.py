	Given a list of strings, return a list with the strings in sorted order, except group all the strings that begin with 'x' first. e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
['xanadu', 'xyz', 'aardvark', 'apple', 'mix']. 
Hint: this can be done by making 2 lists and sorting each of thembefore combining them.
i.	['bbb', 'ccc', 'axx', 'xzz', 'xaa']
ii.	['mix', 'xyz', 'apple', 'xanadu', 'aardvark']

def customSort(lst):
	tmpList=lst
	Xlst=[];nonXlst=[]
	for ele in tmpList:
		if ele[0].lower() == "x" :
			Xlst.append(ele)
		else:
			nonXlst.append(ele)
	Xlst.sort(),nonXlst.sort()
	return Xlst + nonXlst


lst1=['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
lst2=['bbb', 'ccc', 'axx', 'xzz', 'xaa']

print lst1," is sorted as \n",customSort(lst1),"\n\n"
print lst2," is sorted as \n",customSort(lst2),"\n\n"