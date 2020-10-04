def wordcount(filename):
    try:
        with open(filename) as file:
            reader = file.read()  

    except FileNotFoundError:
        print("O arquivo %s não existe!" %filename)
    
    else:
        words = reader.split()
        num_words = len(words)

        print("O numero de palavras no arquivo %s é aproximadamente %d!" %(filename, num_words))


wordcount('book_alice.txt')
wordcount('book_moby_dick.txt')
wordcount('book_the_republic.txt')
