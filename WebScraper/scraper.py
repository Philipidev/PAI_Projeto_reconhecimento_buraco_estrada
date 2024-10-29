import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Configurações
base_url = "https://www.istockphoto.com/br/fotos/buraco-de-estrada?page="
output_folder = "imagens_buracos"
num_paginas = 82  # Número de páginas a percorrer
url_base_imagem = "https://media.istockphoto.com/id/"

# Configuração do driver Selenium
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Executa o navegador em modo headless (sem janela)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver_path = "./chomeDriver/chromedriver.exe"  # Ajuste o caminho se necessário
driver = webdriver.Chrome(service=Service(driver_path), options=options)

# Criar pasta para salvar as imagens
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"Pasta '{output_folder}' criada para armazenar as imagens baixadas.")

# Função para baixar e salvar a imagem usando requests
def download_image(img_url, img_name):
    try:
        print(f"Baixando imagem: {img_url}")
        response = requests.get(img_url)
        if response.status_code == 200:
            with open(f"{output_folder}/{img_name}", "wb") as f:
                f.write(response.content)
            print(f"Imagem '{img_name}' salva com sucesso.")
        else:
            print(f"Erro ao baixar imagem '{img_name}'. Status: {response.status_code}")
    except Exception as e:
        print(f"Erro ao baixar imagem '{img_name}': {e}")

# Loop pelas páginas
for page in range(1, num_paginas + 1):
    url = f"{base_url}{page}"
    print(f"\nAcessando página {page}: {url}")
    
    driver.get(url)
    time.sleep(3)  # Espera para garantir que a página e os scripts JS carreguem completamente

    try:
        # Encontrar todas as imagens na página
        images = driver.find_elements(By.TAG_NAME, "img")
        print(f"Encontradas {len(images)} imagens na página {page}.")

        # Baixar cada imagem que contém a URL base desejada
        downloaded_images = 0
        for img in images:
            try:
                img_src = img.get_attribute("src")
                if img_src and url_base_imagem in img_src:
                    # Extraindo o nome da imagem a partir da URL
                    img_name = img_src.split("/")[-1].split("?")[0]
                    download_image(img_src, img_name)
                    downloaded_images += 1
            except Exception as e:
                print(f"Erro ao processar uma imagem na página {page}: {e}")
                
        print(f"{downloaded_images} imagens com a URL base '{url_base_imagem}' baixadas da página {page}.")

    except Exception as e:
        print(f"Erro ao acessar as imagens na página {page}: {e}")

    # Atraso entre as requisições para evitar bloqueio
    print("Aguardando 2 segundos antes de acessar a próxima página...")
    time.sleep(2)

print("Download de imagens concluído.")
driver.quit()
