import re 
count =0
matcher=re.finditer("\W","a7b@k9Z")
for match in matcher:
	print(match.start(),"...",match.group())

#1..7  
#3..@

#sandeep=[abc]