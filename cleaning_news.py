import re
import glob
import os

# 현재 디렉터리
CURRENT_DIRECTORY = os.path.join(os.getcwd(),'news')

 
# 클리닝 함수
def clean_text(text):
    cleaned_text = re.sub('[a-zA-Z]', '', text)
    cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"◇△ⓒ]',
                          '', cleaned_text)
    return cleaned_text

def main():
    for i in range(3,42):
        for news_file in glob.glob(os.path.join(CURRENT_DIRECTORY,str(i)+'*')):
            text=''
            with open(news_file,'r',encoding='utf-8') as filereader :
                text = clean_text(filereader.read())
            with open(news_file, 'w', encoding='utf-8') as filewriter:
                filewriter.write(text)
 
if __name__ == "__main__":
    main()
