"""
Programa que pega um artigo na internet e o dircussa
"""
from newspaper import Article
import nltk
import pyttsx3


def speak(text):

    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


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

