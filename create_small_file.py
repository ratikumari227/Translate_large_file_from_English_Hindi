# set the path here
import os
file_path = 'ques.txt'
file_text = open(file_path, "r")
os.chdir('/home/rati/Downloads/google_translation/extracted')
a = True
i=0
count=1
name = str(count)
filename = "%s.txt" % name
newFile = open(filename, "w")
while a:
    file_line = file_text.readline()
    print(file_line)
    newFile.write(file_line)
    if not file_line:
        newFile.close()
        print("End Of File")
        a = False
    else:
      
      if i == 1999:
        # Closing file
        newFile.close()
        i=0
        count +=1
        name = str(count)
        filename = "%s.txt" % name
        newFile = open(filename, "x")
      else:
        i+=1


file_text.close()
