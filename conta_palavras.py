# Atividade 20.2 P2 Linguagem de Programação - Omar Cunha Lopes
# Professor Messias R. Batista
# Construa um programa em que o usuário passe o nome do arquivo 
# e receba como resposta número inteiro referente a quantidade 
# de palavras dentro do arquivo.
# 
def wordcount(filename):
    try:
        with open(filename) as file:
            reader = file.read()  

    except FileNotFoundError:
        print("O arquivo %s não existe!" %filename)
    
    else:
        words = reader.split()
        num_words = len(words)

        print("O numero de palavras no arquivo %s é de %d aproximadamente!" %(filename, num_words))

# Conta as palavras dos três livros txt
wordcount('book_alice.txt')
wordcount('book_moby_dick.txt')
wordcount('book_the_republic.txt')
