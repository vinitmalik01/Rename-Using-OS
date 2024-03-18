import os

folder_path = input('Enter the folder path: ')

# List all files in the folder
files = os.listdir(folder_path)

for i, filename in enumerate(files):
    if filename.endswith('.mp3'):
        src = os.path.join(folder_path, filename)
        newname = os.path.join(folder_path, f"{i+1}.mp3")
        os.rename(src, newname)
        
print('Task completed')
