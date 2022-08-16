from Scripts import BotMagikarpShiny, OK
import os 
import time
import click


@click.command()
@click.option("--aberto", prompt='Jogo está logado? y/n', type=str, default="y",
    help="Indica se o jogo está aberto ou não")
@click.option("--cadastrar", default=False, type=bool,
    help="Indica se está rodando para cadastrar novas posicoes ou para encontrar o shiny")
def ShinyHuntMagikarp(aberto, cadastrar):
    '''
    Faz shiny hunt de magikarp na cidade de Sootopolis em Hoenn.
    É necessário ter pokemons com surf, fly, teleport e um pokemon para 
    usar false swipe caso encontre um shiny.

    OBS: Apertar Ctrl + C quando quiser parar o programa.
    '''
    
    if aberto == "n" or aberto == "N":
        aberto = False
    else:
        aberto = True

    print("Em 5 segundos o bot começará...")
    time.sleep(5)
    
    erro = BotMagikarpShiny(aberto, cadastrar)
    if erro != OK:
        print ("Erro #", erro, sep="")
    os.system("PAUSE")
    return erro

if __name__ == "__main__":
    ShinyHuntMagikarp()
