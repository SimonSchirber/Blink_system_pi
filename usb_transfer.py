import shutil, errno
import os

usb_256 = '/media/pi/EBB2-C6AB/blink'
usb_2tb = '/media/pi/76E8-CACF/blink_backup'    
        
month_dir = os.listdir(usb_256)
for month in month_dir:
    path_to_copy = os.path.join(usb_256, month)
    path_to_save = os.path.join(usb_2tb, month)
    og_path_to_save = os.path.join(usb_2tb, month)
    i = 0
    if os.path.exists(path_to_save):
        while os.path.exists(path_to_save):
            i += 1
            str_to_add = str('(' + str(i) + ')')
            path_to_save = str(og_path_to_save + str_to_add)
    os.mkdir(path_to_save)
    day_dir = os.listdir(path_to_copy)
    for day in day_dir:
        day_path_to_copy = os.path.join(path_to_copy, day)
        day_path_to_save = os.path.join(path_to_save, day)
        os.mkdir(day_path_to_save)
        for file in os.listdir(day_path_to_copy):
            print("backing up file " + str(file) + " to drive:")
            print(day_path_to_save)
            file_copy = os.path.join(day_path_to_copy, file)
            shutil.copy2(file_copy, day_path_to_save)

##Delete everything
try:
    shutil.rmtree(usb_256)
except:
    print("could not find files in " + str(usb256) + " to delete")
##delete backup files if present
usb_256_backup = '/media/pi/EBB2-C6AB/blink_backup'
try:
    shutil.rmtree(usb_256_backup)
except:
    print("no backup files in " + str(usb_256_backup) + " to delete")
    
## Delete every folder with "Blink" in it
## Delete every folder with "Blink" in it
blink_path = '/media/pi/EBB2-C6AB'
blink_dir = os.listdir('/media/pi/EBB2-C6AB')
for blink in blink_dir:  
    if "blink" in blink:
        blink_to_del = os.path.join(blink_path, blink)
        shutil.rmtree(blink_to_del)
## Success
print("Sucessfully backed up and deleted, thank you dad!")
