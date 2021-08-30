import requests
import time
from bs4 import BeautifulSoup


inputFile = open("input.txt", 'r', encoding='UTF-8')
# inputFileKeyword = open("Keyword.txt", 'r', encoding='UTF-8')


outputFileURL = open("outputURL.txt", 'w', encoding='UTF-8')
outputFileTitle = open("outputTitle.txt", 'w', encoding='UTF-8')
# outputTitleFill = open("outputTitleFill.txt", 'w', encoding='UTF-8')
# titleFill = ''


def main(URL):
	# openning our output file in append mode

	# specifying user agent, You can use other user agents
	# available on the internet
    HEADERS = ({'User-Agent':
				'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)	Chrome/44.0.2403.157 Safari/537.36',
								'Accept-Language': 'en-US, en;q=0.5'})

	# Making the HTTP Request
    try:
        webpage = requests.get(URL, headers=HEADERS)
    except:
        print("Link lỗi! Skip link" , i , '\n')
        outputFileTitle.write('Link lỗi' + '\n')
        outputFileURL.write('Link lỗi' + '\n')
        return

	# Creating the Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "lxml")

	# retreiving product title
    try:
		# Outer Tag Object
        title = soup.find("span",
						attrs={"id": 'productTitle'})
        
		# Inner NavigableString Object
        title_value = title.string

		# Title as a string value
        title_string = title_value.strip()
        

        outputFileTitle.write(title_string + '\n')
        print("Đã lấy title link", i , '\n')
        # titleFill = title_string

    except AttributeError:
        print("Lỗi không nhận đc title, đang chạy lại!")
        main(URL)
        

data = inputFile.readlines()
# keyword = inputFileKeyword.read()
# keyword = keyword.split(',')


i = 1
for line in data:
    titleFill = ''
    print('Đang chạy link ', i)
    url = line[0:line.find('/B0')+11]
    outputFileURL.write( url + '\n')
    print('Đã rút gọn link ', i)
    main(url)
    # for key in keyword:
    #     if key.isspace(): 
    #         break
    #     key = key.strip()
    #     result = titleFill.find(key)
    #     while result != -1:
    #         titleFill = titleFill.replace(key,'')   
    #         result = titleFill.find(key)
    #     outputTitleFill.write(titleFill + '\n')
    i += 1

inputFile.close()   
outputFileURL.close()
outputFileTitle.close()
# outputTitleFill.close()

input('Hoàn tất! Tắt hoặc enter để thoát chương trình!')