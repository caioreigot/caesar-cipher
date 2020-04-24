# Caesar Cipher / Cifra de César [Descriptografar/Criptografar/Brute Force]
# Programa feito por: [https://github.com/caiorodrgues]
# Obrigado por usar!

# Cores
GREEN = "\033[0;32m"
RED = "\033[1;31m"
BLUE  = "\033[1;34m"
BOLD = "\033[;1m"
RESET = "\033[0;0m"

def Descriptografar():

    try:
        temp = int(input(GREEN + "[!]" + RESET + " Digite a chave/rot: "))

        # É possível usar a operação "%" para isso, porém quis exemplificar melhor
        while temp > 26:
            temp = temp - 26
            rot = temp

        if temp <= 26:
            rot = temp
        
        print("")

    except:
        print(RED + "[!]" + RESET + " Só é aceito números como entrada para a chave")

    try:
        mensagem = input(GREEN + "[!]" + RESET + " Digite a mensagem criptografada: ")
    except:
        print(RED + "[!]" + RESET + " Ocorreu um erro com a leitura de sua mensagem") 
   
    # 'a' na posição ASCII = 97
    # 'A' na posição ASCII = 65
    # Diferença dos dois: 32
    # Alfabeto maiusculo em ASCII: 65 a 90
    # Alfabeto minusculo em ASCII: 97 a 122

    print(GREEN + "[!]" + RESET + " Mensagem descriptografada: ", end="")
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

    continuar = input("\n" + GREEN + "[!]" + RESET + " Tecle ENTER para voltar ao menu ou digite 'exit' para sair: ")
    continuar.lower()
    if continuar == "":
        Main()
    elif continuar == "exit":
        Sair()
    else:
        print(RED + "[!]" + RESET + " Comando inválido, voltando ao menu...")
        print("")
        Main()
 
def Criptografar():

    try:
        temp = int(input(GREEN + "[!]" + RESET + " Chave de criptografia: "))
        
        # É possivel usar a operação "%"
        while temp > 26:
            temp = temp - 26
            rot = temp

        if temp <= 26:
            rot = temp
        
        print("")

    except:
        print(RED + "[!]" + RESET + " Só é aceito números como entrada para a chave")
        print("")

    try:
        mensagem = input(GREEN + "[!]" + RESET + " Digite a mensagem: ")
    except:
        print(RED + "[!]" + RESET + " Ocorreu um erro com a leitura de sua mensagem")

    # 'a' na posição ASCII = 97
    # 'A' na posição ASCII = 65
    # Diferença dos dois: 32
    # Alfabeto maiusculo em ASCII: 65 a 90
    # Alfabeto minusculo em ASCII: 97 a 122

    print(GREEN + "[!]" + RESET + " Mensagem codificada: ", end="")
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

    continuar = input("\n" + GREEN + "[!]" + RESET + " Tecle ENTER para voltar ao menu ou digite 'exit' para sair: ")
    continuar.lower()
    if continuar == "":
        Main()
    elif continuar == "exit":
        Sair()
    else:
        print(RED + "[!]" + RESET + " Comando inválido, voltando ao menu...")
        print("")
        Main()

def BruteForce():

    print("")
    print(GREEN + '[!]' + RESET + ' Digite "help" para ver como usar')
    temp = input(GREEN + "[!]" + RESET + ' Escolha um range de chaves com um espaço entre os dois: ')
    temp.lower()
    if temp == 'help':
        print("")
        print(GREEN + "Como usar:" + RESET)
        print("É preciso inserir dois valores, e um espaço entre eles")
        print('Ex: "1 27" --> O programa irá te mostrar o resultado de cada chave de 1 a 27')
        BruteForce()
    else:

        # lista com o range das chaves/keys (range brute force)
        rangebf = []
        rangebf = temp.strip('').split(' ')
        if len(rangebf) != 2:
            print("")
            print(RED + "[!]" + RESET + " Insira um valor válido, digite help para ver como usar")
            BruteForce()
        else:
            rangekey = int(rangebf[1])

    # mensagem a ser usada pelo brute force
    try:
        mensagem = input("Digite a mensagem criptografada: ")
    except:
        print(RED + "[!]" + RESET + " Ocorreu um erro com a leitura de sua mensagem")

    print("")

    rotkey = int(rangebf[0])

    for key in range(rotkey, (rangekey + 1)):
        print('Descriptografando com a chave' + GREEN + f" {key}" + RESET + ": ", end="")
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

    continuar = input("\n" + GREEN + "[!]" + RESET + " Tecle ENTER para voltar ao menu ou digite 'exit' para sair: ")
    continuar.lower()
    if continuar == "":
        Main()
    elif continuar == "exit":
        Sair()
    else:
        print(RED + "[!]" + RESET + " Comando inválido, voltando ao menu...")
        print("")
        Main()

def Menu():

    print("")
    print(GREEN + "Caesar Cipher, por: caiorodrgues" + RESET)
    print("------------------------")
    print("|" + GREEN + " [1] " + RESET + "Criptografar     |")
    print("|" + GREEN + " [2] " + RESET + "Descriptografar  |")
    print("|" + GREEN + " [3] " + RESET + "Brute Force      |")
    print("|" + GREEN + " [4] " + RESET + "Sair             |")
    print("------------------------")
    print("")

def Main():

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
            print(RED + "[!]" + RESET + " Digite um número válido (1, 2, 3 ou 4)")

    if escolha == 1:
        Criptografar()

    elif escolha == 2:
        Descriptografar()

    elif escolha == 3:
        BruteForce()
    
    elif escolha == 4:
    	Sair()

def Sair():
    print("")
    print(GREEN + "[!]" + RESET + " Obrigado por usar! Saindo...")
    print("")
    exit()

# Depois da leitura de todo o arquivo, o programa chama a função Main()
Main()
