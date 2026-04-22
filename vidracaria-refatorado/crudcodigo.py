"""
CLI standalone para gerenciar vidros via terminal.
Útil para testes rápidos sem precisar subir o servidor Flask.
"""

vidros = []


def _proximo_id():
    """Retorna o próximo ID disponível (não reutiliza IDs deletados)."""
    return max((v["id"] for v in vidros), default=0) + 1


def criar_vidro():
    print("\n--- Cadastro de Vidro ---")
    nome = input("Nome do vidro: ").strip()
    tipo = input("Tipo (temperado, comum, laminado): ").strip()

    try:
        preco = float(input("Preço: ").replace(",", "."))
        if preco < 0:
            raise ValueError
    except ValueError:
        print("Preço inválido.\n")
        return

    vidro = {"id": _proximo_id(), "nome": nome, "tipo": tipo, "preco": preco}
    vidros.append(vidro)
    print("Vidro cadastrado com sucesso!\n")


def listar_vidros():
    print("\n--- Lista de Vidros ---")
    if not vidros:
        print("Nenhum vidro cadastrado.\n")
        return

    for v in vidros:
        print(f"ID: {v['id']} | Nome: {v['nome']} | Tipo: {v['tipo']} | Preço: R$ {v['preco']:.2f}")
    print()


def atualizar_vidro():
    listar_vidros()
    try:
        id_busca = int(input("Digite o ID do vidro que deseja atualizar: "))
    except ValueError:
        print("ID inválido.\n")
        return

    vidro = next((v for v in vidros if v["id"] == id_busca), None)
    if vidro is None:
        print("ID não encontrado.\n")
        return

    print("Digite os novos dados (Enter para manter o valor atual):")

    novo_nome = input(f"Novo nome [{vidro['nome']}]: ").strip()
    novo_tipo = input(f"Novo tipo [{vidro['tipo']}]: ").strip()
    novo_preco_str = input(f"Novo preço [{vidro['preco']:.2f}]: ").strip()

    if novo_nome:
        vidro["nome"] = novo_nome
    if novo_tipo:
        vidro["tipo"] = novo_tipo
    if novo_preco_str:
        try:
            novo_preco = float(novo_preco_str.replace(",", "."))
            if novo_preco < 0:
                raise ValueError
            vidro["preco"] = novo_preco
        except ValueError:
            print("Preço inválido, valor mantido.\n")
            return

    print("Vidro atualizado!\n")


def deletar_vidro():
    listar_vidros()
    try:
        id_busca = int(input("Digite o ID do vidro que deseja deletar: "))
    except ValueError:
        print("ID inválido.\n")
        return

    vidro = next((v for v in vidros if v["id"] == id_busca), None)
    if vidro is None:
        print("ID não encontrado.\n")
        return

    vidros.remove(vidro)
    print("Vidro removido com sucesso!\n")


def menu():
    while True:
        print("==== VIDRAÇARIA ====")
        print("1 - Cadastrar vidro")
        print("2 - Listar vidros")
        print("3 - Atualizar vidro")
        print("4 - Deletar vidro")
        print("0 - Sair")

        opcao = input("Escolha: ").strip()

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


if __name__ == "__main__":
    menu()
