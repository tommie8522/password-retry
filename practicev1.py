i=3
p = input('請輸入密碼')
while p!='a123456':
	i1=i-1 
	if i1==0:
		print('登入失敗')
		break
	else :
		print('你只剩下',i1,'次機會')
		p=input('請輸入密碼')
		i=i1
while p=='a123456' :
	print('登入成功')
	break
	


