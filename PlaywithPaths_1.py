from pathlib import Path
from _datetime import datetime


def playwithPath():
    root=Path("/Users/dhingra/Downloads/TestFiles")
    filepaths=list(root.iterdir())
    for pat in filepaths:
        newfilename=pat.stem+"_"+datetime.now().strftime("%d_%m_%Y_%H_%M")+pat.suffix
        newfilepath=pat.with_name(newfilename)
        pat.rename(newfilepath)