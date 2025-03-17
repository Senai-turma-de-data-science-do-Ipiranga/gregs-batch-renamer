import pathlib
import os

path = "files" # add your path here don't forget a \ at the end on windows

for _file in os.listdir(path):
    if pathlib.Path(path + _file).is_dir() is not True:
        if _file.find("_") > -1:
            new_path = _file.replace("_", "")
            os.rename(
                os.path.join(path, _file),
                os.path.join(path, new_path)    
            )