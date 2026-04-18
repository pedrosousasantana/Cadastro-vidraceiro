vidros = []

def criar_vidro(): print("\n--- Cadastro de Vidro ---") nome = input("Nome do vidro: ") tipo = input("Tipo (temperado, comum, laminado): ") preco = float(input("Preço: "))

vidro = {
    "id": len(vidros) + 1,
    "nome": nome,
    "tipo": tipo,
    "preco": preco
}

vidros.append(vidro)
print("Vidro cadastrado com sucesso!\n")
def listar_vidros(): print("\n--- Lista de Vidros ---") if not vidros: print("Nenhum vidro cadastrado.\n") return

for v in vidros:
    print(f"ID: {v['id']} | Nome: {v['nome']} | Tipo: {v['tipo']} | Preço: R${v['preco']}")
print()
def atualizar_vidro(): listar_vidros() try: id_busca = int(input("Digite o ID do vidro que deseja atualizar: "))

    for v in vidros:
        if v["id"] == id_busca:
            print("Digite os novos dados:")
            v["nome"] = input("Novo nome: ")
            v["tipo"] = input("Novo tipo: ")
            v["preco"] = float(input("Novo preço: "))
            print("Vidro atualizado!\n")
            return

    print("ID não encontrado.\n")
except:
    print("Erro ao atualizar.\n")
def deletar_vidro(): listar_vidros() try: id_busca = int(input("Digite o ID do vidro que deseja deletar: "))

    for v in vidros:
        if v["id"] == id_busca:
            vidros.remove(v)
            print("Vidro removido com sucesso!\n")
            return

    print("ID não encontrado.\n")
except:
    print("Erro ao deletar.\n")
def menu(): while True: print("==== VIDRAÇARIA ====") print("1 - Cadastrar vidro") print("2 - Listar vidros") print("3 - Atualizar vidro") print("4 - Deletar vidro") print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        criar_vidro()
    elif opcao == "2":
        listar_vidros()
    elif opcao == "3":
        atualizar_vidro()
    elif opcao == "4":
        deletar_vidro()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida.\n")
menu()