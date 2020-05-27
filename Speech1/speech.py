"""
Programa que pega um artigo na internet e o dircussa usando o gTTs
"""
import os
from newspaper import Article
from gtts import gTTS
import nltk

LISTA = ["s", "S"]


def speak(text):
    """ Gera o audio e salva"""

    global LISTA

    language = 'pt'
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save('read_article.mp3')  # Salva o em mp3
    res = str(input("Deseja escutar o audio [s/n]? "))
    if res in LISTA:
        return os.system("play /home/victormilhomem/PycharmProjects/Speech/read_article.mp3")
    return "O audio so foi salvo!"


def apagar_audio():
    """ Apaga o audio criado"""
    global LISTA
    audio = "read_article.mp3"

    res = str(input("Deseja apagar o audio [s/n]? "))
    if res in LISTA:
        return os.remove(audio)  # Apaga o audio
    return "Seu audio não foi apagado!"


def main():

    article = str(input("url: "))

    x = Article(article)
    x.download()  # Download do artigo
    x.parse()  # Analisa o artigo

    nltk.download('punkt')  # Download do punkt package
    x.nlp()  # Natural Language Processing
    mytext = x.text  # Pega o texto do artigo e guarda na variavel

    return speak(mytext)


if __name__ == "__main__":
    main()
    apagar_audio()
