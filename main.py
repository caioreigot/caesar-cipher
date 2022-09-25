import os
from utils.Menu import Menu
import utils.Colors as c

def limparConsole():
    os.system('cls') if os.name == 'nt' else os.system('clear')

def Descriptografar():
    print(f"{c.GREEN}> Descriptografar{c.RESET}\n")

    try:
        temp = int(input(f"{c.GREEN}[!]{c.RESET} Digite a chave/rot: "))

        # É possível usar a operação "%" para isso, porém quis exemplificar melhor
        while temp > 26:
            temp = temp - 26
            rot = temp

        if temp <= 26:
            rot = temp
        
        print("")

    except:
        print(f"{c.RED}[!]{c.RESET} Só é aceito números como entrada para a chave")

    try:
        mensagem = input(f"{c.GREEN}[!]{c.RESET} Digite a mensagem criptografada: ")
    except:
        print(f"{c.RED}[!]{c.RESET} Ocorreu um erro com a leitura de sua mensagem") 
  
    # 'a' na posição ASCII = 97
    # 'A' na posição ASCII = 65
    # Diferença dos dois: 32
    # Alfabeto maiusculo em ASCII: 65 a 90
    # Alfabeto minusculo em ASCII: 97 a 122

    print(f"{c.GREEN}[!]{c.RESET} Mensagem descriptografada: ", end="")
    
    for elem in mensagem:
        if elem == " ":
            print(" ", end="")

        elif (ord(elem) <= ord('Z')) and (ord(elem) >= ord('A')):
            temp = (ord(elem) - rot)

            # Possível usar a operação "%"
            if temp < 65:
                while temp < 65:
                    temp = (ord(elem) - rot) + 26
                    somaascii = temp
                print(chr(somaascii), end="")
            else:
                print(chr(ord(elem) - rot), end="")

        elif (ord(elem) <= ord('z')) and (ord(elem) >= ord('a')):
            temp = (ord(elem) - rot)

            # Possível usar a operação "%"
            if temp < 97:
                while temp < 97:
                    temp = (ord(elem) - rot) + 26
                    somaascii = temp
                print(chr(somaascii), end="")
            else:
                print(chr(ord(elem) - rot), end="")

        # Caso a palavra tenha um acento
        else:
            print(elem, end="")

    print("")

    continuar = input("\n" + f"{c.GREEN}[!]{c.RESET} Tecle ENTER para voltar ao menu ou digite 'exit' para sair: ")
    continuar.lower()
    if continuar == "":
        Main()
    elif continuar == "exit":
        Sair()
    else:
        print(f"{c.RED}[!]{c.RESET} Comando inválido, voltando ao menu...\n")
        Main()

def Criptografar():
    print(f"{c.GREEN}> Criptografar{c.RESET}\n")

    try:
        temp = int(input(f"{c.GREEN}[!]{c.RESET} Chave de criptografia: "))
        
        # É possivel usar a operação "%"
        while temp > 26:
            temp = temp - 26
            rot = temp

        if temp <= 26:
            rot = temp
        
        print("")

    except:
        print(f"{c.RED}[!]{c.RESET} Só é aceito números como entrada para a chave\n")

    try:
        mensagem = input(f"{c.GREEN}[!]{c.RESET} Digite a mensagem: ")
    except:
        print(f"{c.RED}[!]{c.RESET} Ocorreu um erro com a leitura de sua mensagem")

    # 'a' na posição ASCII = 97
    # 'A' na posição ASCII = 65
    # Diferença dos dois: 32
    # Alfabeto maiusculo em ASCII: 65 a 90
    # Alfabeto minusculo em ASCII: 97 a 122

    print(f"{c.GREEN}[!]{c.RESET} Mensagem codificada: ", end="")
    for elem in mensagem:
        if elem == " ":
            print(" ", end="")

        elif (ord(elem) <= ord('Z')) and (ord(elem) >= ord('A')):
            temp = (ord(elem) + rot)

            # É possível usar a operação "%" para isso, porém quis exemplificar melhor
            if temp > 90:
                while temp > 90:
                    temp = (ord(elem) + rot) - 26
                    somaascii = temp
                print(chr(somaascii), end="")
            else:
                print(chr(ord(elem) + rot), end="")

        elif (ord(elem) <= ord('z')) and (ord(elem) >= ord('a')):
            temp = (ord(elem) + rot)

            # É possível usar a operação "%" para isso, porém quis exemplificar melhor
            if temp > 122:
                while temp > 122:
                    temp = (ord(elem) + rot) - 26
                    somaascii = temp
                print(chr(somaascii), end="")
            else:
                print(chr(ord(elem) + rot), end="")
        # Caso a palavra tenha um acento
        else:
            print(elem, end="")

    print("")

    continuar = input("\n" + f"{c.GREEN}[!]{c.RESET} Tecle ENTER para voltar ao menu ou digite 'exit' para sair: ")
    continuar.lower()
    if continuar == "":
        Main()
    elif continuar == "exit":
        Sair()
    else:
        print(f"{c.RED}[!]{c.RESET} Comando inválido, voltando ao menu...\n")
        Main()

def BruteForce():
    print(f"{c.GREEN}> BruteForce{c.RESET}\n")

    print(f"{c.GREEN}[!]{c.RESET}" + ' Digite "help" para ver como usar')
    temp = input(f"{c.GREEN}[!]{c.RESET} Escolha um range de chaves com um espaço entre os dois: ")
    temp.lower()
    if temp == 'help':
        print(f"\n{c.GREEN}Como usar:{c.RESET}")
        print("É preciso inserir dois valores, e um espaço entre eles")
        print('Ex: "1 27" -> O programa irá te mostrar o resultado de cada chave de 1 a 27')
        BruteForce()
    else:
        # lista com o range das chaves/keys (range brute force)
        rangebf = []
        rangebf = temp.strip('').split(' ')
        if len(rangebf) != 2:
            print("")
            print(f"{c.RED}[!]{c.RESET} Insira um valor válido, digite help para ver como usar")
            BruteForce()
        else:
            rangekey = int(rangebf[1])

    # mensagem a ser usada pelo brute force
    try:
        mensagem = input("Digite a mensagem criptografada: ")
    except:
        print(f"{c.RED}[!]{c.RESET} Ocorreu um erro com a leitura de sua mensagem")

    print("")

    rotkey = int(rangebf[0])

    for key in range(rotkey, (rangekey + 1)):
        print(f"Descriptografando com a chave{c.GREEN}" + f" {key}{c.RESET}: ", end="")
        for elem in mensagem:
            temp = key
            # É possível usar a operação "%" para isso, porém quis exemplificar melhor
            while temp > 26:
                temp = temp - 26
                rot = temp

            if temp <= 26:
                rot = temp

            if elem == " ":
                print(" ", end="")

            elif (ord(elem) <= ord('Z')) and (ord(elem) >= ord('A')):
                temp = (ord(elem) - rot)

                # É possível usar a operação "%" para isso, porém quis exemplificar melhor
                if temp < 65:
                    while temp < 65:
                        temp = (ord(elem) - rot) + 26
                        somaascii = temp
                    print(chr(somaascii), end="")
                else:
                    print(chr(ord(elem) - rot), end="")

            elif (ord(elem) <= ord('z')) and (ord(elem) >= ord('a')):
                temp = (ord(elem) - rot)

                # É possível usar a operação "%" para isso, porém quis exemplificar melhor
                if temp < 97:
                    while temp < 97:
                        temp = (ord(elem) - rot) + 26
                        somaascii = temp
                    print(chr(somaascii), end="")
                else:
                    print(chr(ord(elem) - rot), end="")
            # Caso a palavra tenha um acento
            else:
                print(elem, end="")

        print("\n", end="")

    print("")

    continuar = input("\n" + f"{c.GREEN}[!]{c.RESET} Tecle ENTER para voltar ao menu ou digite \"exit\" para sair: ")
    continuar.lower()
    if continuar == "":
        Main()
    elif continuar == "exit":
        Sair()
    else:
        print(f"{c.RED}[!]{c.RESET} Comando inválido, voltando ao menu...\n")
        Main()

def Main():
    limparConsole()

    Menu()
    escolha = 0

    while True:
        try:
            escolha = int(input("Digite a opção desejada: "))
        except:
            print("Insira um número válido")
            
        if (escolha in [1, 2, 3, 4]):
            break
        else:
            print(f"{c.RED}[!]{c.RESET} Digite um número válido (1, 2, 3 ou 4)")

    match escolha:
        case 1:
            Criptografar()
        case 2:
            Descriptografar()
        case 3:
            BruteForce()
        case 4:
            Sair()

def Sair():
    print(f"\n{c.GREEN}[!]{c.RESET} Obrigado por usar! Saindo...\n")
    exit()

Main()