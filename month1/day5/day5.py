#problem1
lang1='rust'
languages=['go', 'java', 'hph' , 'python', 'javascript', 'ruby']
for i in languages:
	if (i==lang1):
		print("this languages is in list")
	else:
		print()
#problem2
lang1='rust'
languages=['go', 'java', 'hph' , 'python', 'javascript', 'ruby']
for a in languages:
	if a=='php':
		print('php')
		break
	print(a)
#problem3
#a=7
#for a*a:
#	k+=1
#4
languages=['go', 'java', 'hph' , 'python', 'javascript', 'ruby']
d=len(languages)
for i in range(d):
	print(i+0, languages[i])
#5
a=[]
for i in range(1, 11):
	a.append(a)
b=str(a[0:-1]+x[::-1])
print(b)
