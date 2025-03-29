# Impime ANDARES de um Hotel usando Python

## Índice
1. [Descrição](#descrição)
2. [Como Usar](#como-usar)
3. [Exemplo de Saída Esperada](#exemplo-de-saída-esperada)
4. [Pré-Requisitos](#pré-requisitos)
5. [Contato e Network](#contatos-e-network)
6. [Contribua](#contribuições)
7. [Licença](#licença)


## Descrição

Este repositório contém um código simples em Python que tem como objetivo imprimir os números de andares de um prédio, começando do andar fornecido até o andar 1 excluindo o 13º andar, devido à superstição do proprietário.. A principal característica deste código é o uso de diferentes tipos de laços de repetição para demonstrar como eles funcionam no Python. O código implementa três abordagens para resolver o problema:

- **Laço `while`**: A primeira função usa o laço `while` tradicional, verificando se o andar é diferente de 13 antes de imprimi-lo e decrementando o valor do andar.
- **Laço `do-while`**: A segunda função implementa um laço similar ao `do-while`, onde a condição de parada é verificada após a execução do código.
- **Laço `for`**: A terceira função utiliza um laço `for` para iterar sobre os andares.

Esse exercício serve como estudo para o entendimento de laços de repetição e suas diferenças em Python.


## Como Usar

Para utilizar o script, siga as instruções abaixo:

1. **Clone o repositório**:
   Se você ainda não tem o repositório em sua máquina, clone-o utilizando o comando:
   ```bash
   git clone https://github.com/jacivaldocarvalho/imprime-andares-python.git
   ```

2. **Abra o arquivo `main.py`**:
   Dentro do diretório clonado, localize e abra o arquivo `imprime_andares.py` no seu editor de código preferido.

3. **Execute o script**:
   Caso tenha o Python instalado em sua máquina, você pode rodar o script diretamente via terminal/linha de comando:
   ```bash
   python imprime_andares.py
   ```

4. **Informe o número do andar**:
   O script está configurado para imprimir os andares a partir do andar 21, mas você pode alterar o valor diretamente na variável `andar` dentro da função `main()`.


## Exemplo de Saída Esperada

Ao rodar o script, o programa deve imprimir os andares, de 21 até 1, pulando o andar 13, utilizando três métodos diferentes. A saída será algo similar a:

```
Usando laço while:
21
20
19
18
17
16
15
14
12
11
10
9
8
7
6
5
4
3
2
1

Usando laço do while:
21
20
19
18
17
16
15
14
12
11
10
9
8
7
6
5
4
3
2
1

Usando laço for:
21
20
19
18
17
16
15
14
12
11
10
9
8
7
6
5
4
3
2
1
```


## Pré-Requisitos

Para executar o script, você precisará de:

- **Python 3.x**: O código foi desenvolvido e testado para Python 3. Certifique-se de que você tenha o Python 3 instalado na sua máquina.
  - Para verificar sua versão do Python, execute no terminal:
    ```bash
    python --version
    ```
  
Não há dependências adicionais ou bibliotecas externas necessárias para o funcionamento do script.


## Contribuições

Se você tiver sugestões de melhorias ou encontrar problemas com o script, sinta-se à vontade para abrir um **issue** ou submeter um **pull request**.

## Contatos e Network

Gostaria de trocar ideias, colaborar ou aprender mais sobre DevOps, Infraestrutura como Código e desenvolvimento de software? Fique à vontade para me contactar nas plataformas abaixo:

- **LinkedIn**: [LinkedIn](https://www.linkedin.com/in/jacivaldocarvalho/) 👔
- **E-mail**: [E-mail](mailto:jacivaldocarvalho@gmail.com) 📧
- **GitHub**: [GitHub](https://github.com/jacivaldocarvalho) 🐙
- **Medium**: [Medium](https://medium.com/@jacivaldocarvalho) ✍️

Sempre aberto a novas conexões e oportunidades de aprendizado!

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
