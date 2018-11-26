import hashlib
#File 1
hasher1 = hashlib.md5()
afile1 = open('/home/lucifer/md5sumtest/somerandomdirectory/testfile1', 'rb')
buf1 = afile1.read()
a = hasher1.update(buf1)
md5_a=(str(hasher1.hexdigest()))

#File 2
hasher2 = hashlib.md5()
afile2 = open('/home/lucifer/md5sumtest/somerandomdirectory2/testfile1', 'rb')
buf2 = afile2.read()
b = hasher2.update(buf2)
md5_b=(str(hasher2.hexdigest()))
#Compare md5
if(md5_a==md5_b):
    print("Yes")
else:
    print("No")

##No
