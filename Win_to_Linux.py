import os             
# all_files = os.listdir("labels/") 

os.chdir("C:\\Users\\Saurav Akolia\\OIDv4_ToolKit\\OID\\Dataset\\validation\\")
# all_files=[]
# import os
# for file in os.listdir("img"):
#     if file.endswith(".txt"):
#        all_files.append(file)
	# replacement strings
WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'


import glob
import os

# os.chdir(r'directory where the files are located')
myFiles = glob.glob('*.txt')
print(myFiles)

	# relative or absolute file path, e.g.:
# file_path = r"soc.txt"
# myFiles="obj.names"



for x in myFiles:
	with open(x, 'rb') as open_file:
		content = open_file.read()

	content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)

	with open(x, 'wb') as open_file:
		open_file.write(content)




# for replacing strings


# for x in myFiles:
# 	with open(x, 'rt') as open_file:
# 		content = open_file.read()

# 	content = content.replace('Chair','0')
# 	open_file.close()

# 	with open(x, 'wt') as open_file:
# 		open_file.write(content)
# 	open_file.close()
	# with open(x, 'wb') as open_file:
	# 	open_file.write(content)
	# open_file.close()



# #read input file
# fin = open("data.txt", "rt")
# #read file contents to string
# data = fin.read()
# #replace all occurrences of the required string
# data = data.replace('pyton', 'python')
# #close the input file
# fin.close()
# #open the input file in write mode
# fin = open("data.txt", "wt")
# #overrite the input file with the resulting data
# fin.write(data)
# #close the file
# fin.close()


