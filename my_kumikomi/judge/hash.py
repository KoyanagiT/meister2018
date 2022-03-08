import hashlib

Path = 'change_f.py'

f = open(Path,'rb')
BinaryData = f.read()
f.close()

SHA256 = hashlib.sha256(BinaryData).hexdigest()
print('SHA256:',SHA256)
