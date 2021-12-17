import os

folder = '' #path to folder containing .jpg and .png files

def imgSrcs(folder):
    for file in os.listdir(folder):
        if file.endswith('.jpg' or '.png'):
            print(file)

def imgAlts(folder):
    files = [os.path.splitext(filename)[0] for filename in os.listdir(folder) if filename.endswith('.jpg' or '.png')]
    for file in files:
        print (file.replace('-', ' ')) #replacement for hyphen-separated filenames

#call imgSrcs(folder) from terminal
#call imgAlts(folder) from terminal
