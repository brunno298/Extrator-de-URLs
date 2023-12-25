import re
import sys

def extrair_urls(texto):
    # Expressão regular para extrair URLs
    padrao = re.compile(r'https?://\S+')

    # Encontrar todas as URLs no texto
    urls = padrao.findall(texto)

    # Remover duplicatas usando um conjunto (set)
    urls_unicas = list(set(urls))

    return urls_unicas

def salvar_urls_em_txt(arquivo, urls):
    # Salvar URLs em um arquivo de texto
    with open(arquivo, 'w') as arquivo_saida:
        for url in urls:
            arquivo_saida.write(url + '\n')

def ler_urls_de_txt(arquivo, encoding='utf-8'):
    # Ler URLs de um arquivo de texto
    try:
        with open(arquivo, 'r', encoding=encoding) as arquivo_entrada:
            texto = arquivo_entrada.read()
        return texto
    except (OSError, IOError) as e:
        return ''

def main():
    # Verificar se o nome do arquivo foi fornecido como argumento
    if len(sys.argv) < 2:
        print("Por favor, forneça o nome do arquivo como argumento.")
        sys.exit(1)

    # Nome do arquivo é o segundo argumento
    nome_arquivo = sys.argv[1]

    # Definir novas_urls dentro da função main
    novas_urls = [
        'https://novosite1.com',
        'https://novosite2.com',
        # Adicione mais URLs conforme necessário
    ]

    bloco_de_texto = ler_urls_de_txt(nome_arquivo)
    urls_encontradas = extrair_urls(bloco_de_texto)

    # Adicionar novas URLs e remover duplicatas
    urls_encontradas.extend(novas_urls)
    urls_unicas = list(set(urls_encontradas))

    # Salvar URLs únicas de volta no arquivo
    salvar_urls_em_txt(nome_arquivo, urls_unicas)

    for url in urls_unicas:
        print(url)

if __name__ == "__main__":
    main()
