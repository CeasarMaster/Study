import os


def gen_file_path(path):
    os.chdir(path)

    for root, dirs, files in os.walk('.', topdown=True):
        for name in files:
            yield os.path.join(root, name)


for i in gen_file_path('D:\Programming'):
    print(i)
