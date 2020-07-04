import os

putanja = "F:\Pycharm WIN10\Youtube list downloader\Kina bro"

i = 1
for d in os.listdir(putanja):
    filenew = str(i) + ".mp3"
    fileNewName = os.path.join(putanja , filenew)


    fileOldName = os.path.join(putanja , d)
    print(fileOldName)
    print(fileNewName)
    os.rename(fileOldName , fileNewName)
    i += 1

