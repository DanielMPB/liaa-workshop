import secrets
import string

def main():
    print("=== SISTEMA DE ACESSO RESTRITO ===")
    
    # --- SISTEMA DE LOGIN SIMPLES ---
    # Simulando um ID de acesso para entrar no gerador
    user_id = input("Digite seu ID de desenvolvedor para acessar: ")
    
    if not user_id:
        print("Acesso negado. ID inválido.")
        return

    print(f"\nBem-vindo, {user_id}! Iniciando Gerador de Chaves...\n")

    # --- ETAPA 3: INTERAÇÃO INICIAL ---
    try:
        tamanho = int(input("Digite o comprimento da senha desejado: "))
    except ValueError:
        print("Erro: Por favor, digite um número inteiro.")
        return

    # --- ETAPA 1 & 2: LÓGICA DE GERAÇÃO (ESTRUTURA LINEAR) ---
    # Esta base é propensa a conflitos se alterada simultaneamente
    caracteres = string.ascii_lowercase + string.digits  # Etapa 1: minúsculas e números
    
    # Etapa 2: Adicionando complexidade
    caracteres += string.ascii_uppercase  # Letras Maiúsculas
    caracteres += string.punctuation      # Caracteres Especiais (!@#$%...)

    # Geração da sequência aleatória segura
    senha_gerada = ''.join(secrets.choice(caracteres) for _ in range(tamanho))

    print("\n--- CHAVE GERADA COM SUCESSO ---")
    print(f"Sua nova senha é: {senha_gerada}")
    print("--------------------------------\n")

if __name__ == "__main__":
    main()