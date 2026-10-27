def calcular_media(notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)

def verificar_situacao(media):
    ##Critério: Média 7.0 para aprovação
    return "Aprovado" if media >= 7.0 else "Reprovado"

def exibir_menu(): # Moved outside 'verificar_situacao' and aligned
    print("\n--- SISTEMA DE GESTÃO DE NOTAS ---")
    print("1. Cadastrar Aluno e Notas")
    print("2. Listar Alunos e Média")
    print("3. Buscar aluno")
    print("4. Sair")
    return input("Escolha uma opção: ") # Fixed "opcção" to "opção"

def executar_sistema():
    ##Banco de dados em memória (Dicionário)
    ##Estrutura: {"Nome do Aluno": [nota1, nota2, ...]}
    alunos = {}

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            nome = input("Digite o nome do Aluno: ").strip()
            if not nome:
                print("Nome inválido!")
                continue

            try:
                qtd_notas = int(input(f"Quantas notas deseja inserir para {nome}? "))
                notas = []
                for i in range(qtd_notas):
                    nota = float(input(f"Digite a nota {i+1}: ")) # Fixed 'intput' to 'input'
                    if 0 <= nota <= 10:
                        notas.append(nota)
                    else:
                        print("Nota inválida! Digite um valor entre 0 e 10.")
                        break
                else: # This 'else' belongs to the 'for' loop, executes if loop completes without break.
                    alunos[nome] = notas
                    print(f"Aluno {nome} cadastrado com sucesso!") # Fixed "cadstrado" to "cadastrado"
            except ValueError:
                print("Entrada inválida. Certifique-se de digitar números para as notas.")
            except Exception as e:
                print(f"Ocorreu um erro: {e}")

        elif opcao == "2": # Listar Alunos e Média
            print("\n--- RELATÓRIO GERAL ---")
            if not alunos:
                print("Nenhum aluno cadastrado ainda.")
            else:
                for nome_aluno, notas_aluno in alunos.items():
                    media_aluno = calcular_media(notas_aluno)
                    situacao_aluno = verificar_situacao(media_aluno) # Fixed semantic error: pass media
                    print(f"Aluno: {nome_aluno} | Notas: {notas_aluno} | Média: {media_aluno:.2f} | Situação: {situacao_aluno}")

        elif opcao == "3": # Buscar aluno (original option 2)
            nome_busca = input("Digite o nome do aluno que busca: ").strip() # Fixed "alumo" to "aluno"
            if nome_busca in alunos:
                notas_busca = alunos[nome_busca]
                media_busca = calcular_media(notas_busca)
                situacao_busca = verificar_situacao(media_busca)
                print(f"\nAluno Encontrado: {nome_busca}")
                print(f"Notas: {notas_busca}")
                print(f"Média Final: {media_busca:.2f}")
                print(f"Situação: {situacao_busca}")
            else:
                print("Aluno não encontrado no sistema.")

        elif opcao == "4": # Sair (original option 3)
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

##Inicia o programa
if __name__ == "__main__": # Fixed 'if__name__' and colon
    executar_sistema()
