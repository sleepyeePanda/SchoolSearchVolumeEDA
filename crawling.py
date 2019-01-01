from bs4 import BeautifulSoup
import urllib.request
 
# 출력 파일
OUTPUT_FILE_NAME = 'news.txt'
# 크롤링할 URL
URL = 'http://www.cctoday.co.kr/?mod=news&act=articleView&idxno=1163002'
 
 
# 크롤링 함수
def get_text(URL):
    source_code_from_URL = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_URL, 'html.parser', from_encoding='utf-8')
    text = ''
    for item in soup.find_all('div', id='adiContents'):
        text = text + str(item.find_all(text=True))
    return text
 
 
# 메인 함수
def main():
    open_output_file = open(OUTPUT_FILE_NAME, 'w')
    result_text = get_text(URL)
    open_output_file.write(result_text)
    open_output_file.close()
    
 
if __name__ == '__main__':
    main()