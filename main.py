import os
import shutil
# print(os.getcwd())

#function to move files to specified folder
def clear(folder, files):
    for file in files:
        os.replace(file, f"{folder}/{file}")

#display all the files and folders of the current folder
files = os.listdir()
files.remove("main.py")
print(files)

#function to create directories
def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

if __name__ == "__main__":
    createIfNotExist("Images")
    createIfNotExist("doc")
    # createIfNotExist("pdf")
    createIfNotExist("movie")
    createIfNotExist('Others')
 
    imgExts = [".png", ".jpg",".jpeg"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
    # print(images)

    docExts = [".pdf", ".txt", ".docx"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]
    # print(docs)

    movieExts = [".mp4"]
    movie = [file for file in files if os.path.splitext(file)[1].lower() in movieExts]
    # print(movie)

    others = []
    #for loop for other files 
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in imgExts) and (ext not in docExts) and (ext not in movieExts) and os.path.isfile(file):
            others.append(file)
    # print(others)

    clear("Images", images)
    clear("doc", docs)
    clear("movie", movie)
    clear("Others", others)
    # # for film in movie:
    # #     os.replace(film,f"movie/{film}")

    # # for image in images:
    # #     shutil.move(clear,f"clear/Images")
    
    # # #Check whether specified path is an existing file or not
    # # isFile = os.path.isfile(os.getcwd())
    # # print(isFile)

    # # #Check whether specified path is an existing directory or not
    # # isDir = os.path.isdir(os.getcwd())
    # # print(isDir)


