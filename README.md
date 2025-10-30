Projeto: Calculadora de Maior Número (Python)

Este é um projeto simples em Python que pede ao usuário dois números inteiros e determina qual deles é o maior.

O principal objetivo deste projeto é demonstrar as boas práticas de desenvolvimento de software, separando a lógica de negócio (o cálculo) da interface do usuário para permitir a criação de testes unitários robustos.

---

Estrutura do Projeto

O projeto é dividido em dois arquivos principais:

1.  calculadora_max.py
    * Contém a lógica de negócio isolada na função encontrar_maior().
    * Contém a função rodar_programa_principal() que lida com a interação do usuário e o tratamento de erros.

2.  test_calculadora_max.py
    * Contém a suíte de testes unitários que valida a função encontrar_maior().
    * Os testes cobrem múltiplos cenários, incluindo números positivos, negativos, iguais e o zero.

---

Como Usar
1. Executar o Programa Principal

Para executar o programa e interagir com ele no terminal:
python calculadora_max.py
