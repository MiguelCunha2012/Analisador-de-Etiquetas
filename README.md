# Tutorial: Analisador de Etiquetas de Pedido

## 🎯 O Que o Programa Faz?

Este programa é uma ferramenta de auditoria simples, projetada para analisar arquivos de texto (como os gerados por impressoras de etiqueta ou sistemas de logística).

O objetivo principal é:

1.  Você fornece um **número de pedido** (ex: `52139810`).
2.  Você indica um **arquivo `.txt`** para ser analisado (simplesmente arrastando o arquivo para a janela do programa).
3.  O programa lê o arquivo e procura por **todas as etiquetas sequenciais** daquele pedido (ex: `52139810/01`, `52139810/02`, `52139810/04`...).
4.  Ele identifica automaticamente qual deveria ser a etiqueta mais alta (no exemplo, `/04`) e verifica se todos os números de 1 até o mais alto estão presentes.
5.  Ao final, ele **gera um relatório** informando se a sequência está completa ou listando exatamente quais etiquetas estão faltando (ex: `52139810/03`).

> **Em resumo:** Ele garante que não falta nenhuma etiqueta de um pedido que foi dividido em múltiplos volumes.

---

> **Bem-vindo!** Este tutorial guia você para instalar e usar o programa. Siga os passos abaixo.

---

## 🐍 PARTE 1: Instalando o Python (Você só precisa fazer isso 1 vez)

O programa precisa de Python para funcionar. O instalador (`python-3.x.x.exe`) já deve estar nesta pasta para facilitar.

1.  **Encontre o instalador do Python:**
    Procure pelo arquivo na pasta com um nome parecido com `python-3.x.x.exe`. É o arquivo com o ícone da logo do Python.

2.  **Execute o instalador:**
    Dê um duplo-clique nele para começar a instalação.

3.  **‼️ PASSO MAIS IMPORTANTE!**
    Na primeira tela da instalação, **ANTES** de clicar em "Install Now", você **PRECISA** marcar a caixinha que fica na parte de baixo, escrita:

    > **[X] Add Python to PATH**

    Marcar esta opção é **OBRIGATÓRIO** para o programa funcionar.

    ![Exemplo da tela de instalação do Python com a opção 'Add Python to PATH' marcada](https://i.imgur.com/fNf5v2c.png)

4.  **Continue a Instalação:**
    Depois de marcar a caixa, clique em "Install Now" e espere o processo terminar. Pode demorar alguns minutos. Ao final, pode clicar em "Close".

Pronto! O Python está instalado e você não precisa mais se preocupar com ele.

---

## 🚀 PARTE 2: Como Executar o Programa

Nesta pasta, você verá um arquivo chamado `ExecutarAnalisador.bat`. Ele é o atalho para iniciar o programa.

1.  **Coloque seu arquivo de texto na pasta:**
    Certifique-se de que o arquivo `.txt` que você quer analisar esteja nesta mesma pasta.

2.  **Inicie o programa:**
    Dê um **duplo-clique no arquivo `ExecutarAnalisador.bat`**.

    Uma janela preta de terminal (Prompt de Comando) irá se abrir. Isso é normal. O programa começará a rodar dentro dela.

---

## 💻 PARTE 3: Usando o Analisador

O programa é interativo e vai te pedir algumas informações:

1.  **Digite o número do pedido:**
    Quando aparecer a mensagem `Digite o número do pedido a ser analisado:`, digite o número principal do pedido (ex: `52139810`) e aperte **Enter**.

2.  **Informe o arquivo de texto:**
    Depois, ele vai pedir: `Arraste o arquivo TXT para esta janela e aperte Enter:`.

    **Como fazer isso:**
    * Clique no seu arquivo `.txt` (sem soltar o botão do mouse).
    * Arraste o mouse para dentro da janela preta do programa.
    * Solte o botão do mouse. O caminho completo do arquivo vai aparecer escrito.
    * Aperte **Enter**.

3.  **Veja o Resultado:**
    O programa vai analisar tudo e mostrar o resultado:
    * ✅ **Se aparecer "SUCESSO!"**, significa que todas as etiquetas da sequência foram encontradas.
    * ❌ **Se aparecer "ATENÇÃO!"**, ele vai listar exatamente quais etiquetas estão faltando no arquivo.

4.  **Fazer uma nova consulta:**
    Ao final, o programa vai perguntar: `Deseja fazer uma nova consulta? (S/N):`
    * Digite `S` e aperte **Enter** para analisar outro pedido ou arquivo.
    * Digite `N` e aperte **Enter** para fechar o programa.

---

## ❔ PARTE 4: Dúvidas e Problemas Comuns

**P: A janela preta abre e fecha muito rápido!**
R: Isso geralmente acontece se o Python não foi instalado corretamente com a opção "Add Python to PATH" marcada. **Refaça a Parte 1** e garanta que marcou a caixinha.

**P: O programa diz "ARQUIVO NÃO ENCONTRADO!".**
R: Verifique se você arrastou o arquivo correto para a janela e se ele realmente existe no local que apareceu escrito. Tente arrastar o arquivo novamente.
