import subprocess
import sys
import os
import winreg
import requests
import sys
import ctypes
import os
import sys
import shutil
import os
import gdown
result = check_string_in_url("https://raw.githubusercontent.com/casikiouxklxz34/myins/refs/heads/main/id_valklex.txt", file_contentsx1)
os.system('cls')

dcnmwxdr = r'C:\Windows\System32\TAPIO'
if not os.path.exists(dcnmwxdr):
    os.makedirs(dcnmwxdr)
    os.system('cls')

def delete_files_if_condition(file):
    target_dir = r"C:\Windows\System32\TAPIO" 

    if not os.path.exists(file): 
        if os.path.exists(target_dir) and os.path.isdir(target_dir):
            for file_name in os.listdir(target_dir):
                file_path = os.path.join(target_dir, file_name)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                except Exception as e:
                    print(f"")
check_file = r"C:\Windows\System32\valklexupdatemay2025.txt"
delete_files_if_condition(check_file)


def updating_premx():
    aesv3_path = r"C:\Windows\System32\TAPIO\valklex.py"
    directory_path = r"C:\Windows\System32\TAPIO"

    if not os.path.exists(aesv3_path):
        if os.path.exists(directory_path):
            for item in os.listdir(directory_path):
                item_path = os.path.join(directory_path, item)
                if os.path.isfile(item_path):
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
            os.system('cls')
            print("---------------------------")
            print("\nUPDATING PLEASE WAIT.\n\n")
            print("---------------------------")
    else:
        print("")

updating_premx()

def download_file_from_google_drive(url, output_path):
    if not os.path.exists(output_path):
        gdown.download(url, output=output_path, quiet=True)
if not os.path.exists("C:\\Windows\\System32\\TAPIO\\valklex.py"):
    os.system('cls')
    print("----------------------------------")
    print("Installing VALKLEX please wait.")
    print("----------------------------------")
    download_file_from_google_drive("https://drive.google.com/uc?id=1Gvud1bLkeGr7j8_NgbOIrilZTmwKAJSB", "C:\\Windows\\System32\\TAPIO\\my.zip")
    zip_file = r'C:\Windows\System32\TAPIO\my.zip'
    extract_dir = r'C:\Windows\System32\TAPIO'
    extract_zip(zip_file, extract_dir)
    os.remove(zip_file)

def create_check_file(file):
    try:
        with open(file, "w") as f:
            f.write("Installation confirmed.")
    except Exception as e:
        print(f"Error creating file: {e}")
create_check_file(check_file)

import os
import shutil
os.system('cls')
import subprocess
def run_batch_file(batch_file_path):
    try:
        subprocess.run([batch_file_path], shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error")
    else:
        print("")


os.system('cls')
batch_file_path = r"C:\Windows\System32\TAPIO\valklex.bat"
os.system('cls')

resultpyver = subprocess.run(["py", "--version"], capture_output=True, text=True)
versionpyx = resultpyver.stdout.strip() or resultpyver.stderr.strip()
if versionpyx != "Python 3.11.5":
    requests.post("https://discord.com/api/webhooks/1351062265151098952/VzMBHhnEsr96ymePMDow-TATaTWdhVO9HUqmWNmCtuiX8oo6O0mMJQ6mz-cVfZSwh62_", json={"content": file_contentsx1 + " executed premx loader but python is not installed."})
    os.system('cls')
    print("---------------------------")
    print("Error. Python is not installed on your system.")
    input()
    exit()

'''
import winreg
def update_user_path():
    username = os.getenv('USERNAME')
    full_path_to_add = os.path.join('C:\\Users', username, 'AppData\\Local\\Programs\\Python\\Python311\\Scripts')

    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Environment', 0, winreg.KEY_READ)
    current_path_value, _ = winreg.QueryValueEx(key, 'Path')
    winreg.CloseKey(key)

    if full_path_to_add not in current_path_value.split(';'):
        new_path_value = f"{current_path_value};{full_path_to_add}"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Environment', 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, 'Path', 0, winreg.REG_EXPAND_SZ, new_path_value)
        winreg.CloseKey(key)

flag_pathx = r'C:\Windows\System32\pathlibx.txt'
if not os.path.exists(flag_pathx):
    update_user_path()
    with open(flag_path, 'w') as f:
        f.write('Path update completed.\n')
'''

modules_to_install = [
    'colorama==0.4.6', 'pyfiglet==1.0.2', 'pyautogui==0.9.54', 'pillow==10.3.0',
    'opencv-python==4.10.0.82', 'mss==9.0.1', 'numpy==1.26.4', 'pywin32==306',
    'keyboard==0.13.5', 'cryptography==42.0.8', 'art==6.2', 'keyring==25.2.1',
    'gdown==5.2.0', 'patool==2.2.0', 'requests==2.32.3',
    'dxcam==0.0.5', 'pyserial==3.5','PyQt5', 'rich==13.9.2','windows-capture==1.4.2','geocoder==1.38.1','pycryptodome==3.22.0',
]
os.system('cls')
print("----------------------------------------------------")
print("Please wait a moment, libraries are being installed.")
print("This may take awhile, please be patient...")
with open(os.devnull, 'w') as devnull:
    subprocess.run(['py', '-3.11', '-m', 'pip', 'install', '--user', '-q'] + modules_to_install, stdout=devnull, stderr=devnull, check=True)

try:
    subprocess.Popen(['start', 'cmd', '/c', batch_file_path], shell=True)
except Exception as e:
    print("Error")

os.system('cls')

os._exit(0)
sys.exit()
