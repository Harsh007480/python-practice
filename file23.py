import os
if(not os.path.exists("Python _new")):
   os.mkdir("Python _new")

for i in range(0,50):
    os.mkdir(f"python _new{i+1}.py")