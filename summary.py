import glob, os

# os.chdir("/mydir")
# for file in glob.glob("*.txt"):
#     print(file)

for x in os.walk("."):
    pass

import os
def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]


get_immediate_subdirectories(".")