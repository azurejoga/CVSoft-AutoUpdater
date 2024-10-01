# CVSoft-AutoUpdater
Automatize as atualizações do sistema CVSoft e dos módulos financeiros e contábeis da sua empresa com este utilitário.
### Atualizador Automático de Módulos CVSoft

---

#### **Visão Geral para não desenvolvedores**

Este programa foi criado para facilitar o processo de atualização dos sistemas financeiros e contábeis da CVSoft, como o **Sistema de Contabilidade**, **Contas a Pagar**, **Contas a Receber**, entre outros. Ele automatiza a tarefa de baixar e atualizar esses módulos diretamente do site da CVSoft, eliminando a necessidade de fazê-lo manualmente.

Com este programa, você faz login no site da CVSoft, escolhe o módulo que deseja atualizar, seleciona onde deseja salvar o arquivo, e pronto! O programa ainda pergunta se você quer executar o arquivo baixado imediatamente após o download, facilitando ainda mais o uso.

---

#### **Módulos Disponíveis para Download**

Aqui estão os módulos que o programa pode baixar automaticamente:

1. **Sistema de Contabilidade**: Para gestão contábil e relatórios financeiros.
2. **Sistema de Contas a Pagar (SCP)**: Para organizar as contas que precisam ser pagas pela empresa.
3. **Sistema de Contas a Receber (SCR)**: Para gerenciar os pagamentos a serem recebidos pela empresa.
4. **Sistema de Faturamento (SF)**: Para controle de vendas e emissão de notas fiscais.
5. **Sistemas de Livros Fiscais (SLF)**: Para manter registros fiscais conforme a legislação.
6. **Sistema Patrimonial (SP)**: Para controle dos bens da empresa, como imóveis e equipamentos.

Esses módulos podem ser atualizados facilmente com este programa, garantindo que você sempre tenha a versão mais recente.

---

#### **Como Funciona o Programa**

1. **Login no Site da CVSoft**:
   - O programa se conecta ao site da CVSoft automaticamente, utilizando seu nome de usuário e senha, que você deve inserir no código antes de executar o programa. Assim, não será necessário fazer login manualmente toda vez.

2. **Escolha do Módulo para Atualizar**:
   - Ele mostra uma lista com os módulos disponíveis para download. Basta escolher o número correspondente ao módulo desejado.

3. **Escolha da Pasta de Destino**:
   - Você pode escolher onde deseja salvar o arquivo baixado em seu computador. O programa abre uma janela para você selecionar a pasta.

4. **Download Automático**:
   - O programa realiza o download automaticamente e avisa quando concluir. Caso ocorra algum problema, como demora no site da CVSoft, você também será notificado.

5. **Executar o Arquivo**:
   - Após o download, o programa pergunta se você deseja executar o arquivo imediatamente. Se você aceitar, ele será aberto automaticamente.

---

#### **Importante para não desenvolvedores**

Para executar o programa, é necessário que o **Python 3.11 ou superior,** esteja instalado em seu computador, além de algumas bibliotecas essenciais. Você precisará das seguintes bibliotecas instaladas:

- `requests`: Para fazer o download dos arquivos.
- `wxPython`: Para a interface gráfica que facilita a escolha da pasta de destino.

Caso você ainda não tenha essas bibliotecas instaladas, pode fazer isso rodando os seguintes comandos no terminal (ou Prompt de Comando):

```bash
pip install requests
pip install wxpython
```

Também, você precisa abrir o arquivo.py Atualizador.py no bloco de notas e editar as seguintes linhas:

   ```python
   login_data = {
       'usuario': 'Seu-usuario-da-CVSoft',
       'senha': 'Sua-senha-da-CVSoft'
   }
   ```

Depois que tudo estiver instalado e preenchido,  o programa funcionará normalmente.

Se você não se sentir à vontade para fazer isso sozinho, ou se encontrar qualquer dificuldade, posso ajudar! Basta enviar um e-mail para **azurejoga@gmail.com**, que eu ficarei feliz em orientar.

---

#### **Visão Geral para Desenvolvedores**

Este programa é desenvolvido em Python e utiliza as bibliotecas `requests` para gerenciar as requisições HTTP e `wxPython` para fornecer uma interface gráfica simples para o usuário escolher a pasta de destino.

---

#### **Instruções para Desenvolvedores: Como Compilar e Distribuir o Programa**

Se você quiser compilar o programa para distribuí-lo como um executável `.exe` (para Windows), o **PyInstaller** é uma excelente ferramenta para isso. Aqui estão as instruções detalhadas:

1. **Defina o Usuário e Senha**:
   - Antes de compilar o programa, edite o arquivo `atualizador.py` para adicionar seu nome de usuário e senha nos campos corretos:

   ```python
   login_data = {
       'usuario': 'Seu-usuario',
       'senha': 'Sua-senha'
   }
   ```

2. **Instale o Python 3.11**:
   - Certifique-se de ter o Python 3.11 instalado no seu sistema, já que o programa foi construído nessa versão.

3. **Instale as Bibliotecas Necessárias**:
   - Execute os seguintes comandos para garantir que todas as bibliotecas necessárias estejam instaladas:

   ```bash
   pip install requests
   pip install wxpython
   pip install pyinstaller
   ```

4. **Compile o Programa**:
   - Para compilar o código em um executável `.exe`, execute o seguinte comando:

   ```bash
   pyinstaller --onefile atualizador.py
   ```

   Isso criará um único arquivo executável que pode ser encontrado na pasta `dist/` do seu projeto.

5. **Distribuição**:
   - Agora você pode distribuir o executável `.exe` para qualquer usuário. Ele não precisará instalar Python nem as bibliotecas, pois o arquivo gerado já contém tudo o que é necessário para rodar o programa.

---

#### **Conclusão**

Com este programa, os usuários poderão manter seus módulos da CVSoft sempre atualizados de forma rápida e automática, sem complicações. Para desenvolvedores, o processo de compilação é simples com o uso do PyInstaller, garantindo uma distribuição eficiente.

Se você tiver dificuldades para executar ou compilar o programa, não hesite em entrar em contato comigo pelo e-mail **azurejoga@gmail.com**, que estarei pronto para ajudar!