# listfiles.py>
import os

# <editor-fold desc="Scan for files in a specific folder">
def scanforfiles(torque_dir):
        torque_files = []
        dirscan = os.scandir(torque_dir)
        for item in dirscan:
            try:
                
            #    if item.is_file():
                torque_files.append(item.path)
            except:
                print("skipping one item due to exception")

        dirscan.close()
        return torque_files
# </editor-fold>
