Write a function to print the information in the dictionary(bookstore) in the given format

bookstore={"New Arrivals":{"COOKING":["Everyday Italian","Giada De Laurentiis","2005","30.00"],"CHILDREN":["Harry Potter”, J K. Rowling","2005","29.99"],"WEB":["Learning XML","Erik T. Ray","2003","39.95"]}}
BOOKSTORE
'Learning XML', 'Erik T. Ray', '2003', '39.95' 
'Everyday Italian', 'Giada De Laurent is', '2005', '30.00']
'Harry Potter', 'J K. Rowling', '2005', '29.99']

bookstore = {"New Arrivals":{"COOKING":["Everyday Italian","Giada De Laurentiis","2005","30.00"],"CHILDREN":["Harry Potter","J K.Rowling","2005","29.99"],"WEB":["Learning XML","Erik T. Ray","2003","39.95"]}}
print "\n\nBOOKSTORE\n\n"
for dic1 in bookstore.values():
	for lst in dic1.values():
		strn=str(lst)
		strn=strn[1:len(strn)-1]		
		print strn

print "\n\n"