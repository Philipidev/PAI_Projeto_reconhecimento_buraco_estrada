# Projeto: Downloader de Imagens de Buracos de Estrada

Este projeto automatiza o download de imagens de buracos de estrada a partir do site iStockPhoto, acessando múltiplas páginas e salvando todas as imagens que contêm a URL base desejada (`https://media.gettyimages.com/id/`).

## Funcionalidades

- Acessa automaticamente cada página do site, de 1 a 82.
- Filtra imagens que contêm a URL base específica e as baixa para uma pasta local.
- Inclui um atraso entre requisições para evitar bloqueios pelo site.

## Pré-requisitos

1. **Python 3.x** - Certifique-se de que o Python 3 está instalado em seu sistema.
2. **Bibliotecas Python** - Listadas no arquivo `requirements.txt`. Para instalar:

   ```bash
   pip install -r requirements.txt
   ```

## Estrutura de Arquivos

- `script.py` - O script principal para download das imagens.
- `requirements.txt` - Lista as bibliotecas necessárias.
- `README.md` - Este arquivo, que explica o projeto.
- `imagens_buracos/` - Diretório onde as imagens baixadas serão salvas.

## Como Usar

1. Clone ou baixe este repositório.
2. Instale as dependências com o comando:

   ```bash
   pip install -r requirements.txt
   ```

3. Execute o script:

   ```bash
   py scraper.py
   ```

As imagens serão salvas na pasta `imagens_buracos`.

## Explicação do Script

- O script acessa cada página de 1 a 82 do site [iStockPhoto](https://www.istockphoto.com/br/fotos/buraco-de-estrada?page=1).
- Em cada página, ele verifica todas as tags `img` e filtra as URLs de imagem que contêm a URL base especificada.
- Cada imagem filtrada é baixada e salva no diretório `imagens_buracos` com seu nome original.

## Observações

- Este projeto utiliza um atraso de 2 segundos entre as requisições para evitar bloqueio do site.
- Caso o site ou a estrutura de URLs mudem, ajustes no código podem ser necessários.
  
## Licença

Este projeto é para uso pessoal e educacional.