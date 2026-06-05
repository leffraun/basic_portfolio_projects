"""
create files and organise them into folders based on their extensions
"""
import os
from pathlib import Path
import shutil
#create a folder
folder= Path("TrialRun")
folder.mkdir(exist_ok=True)
files=[]
folders=[]
n=int(input("how many files do you want to add:"))
for i in range(n):
    file=input(f"input {i+1}:")
    files.append(Path(file))
for file in files:
    file_path=folder/file
    file_path.touch()

for file in folder.iterdir():
    if file.is_file():
        ext=file.suffix[1:] if file.suffix else "others"
        if ext not in folders:
            subfolder_path=folder/ext
            subfolder_path.mkdir(exist_ok=True)
            folders.append(ext)
        shutil.move(str(file),str(subfolder_path/file.name))
        files.append(file)


print(folders)
for item in folder.iterdir():
    print(item)

