import hashlib 
sent = input('enter string to hash:')
result = hashlib.md5(sent.encode()) 
print("The byte equivalent of hash is : ", end ="")
print(result.hexdigest())