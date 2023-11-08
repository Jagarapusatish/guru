
# File Handling write mode
fp=open("myfile.txt","w")
fp.write("welcome")
print("file written")
fp=open("myfile.txt","r")
print(fp.read())
