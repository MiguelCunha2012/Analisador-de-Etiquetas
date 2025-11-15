import re
import os
import sys

def analisar_etiquetas(pedido_base, texto_completo):
    """
    Analisa um texto em busca de todas as etiquetas sequenciais de um pedido
    e retorna as que estiverem faltando. (Esta função não muda)
    """
    etiquetas_encontradas_str = re.findall(f"{pedido_base}/(\\d+)", texto_completo)
    
    if not etiquetas_encontradas_str:
        return [], 0 

    etiquetas_encontradas = {int(num) for num in etiquetas_encontradas_str}

    maior_etiqueta = max(etiquetas_encontradas)
    etiquetas_esperadas = set(range(1, maior_etiqueta + 1))
    etiquetas_faltantes = sorted(list(etiquetas_esperadas - etiquetas_encontradas))

    return etiquetas_faltantes, maior_etiqueta

# --- LOOP PRINCIPAL DO PROGRAMA ---

while True: # Adicionamos um loop infinito que só será quebrado quando o usuário quiser sair

    # Limpa a tela para a nova consulta (funciona em Windows, Mac e Linux)
    os.system('cls' if os.name == 'nt' else 'clear') 

    print("--- Analisador de Etiquetas de Pedido ---")
    print("Para sair, basta responder 'N' na pergunta final.\n")

    # 1. Pergunta qual o número do pedido
    numero_do_pedido = input("Digite o número do pedido a ser analisado: ")

    # 2. Pede pelo arquivo TXT
    caminho_do_arquivo = ""
    while True:
        caminho_do_arquivo = input("Arraste o arquivo TXT para esta janela e aperte Enter: ").strip()

        # Limpa aspas que o Windows adiciona ao arrastar
        if caminho_do_arquivo.startswith('"') and caminho_do_arquivo.endswith('"'):
            caminho_do_arquivo = caminho_do_arquivo[1:-1]

        # Verifica se o arquivo existe antes de continuar
        if os.path.isfile(caminho_do_arquivo):
            break 
        else:
            print("\n!!! ARQUIVO NÃO ENCONTRADO !!! Por favor, tente novamente.\n")

    # 3. Lê o conteúdo do arquivo e executa a análise
    try:
        with open(caminho_do_arquivo, 'r', encoding='utf-8') as f:
            conteudo_do_arquivo = f.read()
        
        faltantes, total_esperado = analisar_etiquetas(numero_do_pedido, conteudo_do_arquivo)
        
        # 4. Exibe o resultado de forma clara
        print("-" * 45)
        print(f">> RESULTADO DA ANÁLISE")
        print(f"   Pedido: {numero_do_pedido}")
        print(f"   Arquivo: {os.path.basename(caminho_do_arquivo)}")
        print(f"   Total de etiquetas na sequência: {total_esperado}")
        print("-" * 45)

        if not faltantes:
            print("\n✅ SUCESSO! Todas as etiquetas sequenciais estão presentes!\n")
        else:
            print(f"\n❌ ATENÇÃO! {len(faltantes)} etiqueta(s) não foram encontradas:")
            for num in faltantes:
                print(f"  - {numero_do_pedido}/{num:02d}")
            print() # Apenas uma linha em branco para espaçamento

    except Exception as e:
        print(f"\n!!! Ocorreu um erro ao processar o arquivo: {e}\n")

    # 5. Pergunta se o usuário quer continuar
    print("-" * 45)
    nova_consulta = input("Deseja fazer uma nova consulta? (S/N): ")
    
    # Se a resposta NÃO for 's' ou 'sim', o loop é interrompido
    if nova_consulta.lower() not in ['s', 'sim']:
        break # Sai do "while True" e o programa termina

print("\nAnalisador finalizado. Obrigado por usar!")
# Pequena pausa antes de fechar a janela se o script .bat for usado
import time
time.sleep(2)