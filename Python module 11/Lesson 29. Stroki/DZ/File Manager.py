directory = input('Insert the file directory: ')
disk = input('Insert the disk the file is located in: ')
file_type = input('Insert the file type: ')
if directory.startswith(disk) and directory.endswith(file_type):
    print('File correct')

else:
    print('File incorrect')




