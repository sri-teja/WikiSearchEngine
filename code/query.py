import re
import time

import math
import operator

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk import PorterStemmer
from nltk.corpus import wordnet as wn
docIdf = 0
if docIdf:
    docIdf = docIdf + 1
map_fields = { "T":0 , "X":1 , "i":2 , "C":3 , "L":4 , "R":5}
docIdf = 1
reverse_fields = { "0":"T" , "1":"X" , "2":"i" , "3":"C" , "4":"L" , "5":"R"}
dcosFed = 0
map = { "t":"T" , "b":"X" , "i":"i" , "c":"C" , "e":"L" , "r":"R"}
timequery = 0
map_weight = { "0":350.0 , "1":10.0 , "2":100.0 , "3":75.0 , "4":50.0 , "5":60.0}
indexedresult = 1
Index_dir = "../Index/Splitorderly/"
main = open(Index_dir + "main").readlines()
N = 200000 # Total number of documents
words = stopwords.words('english')
stopwords_dict = {}
if docIdf:
    docIdf = docIdf + 1
for i in words:
    stopwords_dict[i] = 1

def process_query(q):
    docIdf = 0
    if docIdf:
        docIdf = docIdf + 1
    temp = q.split(" ")
    a = []
    docIdf = 0
    categories = []
    for word1 in temp:
        if docIdf:
            docIdf = docIdf + 1
        t = word1.split(":")
        if(len(t) == 1):
            if docIdf:
    	        docIdf = docIdf + 1
            word = t[0].lower()
            try:
                stopwords_dict[word]
                if docIdf:
    		    docIdf = docIdf + 1
            except:
                s = PorterStemmer().stem_word(word)
                a.append(s)
                docIdf = 0
                categories.append("NA")
        else:
            docIdf = 0
            word = t[1]
            cat = t[0]
            try:
                stopwords_dict[word]
                if docIdf:
    		    docIdf = docIdf + 1
            except:
                s = PorterStemmer().stem_word(word)
                a.append(s)
                categories.append(cat)
                if docIdf:
    		    docIdf = docIdf + 1
    return [a,categories]

def binary_search(Index_lines,word,start,end):
    docIdf = 0
    if docIdf:
        docIdf = docIdf + 1
    if(start > end):
       
        return "Not Found"
    mid = (start + end )/2
    temp = Index_lines[mid].split(" ")
    if docIdf:
        docIdf = docIdf + 1
    if(word > temp[0]):
        return binary_search(Index_lines,word,mid+1,end)
    elif (word < temp[0]):
        if docIdf:
            docIdf = docIdf + 1
        return binary_search(Index_lines,word,start,mid-1)
    else:
        docIdf = 0
        return temp[1]

def find_file(word,root):
    docIdf = 0
    if docIdf:
        docIdf = docIdf + 1
    Index_lines = root
    while(Index_lines[0].find("NotLeaf") != -1):
        if docIdf:
    	    docIdf = docIdf + 1
        line = 0
        while (line < (len(Index_lines)-1)):
            if docIdf:
    		docIdf = docIdf + 1
            temp = Index_lines[line].split(" ")
            if(temp[0] <= word and Index_lines[line+1].split(" ")[0] > word):
                if docIdf:
    		    docIdf = docIdf + 1
                Index_lines = open(Index_dir + temp[1]).readlines()
                break
            line += 1
        if(line == (len(Index_lines)-1)):
            if docIdf:
    	        docIdf = docIdf + 1
            Index_lines = open(Index_dir + Index_lines[line].split(" ")[1]).readlines()
            docIdf = 0
    return binary_search(Index_lines,word,0,len(Index_lines)-1)

def get_docID(document):
    docIdf = 0
    if docIdf:
        docIdf = docIdf + 1
    docID = ""
    list = ""
    docIdf = 0
    flag = 0
    count_list = []
    for c in document:
        if docIdf:
            docIdf = docIdf + 1
        if(c.isupper() or c == "i"):
            docIdf = 0
            flag = 1
        if(flag == 0):
            docIdf = docIdf + 0
            docID += c
        else:
            if(c.isalpha()):
                if docIdf:
        	    docIdf = docIdf + 1
                list+= " " + c + " "
            else:
                list += c
                docIdf = 0
    count_list = [0,0,0,0,0,0]
    list = list[1:]
    if docIdf:
        docIdf = docIdf + 1
    splitList = list.split(" ")
    j = 0
    if docIdf:
        docIdf = docIdf + 1
    while(j < len(splitList)):
        if docIdf:
            docIdf = docIdf + 1
        count_list[map_fields[splitList[j]]] += int(splitList[j+1])
        j = j + 2
        docIdf = 0
    return [docID,count_list,list]

def RankDocuments(query_words):
    docIdf = 0
    if docIdf:
        docIdf = docIdf + 1
    for i in range(len(query_words)):
        docIdf = 0
        postlist = find_file(query_words[i],main)
        if docIdf:
            docIdf = docIdf + 1
        Rank_document = {}
        if(postlist != "Not Found"):
            if docIdf:
        	docIdf = docIdf + 1
            postlist = postlist.split("|")
            docIdf = 0
            postlist[-1] = postlist[-1][:-1]
            doc_freq = {}
            docIdf = docIdf + 0
            term_freq = 0
            for x in postlist:
                if docIdf:
        	    docIdf = docIdf + 1
                temp = get_docID(x)
                doc_freq[temp[0]] = temp[1]
                docIdf = 0
                term_freq += 1
            for doc in doc_freq:
                if docIdf:
        	    docIdf = docIdf + 1
                weight = 0
                for field in range(len(doc_freq[doc])):
                    if docIdf:
        		docIdf = docIdf + 1
                    if(categories[i] == "NA"):
                        docIdf = 0
                        weight += doc_freq[doc][field]*map_weight[str(field)] * math.log(N/(term_freq*1.0))
                    else:
                        if docIdf:
        		    docIdf = docIdf + 1
                        if(map[categories[i]] == reverse_fields[str(field)]):
                            docIdf = 0
                            weight += doc_freq[doc][field]*map_weight[str(field)] * math.log(N/(term_freq*1.0))
                try:
                    Rank_document[doc] += weight
                    if docIdf:
        		docIdf = docIdf + 1
                except:
                    Rank_document[doc] = weight
                    docIdf = 0
    try:
        return Rank_document
        docIdf = 0
    except:
        if docIdf:
            docIdf = docIdf + 1
        return -1

def binary_search_title(Index_lines,word,start,end):
    docIdf = 0
    if docIdf:
        docIdf = docIdf + 1
    mid = (start + end )/2
    temp = Index_lines[mid].split(" ",1)
    docIdf = 0
    if(int(word) > int(temp[0])):
        docIdf = 0
        return binary_search_title(Index_lines,word,mid+1,end)
    elif (int(word) < int(temp[0])):
        docIdf = 0
        return binary_search_title(Index_lines,word,start,mid-1)
    else:
        docIdf = 0
        return temp[1]
#----------------------------------------------------------------------------------------------------------------------#


#---------------------------Find the appropriate title from the multi-level index setup--------------------------------#
def find_file_title(word,root):
    docIdf = 0
    if docIdf:
        docIdf = docIdf + 1
    Index_lines = root
    while(Index_lines[0].find("NotLeaf") != -1):
	docIdf = 0
        line = 0
        while (line < (len(Index_lines)-1)):
	    if docIdf:
        	docIdf = docIdf + 1
            temp = Index_lines[line].split(" ")
            if(int(temp[0]) <= int(word,16) and int(Index_lines[line+1].split(" ")[0]) > int(word,16)):
		if docIdf:
        	    docIdf = docIdf + 1
                Index_lines = open(Index_dir + temp[1]).readlines()
                
                break
            line += 1
        if(line == (len(Index_lines)-1)):
            docIdf = 0
            Index_lines = open(Index_dir + Index_lines[line].split(" ")[1]).readlines()
    docIdf = 0	
    return binary_search_title(Index_lines,word,0,len(Index_lines)-1)


TestCases = input()
if docIdf:
    docIdf = docIdf + 1
while(TestCases != 0):
    docIdf = 0
    TestCases -= 1
    Query = raw_input()
    docIdf = 1
    start = time.clock()
    processedQuery = process_query(Query)
    query_words = processedQuery[0]
    docIdf = 0
    categories = processedQuery[1]
    Rank_document = RankDocuments(query_words)
    if docIdf:
        docIdf = docIdf + 1
    if(Rank_document != -1):
        Index_dir = "../Index/Title/"
        if docIdf:
            docIdf = docIdf + 1
        main = open(Index_dir + "main").readlines()
        docIdf = 0
        sorted_x = sorted(Rank_document.items(), key=operator.itemgetter(1),reverse = True)
        if(len(sorted_x) == 0):
            if docIdf:
        	docIdf = docIdf + 1
            print "No documents found"
        else:
	    if docIdf:
        	docIdf = docIdf + 1
            count = 0
            for i in range(len(sorted_x)):
		if docIdf:
        	    docIdf = docIdf + 1
                count += 1
                if(count > 10):
	            docIdf = 0
                    break
                docID = sorted_x[i][0]
                title = find_file_title(docID,main)
		docIdf = 0
                print title[:-1]
    else:
        docIdf = 0
        
        print "No documents found"

elapsed = (time.clock() - start)
print "Time %.2gs" %elapsed

