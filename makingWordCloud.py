from konlpy.tag import Twitter
from collections import Counter
import pytagcloud

INPUT_FILE = 'news_cleaned.txt'
filereader = open(INPUT_FILE, 'r', newline='')
word_corpus = str(filereader.readlines())
filereader.close()

nouns_tagger = Twitter()
nouns = nouns_tagger.nouns(word_corpus)
count = Counter(nouns)

ranked_tags = count.most_common(40)
taglist = pytagcloud.make_tags(ranked_tags, maxsize=80)
pytagcloud.create_tag_image(taglist, 'wordcloud.jpg', size=(900, 600), fontname='NanumBarunGothic', rectangular=False)
