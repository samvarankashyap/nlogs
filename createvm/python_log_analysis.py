#!/usr/bin/python
from sets import Set
import sys
import os
import pdb
import re
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
dir_path=sys.argv[1]
tmp_content=[]
print dir_path
if len(sys.argv) != 2 :
	print "incorrect dir please give name of dir"

else:
	print "recursing through dir"
	file_names= os.listdir(dir_path)
	pdb.set_trace()
	for item in file_names:
		if os.path.isfile(dir_path+"/"+item):
			fd_r = open(dir_path+"/"+item,"r")
			content = fd_r.readlines()
			for line in content:
				line1 = line.split(" ")
				if len(line1)>=5:
					tmp_content.append(line1[4])


#p = re.compile('*')


def is_valid_host(host):
    '''IDN compatible domain validator'''
    host = host.encode('idna').lower()
    if not hasattr(is_valid_host, '_re'):
        import re
        is_valid_host._re = re.compile(r'^([0-9a-z][-\w]*[0-9a-z]\.)+[a-z0-9\-]{2,15}$')
    return bool(is_valid_host._re.match(host))



content = Set(tmp_content)			

filtered_con=""
for x in content:
	if is_valid_host(x):
		filtered_con+=x+"\n"
fd_w = open("filters.txt","a")
fd_w.write(filtered_con)

