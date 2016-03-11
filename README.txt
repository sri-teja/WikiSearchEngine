
1- Installation Requirements:

 	Compiler/Interpreter/Librarie(s):      Python,NLTK,NLTK stopwords corpus

2- About the Files:

Contains -  myindex.py 

myindex.py : It parses the entire XML file , stores it in a dictionary and then writes it onto an outputfile

Format of the Datastructure Used:
store[word][pageID] = [Title_count , Bodytext_count , Infobox_count , Categories_count , Externallinks_count , References_count ]
	
1.) The code reads the sample XML file line by line. The pagecontentHandler takes appropriate actions when it encounters a start tag, end tag or content in between.
2.) Content between Infobox,References,External links,Titles and Categories are isolated appropriately and stored seperately
3.) The Regex "[a-zA-Z0-9]+" is used to tokenize the content. The Regex removes all special characters and punctuations.
4.) The tokens obtained via the above regular expression are further filtered using the nltk stopwords corpus. This corpus of very frequently occuring english words which are of not much significance. All these words are stored as keys in a dictionary which is then used to check if a particular token is a stop word or not. 
5.) Then the root form of the word is obtained by using the NLTK porter stemmer which is then saved in the final dic ( Structure of the dictionary is mentioned above).
6) The code runs the given file (evaluate.xml) file in about 3 min 55 sec.
7) The pageID is first mapped to an integer "page_number" which starts from 1 and then converted to hexadecimal to conserve space.

3-Indexedfile format : 

Word pageIDT(count)X(count)i(count)C(count)L(count)R(count)...
T -> Title
X -> Body Text
i -> Infobox
C -> Categories
L -> External Links
R -> References


4- Query :
i) Comprises of MultiIndexBody.py,MultiIndexTitle.py,Query.py
ii) The MultiIndexBody.py creates a multi-level index for the index obtained on 43GB wiki corpus. We split the entire sorted Index into files of 500 lines of each , create index for these files and keep doing it until the number of index files obatined are less than 200. We then create a "main" index file for the top most index files. This could be visualized as a tree structure where the leaf nodes are the actual files of index and the rest of the nodes are index files on the files below them. The MultiIndexTitle.py does the same thing on the DocID - Title map file.
iii) The Query.py searches for the query words in the Index file , retieves the post list and calcualates the relevance of every document-word pair using T.F * I.D.F weight. It then prints the titles of the top 10 relevant documents.
iv) The Index folder contains the output index files, the folder ./Index/Splitorderly contains the Index broken into files of 500 lines each with index built on them. The folder ./Index/Title contains the title with docID mapped file broken into files of 500 lines each with index built on them.



	
