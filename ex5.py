fp=open("Home\\python11.txt",'w+')
fp.write("python is Important to me")
fp.write("This is a good day")
fp.seek(0)
print(fp.read())
fp.close()