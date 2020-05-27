# speech
This program allows you to get an article url and will transform it into a speech
pip install newspaper
pip install gTTS

Need to import:
    import os
    from newspapper import Article
    from gtts import gTTS
    import nltk
    
if you are using windows you will need to change os.system("play /home/victormilhomem/PycharmProjects/Speech/read_article.mp3")
to os.system("start read_article.mp3")
