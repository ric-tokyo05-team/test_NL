#coding :utf-8
from janome.tokenizer import Tokenizer
 
t = Tokenizer()
tokens = t.tokenize(u'表参道でカフェ行きたい！')
for token in tokens:
    # 品詞を取り出し
    partOfSpeech = token.part_of_speech.split(',')[0]
    print(token)
    # if partOfSpeech == u'名詞':
    #     print(token.surface)
