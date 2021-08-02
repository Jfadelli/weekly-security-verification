import os
import shutil

with open('user_info.txt', 'r') as file:
    user_account_name = file.read().replace('\n', '')

#  Set Filename Variables
desktop = 'C:/Users/'+user_account_name+'/desktop'
documents = 'C:/Users/'+user_account_name+'/documents'
downloads = 'C:/Users/'+user_account_name+'/downloads'

#  REMOVE THE FILES
try:
    for f in os.listdir(desktop):
        path = os.path.join(desktop, f)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)
except Exception as e:
    print("An exception occured: ", e)

try:
    for f in os.listdir(documents):
        path = os.path.join(documents, f)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)
except Exception as e:
    print("An exception occured: ", e)

try:
    for f in os.listdir(downloads):
        path = os.path.join(downloads, f)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)
except Exception as e:
    print("An exception occured: ", e)
print('program closing...')

#  Create SHOW THE FOLDERS functions
ShowDesktop = os.system('explorer "C:\\Users\\"'+user_account_name+'"\Desktop"')
ShowDownloads = os.system('explorer "C:\\Users\\"'+user_account_name+'"\Downloads"')
ShowDocuments = os.system('explorer "C:\\Users\\"'+user_account_name+'"\Documents"')

#  SHOW THE FOLDERS
ShowDesktop
ShowDownloads
ShowDocuments