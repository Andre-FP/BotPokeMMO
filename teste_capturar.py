from functions.Functions import *


reconhecimento = 5
print("Pokemon shiny encontrado!")

erro = KillNonShinyHorde(reconhecimento)
if erro != OK:
    print("\n\nErro", erro)

erro = FalseSwipeHorde(reconhecimento, pp=30)                    
if erro != OK:
    print("\n\nErro", erro)

confirmacao = POKEMON_NAO_CAPTURADO
while confirmacao == POKEMON_NAO_CAPTURADO:
    erro = LancarPokebola(qntdPokebolas=50)
    if erro != OK:
        print("\n\nErro", erro)
    confirmacao = VerificarPokemonCapturado(manter_pokemon=True)

Teclado(t_ESC)
RegisterShiny(FOUND_SHINY_FILE)
time.sleep(3)
Teclado(t_SweetScent)


print("Testando lançar pokebola...")
confirmacao = POKEMON_NAO_CAPTURADO
while confirmacao == POKEMON_NAO_CAPTURADO:
    erro = LancarPokebola(qntdPokebolas=2)
    if erro != OK:
        print("\n\nErro", erro)
    
    confirmacao = VerificarPokemonCapturado(manter_pokemon=True)
Teclado(t_ESC)
RegisterShiny(FOUND_SHINY_FILE)
time.sleep(3)
Teclado(t_SweetScent)