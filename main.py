from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

# ID sheet
folder_id = "14vfuG38VeV9NxXln1xq8ELDWdwUO4Bsp"

# Query untuk list isi folder
file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()

for file in file_list:
    print(f"{file['title']} — ID: {file['id']}")