Given a string, str1=""”Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly braces or keywords), and a syntax which allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java.The language provides constructs intended to enable writing clear programs on both a small and large scale.Python features a dynamic type system and automatic memory management and supports multiple programming paradigms, including object-oriented, imperative, functional programming, and procedural styles. It has a large and comprehensive standard library.Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems. CPython, the reference implementation of Python, is open source softwareand has a community-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation."""
a.	Build a dictionary, with "words as key" --> Frequency of occurrence as value
E.g. Python 7, is3
b.	Print the top 5 words with their frequency of occurrence


str1="""Python is a widely used high-level programming langauage for general-purpose prograaming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly braces or keywords), and a syntax which allows programmers to concpets in fewer lines of code than possible languages such as C++ or Java. The language provides constructs inteneded to enable writing clear programs on both a small scale and a large scale. Python featues a dynamic type system and sutomatic memory management and supports multiple programming paradgms,including object-oriented, imperative, functional programming, and procedural styles. It has a large and comprehensive standard library. Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems. CPython , the reference implementation of Python, is opne source software and has a community-based development model, as do nearly all of its variant implementations. CPython os managed by the non-profit Python Software Foundation."""


wordCountTable={}
wordList=str1.split()
for word in wordList:
	wordCountTable[word]=str1.count(word)


values=wordCountTable.values()
values.sort()
values.reverse()
topFive=values[0:5]
printCount=0


print "\n\nTop Five words in the given string with their occurrences"
print "\n\n---------------------------"
print "word\t\tcount"
print "---------------------------"
for v in topFive:
	for word in  wordCountTable:
		if wordCountTable[word] == v:
			print word,"\t\t",wordCountTable[word]
			printCount+=1
			if printCount==5:
				break
	if printCount==5:
		break


print "\n\n\n"			