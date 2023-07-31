import os
import shutil
import psutil
import subprocess

# Custom Variables
appName = 'My App 1.27'
dmgFile = 'My App.dmg'
appFile = 'My App'


def input_var(fileName):
    global dmgFile
    dmgFile = fileName


# Function to install the application from the DMG file
def install_app():
    print("Installing App...")
    subprocess.run(["hdiutil", "attach", dmgFile], check=True)

    partitions = psutil.disk_partitions()
    for p in partitions:
        if len(str(p.mountpoint)) > 2:
            if str(p.mountpoint)[1] == "V":
                appName = str(p.mountpoint).split('/')[2]

    # Assuming the application is dragged into the Applications folder
    for file in os.listdir(f"/Volumes/{appName}/"):
        if file.endswith("app"):
            appFile = file
            shutil.copytree(f"/Volumes/{appName}/{appFile}", f"/Applications/{appFile}")


# Function to remove the DMG file
def remove_dmg():
    print(f"Unmounting and deleting {dmgFile}...")
    subprocess.run(["hdiutil", "detach", f"/Volumes/{appName}"], check=True)
    os.remove(dmgFile)
