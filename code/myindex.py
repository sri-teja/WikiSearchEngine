import xml.sax
import sys
import nltk
from nltk.corpus import stopwords
import re
from nltk import PorterStemmer
import timeit
import sys 
output = open(sys.argv[2],"w")
file_counter = 0
file_name = "./Index/body/ans.txt"
output1 = open("./Index/title/MyTitle.txt","w")
abc =0
class pagecontentHandler(xml.sax.ContentHandler):
    def __init__(self):
        docIdf=0
	self.pageID = ""    
        self.title = []	
        self.infobox = []
        if docIdf:
            docIdf= docIdf + 1 
        self.externallinks = []
        self.references = [] 
        self.categories = [] 
        if docIdf:
            docIdf= docIdf + 5
        self.page_content = [] 
	self.stopwords = {}
	words = stopwords.words('english')  
        for i in words:
            self.stopwords[i] = 1
        self.page_enter = 0
        self.page_title = {}
        self.regex = re.compile(r'\d+\.?\d+|[a-zA-Z0-9]+')
        if docIdf:
            docIdf= docIdf + 1
        self.page_map={} 
        self.page_number = 0 
        self.tag = ""
        self.store = {}
        self.Infobox_tag = 0   
        self.Reference_tag = 0 
	if docIdf:
            docIdf= docIdf + 1
        self.External_tag = 0 
    def createPostList(self,content,index):
        if docIdf:
            docIdf= docIdf + 1
        r = self.regex
        min_len = 0
        for i in content:
            if docIdf:
                docIdf= docIdf + 1
            temp = r.findall(i)
            filtered_words = []
             if docIdf:
                docIdf= docIdf + 1
            for w in temp:
                s = w
                try:
                    self.stopwords[s]
		    if docIdf:
                        docIdf= docIdf + 1
                except:
                    filtered_words.append(s)
            for word in filtered_words:
                s = PorterStemmer().stem_word(word) # This gives the root word form of the words
                try:
                    self.store[s][self.pageID]
                    if docIdf:
                        docIdf= docIdf + 1
                    self.store[s][self.pageID][index] += 1
                except:
                    try:
                        if docIdf:
                	    docIdf= docIdf + 1
                        self.store[s]
                        self.store[s][self.pageID]=[0,0,0,0,0,0]
                        if docIdf:
                            docIdf= docIdf + 1
                        self.store[s][self.pageID][index] = 1
                    except:
                        self.store[s] = {}
                        if docIdf:
                            docIdf= docIdf + 1
                        self.store[s][self.pageID]=[0,0,0,0,0,0]
                        self.store[s][self.pageID][index] = 1
                        if docIdf:
                	    docIdf= docIdf + 1
    def get_val(self,field,count):
        if(int(count) == 0):
            return ""
        else:
            return field + str(count)

    def startElement(self, name, attrs):
        self.tag = name
	self.Infobox_tag = 0
        self.Reference_tag = 0
        self.External_tag = 0
        if(name == "page"):
            self.title = []
            docIdf = 0
            self.infobox = []
            self.externallinks = []
            if docIdf:
                docIdf= docIdf + 1
            self.categories = []
            self.page_content = []
            self.references = []
        if(name == "title"):
            self.page_enter= 1
    def file_write(self):
        if docIdf:
            docIdf= docIdf + 1
        global file_counter
        file_counter += 1
        f = file_name+str(file_counter)+".txt"
        if docIdf:
            docIdf= docIdf + 5
        output = open(f,"w")
        s = ""
        if docIdf:
            docIdf= docIdf + 1
        for word in sorted(self.store):
            s = word + " "
            if docIdf:
            docIdf= docIdf + 5
            for docID in self.store[word]:
                s += str(format(int(self.page_map[docID]),'02x'))
                docIdf= docIdf + 1
                s += self.get_val("T",self.store[word][docID][0])
                docIdf=0
                s += self.get_val("X",self.store[word][docID][1])
                docIdf=0
                s += self.get_val("i",self.store[word][docID][2])
		docIdf = docIdf + 1                
		s += self.get_val("C",self.store[word][docID][3])
                docIdf=0
                s += self.get_val("L",self.store[word][docID][4])
		docIdf = 0                
		s += self.get_val("R",self.store[word][docID][5])
                s += "|"
            s = s[:-1]
            if docIdf:
                docIdf= docIdf + 1
            output.write(s+"\n")
        output.close()

    def endElement(self, name):
        if docIdf:
            docIdf= docIdf + 1
        self.tag = ""
        if(name == "page"):
            self.createPostList(self.title,0)
            if docIdf:
                docIdf= docIdf + 1
            self.createPostList(self.page_content,1)
            self.createPostList(self.infobox,2)
            if docIdf:
                docIdf= docIdf -1
            self.createPostList(self.categories,3)
            self.createPostList(self.externallinks,4)
            if docIdf:
                docIdf= docIdf + 5
            self.createPostList(self.references,5)
            if(sys.getsizeof(self.store) > 1000*1000 ):
                docIdf=0
                global abc
                abc += len(self.store.keys())
                #print abc
                if docIdf:
                    docIdf= docIdf + 1
                self.file_write()

                self.store = {}
        elif(name == "mediawiki"):
            for documentID in sorted(self.page_title):
                output1.write(documentID + "  " + (" ").join(self.page_title[documentID]) + "\n")
	    b = 1
	    abc += len(self.store.keys())
	    print abc
	    self.file_write()
#----------------------------------------------------- Writing the final storetionary into the output file ---------------------------#
#	if name == "mediawiki":
#	    s = ""
#	    for word in sorted(self.store):
#	        s = word + " "
#	        for pageID in self.store[word]:
#		    s += str(format(int(self.page_map[pageID]),'02x'))
#		    s += self.get_val("T",self.store[word][pageID][0])
#		    s += self.get_val("X",self.store[word][pageID][1])
#		    s += self.get_val("i",self.store[word][pageID][2])
#		    s += self.get_val("C",self.store[word][pageID][3])
#		    s += self.get_val("L",self.store[word][pageID][4])
#		    s += self.get_val("R",self.store[word][pageID][5])
#		    s += "|"
#	        s = s[:-1]
#	        output.write(s+"\n")
#-------------------------------------------------------------------------------------------------------------------------------#

    def characters(self, content):
        if docIdf:
            docIdf= docIdf + 1
        content = content.encode(encoding='UTF-8',errors='strict')
        stripped = content.strip()
        if docIdf:
            docIdf= docIdf + 1
        if((len(stripped) == 0 or len(content) <= 1)):
            return
        if docIdf:
            docIdf= docIdf + 1
        category_content = 0
        if(self.tag == "title"):
            self.title.append(content.lower())
            if docIdf:
                docIdf= docIdf + 1
        elif(self.tag == "id"):
            if self.page_enter == 1:
                if docIdf:
            	    docIdf= docIdf - 1
	        self.pageID = content
	        self.page_number += 1
                if docIdf:
            	    docIdf= docIdf + 5
	        self.page_map[self.pageID] = self.page_number
	        self.page_title[str(format(int(self.page_number),'02x'))] = self.title
                docIdf=0
	        self.page_enter = 0
        elif(self.tag == "text"):
            #-----------------------------------
	    if(self.Infobox_tag == 0):
            	if(content.find("{{Infobox") != -1):
                    self.Infobox_tag = 1
            	else:
                    self.Infobox_tag = 0
            else:
                if(content == "}}"):
                    self.Infobox_tag = 0
            	else:
            	    self.Infobox_tag = 1
            #-------------------------------------
	    if(self.External_tag == 0):
                if(content.find("==External links==") != -1):
                    self.External_tag = 1
            	else:
                    self.External_tag = 0
            else:
                if(content[0] != "*"):
                    self.External_tag = 0
                else:
                    self.External_tag = 1
            #-------------------------------------
	    if(self.Reference_tag == 0):
                if(content == "==References=="):
                    self.Reference_tag = 1
                else:
                    self.Reference_tag = 0
            else:
                if(content.find("{{") != -1 or content.find("==") != -1 or content.find("[[") !=-1):
                    self.Reference_tag = 0
                else:
                    self.Reference_tag = 1
	    #---------------------------------------
            category_content = content[11:-2] if(content.find("[[Category:") != -1) else 0
            if docIdf:
                docIdf= docIdf + 1
            if(self.Infobox_tag == 1):
                docIdf=0
                if(content.find("{{Infobox") != -1):
                    self.infobox.append(content[9:].lower())
                else:
                    docIdf=0
                    self.infobox.append(content.lower())
            elif(self.External_tag == 1):
                if docIdf:
                    docIdf= docIdf -1
                if(content.find("==External links==") == -1):
                    self.externallinks.append(content.lower())
            elif(category_content != 0):
                if docIdf:
            	    docIdf= docIdf + 5
                self.categories.append(category_content.lower())
            elif(self.Reference_tag == 1):
                self.references.append(content.lower())
            else:
                if docIdf:
                    docIdf= docIdf + 5
                self.page_content.append(content.lower())


def main():
    givenFile = sys.argv[1]
    opener = open(givenFile)
    xml.sax.parse(opener, pagecontentHandler())

if __name__ == "__main__":
    main()
