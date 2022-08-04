Given a string, str1=""”Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly braces or keywords), and a syntax which allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java.The language provides constructs intended to enable writing clear programs on both a small and large scale.Python features a dynamic type system and automatic memory management and supports multiple programming paradigms, including object-oriented, imperative, functional programming, and procedural styles. It has a large and comprehensive standard library.Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems. CPython, the reference implementation of Python, is open source softwareand has a community-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation."""
Hint: Assume that the first word is preceded by " "
a.	Build a dictionary where the key is a word and the value is the list of words that are likely to follow.
i.	E.g. Python  [is, has, features, interpreters, code, Software]. In this example the words listed are likely to follow “Python”
b.	Given a word predict the word that’s likely to follow.


str1="Python is a widely used high-level programming langauage for general-purpose prograaming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly braces or keywords), and a syntax which allows programmers to concpets in fewer lines of code than possible languages such as C++ or Java. The language provides constructs inteneded to enable writing clear programs on both a small scale and a large scale. Python featues a dynamic type system and sutomatic memory management and supports multiple programming paradgms,including object-oriented, imperative, functional programming, and procedural styles. It has a large and comprehensive standard library. Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems. CPython , the reference implementation of Python, is opne source software and has a community-based development model, as do nearly all of its variant implementations. CPython os managed by the non-profit Python Software Foundation."




def getDic(strn):
	dic={}
	wordList=strn.split()
	length=len(wordList)
	for index,word in enumerate(wordList):
		if dic.has_key(word):
			continue
		tmpList=[]
		for i in range(index,length):
			if index==length-1:
				break
			if word==wordList[i]:
				nextWord=wordList[i+1]
				tmpList.append(nextWord)

		dic[word]=tmpList
	return dic

def predict(strn,word):
	wordDictionary=getDic(strn)
	print "in the given string, the word ' ",word,"' is likely followed by the list of words",wordDictionary[word]


predict(str1,"Python")