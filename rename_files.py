import os

def rename_files(file_path):
	#Copy the current working directory
	working_path = os.getcwd()

	#(1) get file names from a folder
	file_list = os.listdir(file_path)

	#Change current working directory to the folder with the files
	os.chdir(file_path)
	
	#(2) for each file, rename filename
	for file_name in file_list:

		#Print original file name
		print("Original File Name: " + file_name)

		#Renames the input file using translate(table to translate, characters to delete)
		os.rename(file_name, file_name.translate(None, "0123456789"))

		#Print updated file name
		print("New File Name: " + file_name)

	#Change current working directory back to original
	os.chdir(working_path)

#Set directory for files that need processing
file_path = r'/Users/Jasen/nanodegree/PythonFound/rename_files/prank'

rename_files(file_path)


