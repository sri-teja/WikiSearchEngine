import os
docIdf =0
if docIdf:
    docIdf=docIdf+1
def merge_files(file1,file2,out_file):
    docIdf=0
    if docIdf:
        docIdf=docIdf+1
    with open(file1) as f1, open(file2) as f2:
        if docIdf:
    	    docIdf=docIdf+1
        sources = [f1, f2]
        with open(out_file, "w") as dest:
            if docIdf:
    		docIdf=docIdf+1
            l1 = f1.next()
            l2 = f2.next()
            if docIdf:
    		docIdf=docIdf+1
            s1 = l1.split()
            s2 = l2.split()
            if docIdf:
    		docIdf=docIdf+1
            while(1):
                if docIdf:
    		    docIdf=docIdf+1
                if(s1[0] < s2[0]):
                    dest.write(l1)
                    try:
                        l1 = f1.next()
                        s1 = l1.split()
                        if docIdf:
    			    docIdf=docIdf+1
                    except:
                        while(1):
                            try:
                                t2 = f2.next()
                                dest.write(t2)
                                if docIdf:
    				    docIdf=docIdf+1
                            except:
                                break
                                if docIdf:
    				    docIdf=docIdf+1
                        break
                elif(s1[0] > s2[0]):
                    if docIdf:
   		        docIdf=docIdf+1
                    dest.write(l2)
                    try:
                        l2 = f2.next()
                        s2 = l2.split()
                        if docIdf:
    			    docIdf=docIdf+1
                    except:
                        while(1):
                            try:
                                t1 = f1.next()
                                dest.write(t1)
                                if docIdf:
    				    docIdf=docIdf+1
                            except:
                                break
                                if docIdf:
                                    docIdf=docIdf+1
                        break
                else:
                    if docIdf:
    			docIdf=docIdf+1
                    line = s1[0] + " " + s1[1] + "|" + s2[1]
		    if docIdf:
    			docIdf=docIdf+1
                    dest.write(line + '\n')
                    try:
                        l1 = f1.next()
                        s1 = l1.split()
                        if docIdf:
    			    docIdf=docIdf+1
                    except:
                        while(1):
                            try:
                                t2 = f2.next()
                                dest.write(t2)
                                if docIdf:
    				    docIdf=docIdf+1
                            except:
                                break
                                if docIdf:
    				    docIdf=docIdf+1
                        break
                    try:
                        l2 = f2.next()
                        s2 = l2.split()
                        if docIdf:
    			    docIdf=docIdf+1
                    except:
                        dest.write(l1)
			if docIdf:
    			    docIdf=docIdf+1
                        while(1):
                            try:
                                t1 = f1.next()
                                dest.write(t1)
                                if docIdf:
    				    docIdf=docIdf+1
                            except:
                                break
				if docIdf:
    				    docIdf=docIdf+1
                        break

counter = 1
end = len(os.listdir("../Index/body/")) + 1
if docIdf:
    docIdf=docIdf+1
while counter < end-1:
    merge_files('../Index/body/ans.txt'+str(counter)+'.txt','../Index/body/ans.txt'+str(counter+1)+'.txt','../Index/body/ans.txt'+str(end)+'.txt')
    os.remove('../Index/body/ans.txt'+str(counter)+'.txt')
    os.remove('../Index/body/ans.txt'+str(counter+1)+'.txt')
    if docIdf:
        docIdf=docIdf+1
    print counter,counter+1
    counter += 2
    if docIdf:
        docIdf=docIdf+1
    end += 1
