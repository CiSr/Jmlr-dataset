from collections import Counter
from itertools import chain
from collections import defaultdict
import glob
import re
import sys
import xmltodict
#import nltk
temp=glob.glob("o*.txt")
d = defaultdict(list)

print len(temp)

i=1
for i in range(0,len(temp)):
        with open(temp[i], 'rU') as f:
                data=f.read()
                a= dict(xmltodict.parse(data)['dblp']['article'])

		#print i
		#print temp[i]		
		#print a.get('author')
		#print a.get('title')


		a.pop("ee", None)
		a.pop("journal",None)
		a.pop("volume",None)
		a.pop("@mdate",None)
		a.pop("@key",None)
		a.pop("volume",None)
		a.pop("year",None)
		a.pop("pages",None)
		a.pop("url",None)
		a.pop("number",None)
		a.pop("[a-z,0-9]*",None)
		keys=a.viewkeys()
		#print keys
#		print a
		sz= len(a.get('author'))
		lt= len(a.get('title'))

		st=''
		for i in range(0,lt):
			st=st+str(a.get('title')[i])


#		print st

		for i in range(0,sz):
			d[a.get('author')[i]].append(st)


#		print a.get('title')
	
#		data1=[(2010, 2), (2009, 4), (1989, 8), (2009, 7)]
#		d[a.get('author')].append(a.get('title'))
		#print data
		#print a[0].split(',')
		#print d

#for a.viewkeys('author'), a.viewkeys('title') in data:
#	     		d['author'].append('title')
		#list=a
		#print list
		#s=dict(chain(a[i].iteritems(), a[i+1].iteritems()))
		#print s
		#temp=a.get('author')
		#print temp.split(',')
		#print a.get('title')
		#new=set(a.get('author'))
		#print new
		#newdict=a.copy()
		#print newdict
		#c = {x: a.get(x, 0) + a.get(x, 1) }
		#print c
		#d = defaultdict(list)
		#r=a.get('author')
		#s=a.get('title')
		#for r,s in a:
    		#	 d[r].append(s)
		#print a.get('author')		
		#print a.get('title')
		

#for author, title in data:
#     d[author].append(title)


dl=len(d)

print d.items()
#for i in range(0,dl):
#	print d[i]

#for year, month in data1:


#print d[2009]



