from pathlib import Path
from _datetime import datetime
import zipfile



root=Path("/Users/dhingra/Downloads/TestFiles")
def playwithPath():
    filepaths=list(root.iterdir())
    for pat in filepaths:
        newfilename=pat.stem+"_"+datetime.now().strftime("%d_%m_%Y_%H_%M")+pat.suffix
        newfilepath=pat.with_name(newfilename)
        pat.rename(newfilepath)

def PlaywithFolder():

    filepaths=list(root.glob("**/*")) # This is used to demonstrate the path of folder
    for pat in filepaths:
        if(pat.is_file()):
            yearname=pat.parts[-3] #Parts is used to fetch full path
            monname=pat.parts[-2]
            filename=yearname+"_"+monname+"_"+pat.name
            filepath=pat.with_name(filename) #with_name function is used to add the path with new filename
            pat.rename(filepath)



def PlayCreatedTime():
    filepaths=list(root.glob("**/*"))
    for pat in filepaths:
        if(pat.is_file()):
            createdTime=datetime.fromtimestamp(pat.stat().st_ctime).strftime("%d-%m-%Y")
            filename=pat.stem+"_"+createdTime+"_"+pat.suffix
            filepath=pat.with_name(filename)
            pat.rename(filepath)

def convertExtension():
    filepaths=list(root.glob("**/*.txt"))
    for pat in filepaths:
        filepath=pat.with_suffix(".csv")
        pat.rename(filepath)


def createEmptyFiles(n):
    for i in range(1,n):
        filename=str(i)+".txt"
        filepath=root/Path(filename)
        filepath.touch()

def zipTheFiles():
    archivepath=root/Path("archive.zip")
    with zipfile.ZipFile(archivepath,"w") as zf:
        filepaths = list(root.glob("**/*.txt"))
        for pat in filepaths:
            zf.write(pat)
            pat.unlink()


def unzipFiles():
        filepaths = list(root.glob("**/*.zip"))
        for pat in filepaths:
            with zipfile.ZipFile(pat, "r") as zf:
                dest=root/Path(pat.name.replace(".zip",""))
                zf.extractall(path=dest)

def searchFile(filenam):
    filepaths = list(root.rglob("*"))
    for pat in filepaths:
        if pat.is_file():
            if filenam in pat.stem:
                print(pat.absolute())

        """
        if(pat.name.find(filenam)!=-1 and pat.is_file()):
            pat.absolute()
            """

    #print(filepaths)


