from citacoes import obter_citacao_aleatoria, CITACOES

def exibir_menu():
    print("\n--- GERADOR DE CITAÇÕES ---")
    print("1. Gerar citação aleatória")
    print("2. Escolher por categoria")
    print("3. Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            try:
                citacao = obter_citacao_aleatoria()
                print(f"\n💡 \"{citacao}\"")
            except Exception as e:
                print(f"\nErro: {e}")
                
        elif opcao == "2":
            print(f"\nCategorias disponíveis: {', '.join(CITACOES.keys())}")
            cat = input("Digite a categoria desejada: ").strip()
            try:
                citacao = obter_citacao_aleatoria(cat)
                print(f"\n💡 \"{citacao}\"")
            except ValueError as e:
                print(f"\n⚠️ {e}")
                
        elif opcao == "3":
            print("\nAté logo!")
            break
        else:
            print("\n❌ Opção inválida.")

if __name__ == "__main__":
    main()