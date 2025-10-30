# -*- coding: utf-8 -*-

def encontrar_maior(num1, num2):
    """
    Recebe dois números (int ou float) e retorna o maior deles.
    """
    if num1 >= num2:
        return num1
    else:
        return num2
def rodar_programa_principal():
    """
    Função principal para interagir com o usuário.
    """
    try:
        numero1 = int(input("Escreva o primeiro número: "))
        numero2 = int(input("Escreva o segundo número: "))
        
        maior = encontrar_maior(numero1, numero2)
        
        if numero1 == numero2:
            print("Os números são iguais. O valor é:", maior)
        else:
            print("O maior número é:", maior)
            
    except ValueError:
        print("Erro: Você deve digitar um número inteiro válido.")

if __name__ == "__main__":
    rodar_programa_principal()
