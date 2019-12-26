plain_text="Niyati Patel"
d={'a':'z','b':'y','c':'x','d':'w','e':'v','f':'u','g':'t','h':'s','i':'r','j':'q','k':'p','l':'o','m':'n',
'n':'m','o':'l','p':'k','q':'j','r':'i','s':'h','t':'g','u':'f','v':'e','w':'d','x':'c','y':'b','z':'a'}
cipher_text=""
for i in plain_text:
	if i.isupper():
		k=i.lower()
		if k in d:
			s=d[k]
			u=s.upper()
			cipher_text+=u
	elif i==" ":
		cipher_text+=" "
	else:
		if i in d:
			s=d[i]
			cipher_text+=s
print("Plain text: ",plain_text)
print("Cipher text: ",cipher_text)
d1={}
for i in plain_text:
	if i==" ":
		continue
	else:
		c=plain_text.count(i)
		d1[i]=c
print(d1)
d2={}
for i in cipher_text:
	if i==" ":
		continue
	else:		
		c=cipher_text.count(i)
		d2[i]=c
print(d2)
