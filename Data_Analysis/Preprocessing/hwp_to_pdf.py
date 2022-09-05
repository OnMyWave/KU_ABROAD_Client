import os
import win32com.client as win32
import win32gui

BASE_DIR = "C:\\Users\\JongGeun\\iCloudDrive\\Desktop\\download"
os.chdir(BASE_DIR)

hwp_list = []
for f_name in os.listdir():
    if f_name.endswith('.hwp'):
        hwp_list.append(f_name)

hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")
hwnd = win32gui.FindWindow(None, 'Noname 1 - HWP')

print(hwnd)

for i in hwp_list:
    hwp.Open(os.path.join(BASE_DIR, i))
    hwp.SaveAs(BASE_DIR+"\\"+i+".pdf", "PDF")


hwp.Quit()