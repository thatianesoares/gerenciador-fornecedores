import json

# Cores para o terminal
CORES = {
    "vermelho": "\033[91m",
    "verde": "\033[92m",
    "azul": "\033[94m",
    "reset": "\033[0m"
}


# Carregar dados do arquivo
def carregar_dados():
    try:
        with open("fornecedores.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []


# Salvar dados no arquivo
def salvar_dados(fornecedores):
    with open("fornecedores.json", "w") as arquivo:
        json.dump(fornecedores, arquivo, indent=4)


# Menu principal
def mostrar_menu():
    print(f"\n{CORES['azul']}=== GERENCIADOR DE FORNECEDORES ==={CORES['reset']}")
    print("1. Adicionar fornecedor")
    print("2. Listar fornecedores")
    print("3. Marcar como contatado")
    print("4. Remover fornecedor")
    print("5. Sair")
    return input("Escolha uma opção: ")


# Função principal
def main():
    fornecedores = carregar_dados()

    while True:
        opcao = mostrar_menu()

        # Adicionar fornecedor
        if opcao == "1":
            nome = input("\nNome do fornecedor: ")
            tipo = input("Tipo (material/serviço): ")
            fornecedores.append({
                "nome": nome,
                "tipo": tipo,
                "contatado": False
            })
            print(f"{CORES['verde']}Fornecedor adicionado!{CORES['reset']}")

        # Listar fornecedores
        elif opcao == "2":
            print(f"\n{CORES['azul']}=== LISTA DE FORNECEDORES ==={CORES['reset']}")
            for idx, fornecedor in enumerate(fornecedores, 1):
                status = f"{CORES['verde']}✔{CORES['reset']}" if fornecedor[
                    'contatado'] else f"{CORES['vermelho']}✖{CORES['reset']}"
                print(f"{idx}. {fornecedor['nome']} ({fornecedor['tipo']}) - Contatado: {status}")

        # Marcar como contatado
        elif opcao == "3":
            try:
                idx = int(input("\nNúmero do fornecedor: ")) - 1
                fornecedores[idx]['contatado'] = True
                print(f"{CORES['verde']}Status atualizado!{CORES['reset']}")
            except:
                print(f"{CORES['vermelho']}Erro: número inválido!{CORES['reset']}")

        # Remover fornecedor
        elif opcao == "4":
            try:
                idx = int(input("\nNúmero do fornecedor: ")) - 1
                fornecedor_removido = fornecedores.pop(idx)
                print(f"{CORES['verde']}{fornecedor_removido['nome']} removido!{CORES['reset']}")
            except:
                print(f"{CORES['vermelho']}Erro: número inválido!{CORES['reset']}")

        # Sair e salvar
        elif opcao == "5":
            salvar_dados(fornecedores)
            print(f"{CORES['azul']}\nDados salvos. Até logo! 👋{CORES['reset']}")
            break

        else:
            print(f"{CORES['vermelho']}Opção inválida! Tente novamente.{CORES['reset']}")


if __name__ == "__main__":
    main()
