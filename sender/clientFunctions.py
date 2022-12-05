import subprocess


FORMAT = "utf-8"

def getFileForTransfer():
    #past the path name of where the document you want to transfer reside
    #returns the filepath and the filename
    PATH = "/Users/farhanishraq/Downloads/Summer 2022/Summer-Projects/fileTransfers/send/"
    cur_dir =  subprocess.run(['ls',PATH], stdout=subprocess.PIPE)
    output = cur_dir.stdout
    print("Directory: ")
    print(output.decode(FORMAT))
    fileForTransfer = input("Select a file: ")
    fileForTransferPath = PATH+fileForTransfer
    return fileForTransferPath,fileForTransfer