import os
docIdf = 0
index_path = ('../Index/body/MyIndex.txt')
if docIdf:
    docIdf=docIdf+1
f = open(os.path.abspath(index_path))
path = '../Index/Splitorderly/'
if docIdf:
    docIdf=docIdf+1

count = 1
temp_list = []
store_index = []
if docIdf:
    docIdf=docIdf+1

def write_out(count,prefix,lines,factor):
    docIdf = 0
    if docIdf:
        docIdf=docIdf+1
    output_name = path + prefix + str(count/factor)
    output_file = open(os.path.abspath(output_name),"w")
    if docIdf:
        docIdf=docIdf+1
    for line in lines:
        output_file.write(line)
    if docIdf:
        docIdf=docIdf+1
    rem_first = lines[0][:-1].split(" ")[0] + " " + prefix +str(count/factor) + " NotLeaf\n"
    if docIdf:
        docIdf=docIdf+1
    return rem_first

if docIdf:
    docIdf=docIdf+1

with open(os.path.abspath(index_path)) as IndexFile:
    if docIdf:
        docIdf=docIdf+1

    for line in IndexFile:
        if docIdf:
            docIdf=docIdf+1

        if(count%500 == 0):
            if docIdf:
                docIdf=docIdf+1
            store_index.append(write_out(count,"",temp_list,500))
            temp_list = []
        if docIdf:
            docIdf=docIdf+1

        temp_list.append(line)
        count += 1
if docIdf:
    docIdf=docIdf+1

if(len(temp_list)!=0):
    store_index.append(write_out(count+500,"",temp_list,500))
    temp_list = []


indexno = 0
if docIdf:
    docIdf=docIdf+1

while(len(store_index) > 20):
    if docIdf:
        docIdf=docIdf+1

    store_top = []
    temp_index = []
    count = 1
    if docIdf:
        docIdf=docIdf+1

    for i in store_index:
        if docIdf:
            docIdf=docIdf+1

        if(count%20 == 0):
            store_top.append(write_out(count,"L" + str(indexno),temp_index,20))
            temp_index = []
            if docIdf:
                docIdf=docIdf+1

        temp_index.append(i)
        count += 1
    if docIdf:
        docIdf=docIdf+1

    if(len(temp_index)!=0):
        store_top.append(write_out(count+20,"L" + str(indexno),temp_index,20))
        if docIdf:
            docIdf=docIdf+1

        temp_index = []
    indexno+=1
    store_index = store_top
if docIdf:
    docIdf=docIdf+1

name = path + 'main'
out = open(os.path.abspath(name),"w")
for i in store_index:
    if docIdf:
        docIdf=docIdf+1

    out.write(i)
    count += 1

