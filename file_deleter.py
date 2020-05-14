import os

current_cwd = os.getcwd()
print(current_cwd)

# list of unwanted extensions
extensions = ['.nfo', '.jpg', '.rtf', '.txt']

# later used method 'endswith()' doesn't accept list as arg, only tuples
ext1 = tuple(extensions)

user_warning = input("Warning: You are about to delete files, type 'y' to delete files or 'n' to cancel")

# loop over all subdirs in root folder
for root, dirs, files in os.walk(current_cwd):
	for name in files: 
		if name.endswith(ext1):
			if user_warning == 'y':
				os.remove(root + '/' + name)
			elif user_warning == 'n':
				print('Process cancelled')
				break
