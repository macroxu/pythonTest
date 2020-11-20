#----导入spacy
#
import spacy
from collections import Counter


enDocExample='your There are moments in life when you miss someone so much that you just want to pick them from your dreams and hug them for real! Dream what you want to dream;go where you want to go;be what you want to be,because you have only one life and one chance to do all the things you want to do.'
enDocExample=enDocExample.replace(';',',')


#---parse doc 
#spacy 加载英文模型
nlp=spacy.load('en_core_web_sm')
doc=nlp(enDocExample)

#获取 unpunctuaction和unspace,unstopword
words=[token.lemma_ for token in doc if not token.is_punct |token.is_space |token.is_stop ]
print(words)

#对单词进行统计
words_stats=Counter(words);
print(words_stats)



