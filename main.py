import os
import shutil

def organizar_arquivos(diretorio):
    """Organiza arquivos em pastas com base em suas extensões."""
    extensoes = {
        'Imagens': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documentos': ['.pdf', '.docx', '.txt'],
        'Vídeos': ['.mp4', '.mov', '.avi'],
        'Outros': []
    }

    if not os.path.exists(diretorio):
        print(f"Diretório {diretorio} não encontrado!")
        return

    for arquivo in os.listdir(diretorio):
        caminho_completo = os.path.join(diretorio, arquivo)

        if os.path.isfile(caminho_completo):
            _, extensao = os.path.splitext(arquivo)
            pasta_destino = next((pasta for pasta, exts in extensoes.items() if extensao in exts), 'Outros')

            caminho_pasta = os.path.join(diretorio, pasta_destino)
            os.makedirs(caminho_pasta, exist_ok=True)
            shutil.move(caminho_completo, os.path.join(caminho_pasta, arquivo))

            print(f"Movido: {arquivo} -> {pasta_destino}")

if __name__ == "__main__":
    diretorio_alvo = input("Digite o diretório a ser organizado: ")
    organizar_arquivos(diretorio_alvo)
