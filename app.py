import os
import shutil

path = os.path.expanduser("~") + "/Downloads"

folders = {
    "Documentos": [".pdf", ".docx", ".txt"],
    "Imagens": [".jpg", ".png", ".jpeg"],
    "Instaladores": [".exe", ".msi"],
    "Compactados": [".zip", ".rar", ".7z"]
}

def organizar():
    for filename in os.listdir(path):
        filepath = os.path.join(path, filename)

        if os.path.isdir(filepath):
            continue

        ext = os.path.splitext(filename)[1].lower()
        
        for folder_name, extensions in folders.items():
            if ext in extensions:
                dest_path = os.path.join(path, folder_name, filename)
                
                if not os.path.exists(dest_path):
                    print(f"Organizando: {filename} -> {folder_name}")
                    shutil.move(filepath, dest_path)
                else:
                    print(f"Aviso: {filename} já existe em {folder_name}. Pulando...")

if __name__ == "__main__":
    organizar()