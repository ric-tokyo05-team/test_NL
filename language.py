from janome.tokenizer import Tokenizer
 
t = Tokenizer()
tokens = t.tokenize(u'お台場で焼肉が食べたい')
for token in tokens:
    # 品詞を取り出し
    partOfSpeech = token.part_of_speech.split(',')[0]
    print(token)
    # if partOfSpeech == u'名詞':
    #     print(token.surface)
