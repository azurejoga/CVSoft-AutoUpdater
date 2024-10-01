import requests
import os
import wx

# Dados de login
login_data = {
    'usuario': 'Seu-usuario',
    'senha': 'Sua-senha'
}

# URLs dos downloads
urls = {
    '1. Sistema de contabilidade': 'https://cvsoft.com.br/download.asp?sistema=SC&tipo=atualiza',
    '2. Sistema de contas a pagar': 'https://cvsoft.com.br/download.asp?sistema=SCP&tipo=atualiza',
    '3. Contas a receber': 'https://cvsoft.com.br/download.asp?sistema=SCR&tipo=atualiza',
    '4. Sistema de faturamento': 'https://cvsoft.com.br/download.asp?sistema=SF&tipo=atualiza',
    '5. Sistemas de livros fiscais': 'https://cvsoft.com.br/download.asp?sistema=SLF&tipo=atualiza',
    '6. Sistema patrimonial': 'https://cvsoft.com.br/download.asp?sistema=SP&tipo=atualiza'
}

# Função para realizar o login
def fazer_login():
    # Iniciar uma sessão
    with requests.Session() as session:
        # Enviar solicitação POST com os dados de login para autenticar
        login_response = session.post("https://cvsoft.com.br/login.asp", data=login_data)
        
        # Verificar se o login foi bem-sucedido (código de status 200 indica sucesso)
        if login_response.status_code == 200:
            print("Login efetuado com sucesso.")
            return session
        else:
            print("Falha no login.")
            return None

# Função para baixar o arquivo selecionado
def baixar_arquivo(session, url, nome_arquivo):
    if session is not None:
        # Obter o diretório de destino do usuário
        destino = obter_destino()

        if destino:
            # Baixar o arquivo
            print(f"Baixando o arquivo {nome_arquivo}, aguarde...")
            download_response = session.get(url)
            
            # Verificar se o download foi bem-sucedido
            if download_response.status_code == 200:
                # Obter o nome do arquivo do cabeçalho Content-Disposition, se estiver presente
                content_disposition = download_response.headers.get('Content-Disposition')
                if content_disposition:
                    filename = content_disposition.split('filename=')[1].strip('"')
                else:
                    # Se o cabeçalho Content-Disposition não estiver presente, use um nome de arquivo padrão
                    filename = f"{nome_arquivo}.extensao"
                
                # Salvar o conteúdo do arquivo no diretório selecionado pelo usuário
                with open(os.path.join(destino, filename), "wb") as file:
                    file.write(download_response.content)
                    
                print(f"Arquivo {nome_arquivo} baixado com sucesso em {destino}.")

                # Perguntar ao usuário se deseja executar o arquivo
                resposta = input("Deseja executar o arquivo? (S/N): ").strip().upper()
                if resposta == 'S':
                    os.startfile(os.path.join(destino, filename))
            else:
                print(f"Falha ao baixar o arquivo {nome_arquivo}. Código de status: {download_response.status_code}")

# Função para obter o diretório de destino do usuário usando wxPython
def obter_destino():
    app = wx.App(None)
    dialog = wx.DirDialog(None, "Selecione a pasta de destino", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
    if dialog.ShowModal() == wx.ID_OK:
        destino = dialog.GetPath()
        dialog.Destroy()
        return destino
    else:
        dialog.Destroy()
        return None

# Realizar o login antes de exibir os arquivos disponíveis para download
session = fazer_login()

# Se o login for bem-sucedido, permitir que o usuário escolha qual arquivo baixar
if session is not None:
    while True:
        print("\nEscolha o arquivo que deseja baixar:")
        for nome_arquivo, _ in urls.items():
            print(nome_arquivo)
        print("0. Sair")
        
        escolha = input("Digite o número correspondente ao arquivo ou 0 para sair: ")
        
        if escolha == '0':
            print("Saindo...")
            break
        elif escolha in [str(i) for i in range(1, len(urls) + 1)]:
            nome_arquivo_escolhido = list(urls.keys())[int(escolha) - 1]
            url_escolhida = list(urls.values())[int(escolha) - 1]
            baixar_arquivo(session, url_escolhida, nome_arquivo_escolhido)
        else:
            print("Escolha inválida. Por favor, digite um número válido.")
