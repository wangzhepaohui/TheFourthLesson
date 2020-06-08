import os
import posixpath

path = input("Please input the folder path:")

files= os.listdir(path)
print(format(files))

for file in files:
    end = os.path.splittext(file)[-1]
    # end = "/Users/liuhaozhe/PycharmProjects/TheFourthLesson/homework3.py"
    # ff= os.path.splittext(end)[-1]
    print(format(end))


