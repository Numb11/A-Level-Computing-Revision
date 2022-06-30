def publicA(message):
 text = []
 for i in message:
     text.append(ord(i))
 return text
def privateA(message):
  text = []
  for i in (message):
     text.append(chr(i))
  return text

    
def publicB(message):
 text = []
 for i in message:
     text.append(ord(i)-1)
 return text
def privateB(message):
 text = []
 for i in (message):
     text.append(chr(i+1))
 return text

print(publicB(["a","b","c"]))
print(privateB(publicB(["a","b","c"])))

#SEND A MESSAGE TO B
sent = (privateA(publicB(["a","b","c"]))) #COMBINED ENCRYPTION KEY
print(sent)
received = (privateB(publicA(sent)))
print(received)
