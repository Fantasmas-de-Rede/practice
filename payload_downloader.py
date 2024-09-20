import requests

url = "http://example.com/payload.exe"  # URL de téléchargement de l'exemple
local_filename = "downloaded_payload.exe"

def download_file(url, local_filename):
    response = requests.get(url)
    with open(local_filename, 'wb') as file:
        file.write(response.content)

download_file(url, local_filename)
print("Téléchargement terminé.")
