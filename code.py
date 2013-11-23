import codecs
import re
fi=codecs.open('yo2.txt', 'r', encoding='utf-8')
fg=fi.read()
fi.close
fg=fg.split("\n")
a=[]
for index,lines in enumerate(fg):
#	output= re.sub(r'(([0-9][a-z][A-Z])*)\n\n\t(.*)*', r'\0',lines)
##	re.sub(r"([A-Z][A-Z]+['\r\n']",r'\0',lines)
#	print(output)
	if not re.match(r"[a-z]*'[a-z]*",lines):
		if(len(lines)>2):
			print(lines)

		
