Given a list of non-empty tuples, return a list sorted in increasing order by the last element in each tuple. 
e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields[(2, 2), (1, 3), (3, 4, 5), (1, 7)]
 Hint: use a custom key= function to extract the last element form each tuple.
i.	[(1, 3), (3, 2), (2, 1)]
ii.	[(1, 7), (1, 3), (3, 4, 5), (2, 2)]

def getLastEle(tup):
	return tup[-1]

def customSort(lst):
	tmplst=lst
	tmplst.sort(key=getLastEle)
	return tmplst



lst1=[(1, 3), (3, 2), (2, 1)]
lst2=[(1, 7), (1, 3), (3, 4, 5), (2, 2)]

print lst1,"\n is sorted as \n",customSort(lst1)

print "\n\n"

print lst2,"\n is sorted as \n",customSort(lst2)
