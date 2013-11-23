import codecs
import re
fi=codecs.open('dump2.txt', 'r', encoding='utf-8')
fg=fi.read()
fi.close
fg=fg.split("\n")
start='a'
end='x'
for index,lines in enumerate(fg):
	if lines[0]==start and lines[-1]==end:
		fi=codecs.open('write.txt', 'a+', encoding='utf-8')
		fi.write(lines)
		fi.close
	else:
		continue
