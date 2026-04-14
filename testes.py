from src.Application.Service.game_service import GameService


typed_name = input("Digite um jogo: ")
possiveis = GameService.get_slug_name(typed_name)

i = 0
if possiveis:
    print("Escolha uma das opções abaixo: ")
    for item in possiveis:
        print(f"""[{i}] {item["name"]} - {item["capa"]}""")
        i += 1

resposta = int(input("Digite sua escolha: "))

slug_name = GameService.get_game_by_slug_name(possiveis[resposta]["slug_name"])
print(slug_name)


registro_jogo = GameService.register_game(slug_name)