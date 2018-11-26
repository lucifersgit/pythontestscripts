import hashlib
#File 1
hasher1 = hashlib.md5()
print("Enter the full path of files to compare - e.g. /home/user/file.txt")
afile1 = open(input("File 1: ", 'rb')
buf1 = afile1.read()
a = hasher1.update(buf1)
md5_a=(str(hasher1.hexdigest()))

#File 2
hasher2 = hashlib.md5()
afile2 = open(input("File 2: "), 'rb'))
buf2 = afile2.read()
b = hasher2.update(buf2)
md5_b=(str(hasher2.hexdigest()))
#Compare md5

print (" ")
print ("File 1 hash: ") + (md5_a)
print ("FIle 2 hash: ") + (md5_b)

print (" ") 
if(md5_a==md5_b):
    print("Yes - MD5 sums match")
else:
    print("No - MD5 sums do not match")

##No
