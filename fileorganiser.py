"""
create files and organise them into folders based on their extensions
"""
#first function is to create a file
#next one is to create subfolders and arranges them
#and a third displays all this to console.
import shutil
from pathlib import Path

folder=Path("Another")
files=[]
subfolder=[]
def create_file(folder,files):
    folder.mkdir(exist_ok=True) #creating the file
    print("file is set!")
    n=int(input("enter number of files you want to add to:"))
    for i in range(n):
        file=input("enter the name of the file you want to add:")
        files.append(file)
        file_path=folder/file
        file_path.touch() #create file in that folder


def create_subfolder(folder,subfolder):
    for file in folder.iterdir():
        ext=file.suffix[1:] if file.suffix else "others"
        if ext not in subfolder:
            subfolder.append(ext)
        subfolder_path=folder/ext
        subfolder_path.mkdir(exist_ok=True)
        shutil.move(str(file), str(subfolder_path/file.name))


def displayfiles(folder):
    for file in folder.iterdir():
        print(file)


create_file(folder,files)
create_subfolder(folder,subfolder)
displayfiles(folder)

