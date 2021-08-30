# # importing libraries
# from bs4 import BeautifulSoup
# import requests

# def main(URL):
# 	# openning our output file in append mode

# 	# specifying user agent, You can use other user agents
# 	# available on the internet
# 	HEADERS = ({'User-Agent':
# 				'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)	Chrome/44.0.2403.157 Safari/537.36',
# 								'Accept-Language': 'en-US, en;q=0.5'})

# 	# Making the HTTP Request
# 	webpage = requests.get(URL, headers=HEADERS)

# 	# Creating the Soup Object containing all data
# 	soup = BeautifulSoup(webpage.content, "lxml")

# 	# retreiving product title
# 	try:
# 		# Outer Tag Object
# 		title = soup.find("span",
# 						attrs={"id": 'productTitle'})

# 		# Inner NavigableString Object
# 		title_value = title.string

# 		# Title as a string value
# 		title_string = title_value.strip().replace(',', '')

# 	except AttributeError:
# 		title_string = "NA"

# 	# saving the title in the file
# 	File.write(title_string + '\n')

# 	# retreiving price
# 	try:
# 		price = soup.find(
# 			"span", attrs={'id': 'priceblock_ourprice'}).string.strip().replace(',', '')
# 		# we are omitting unnecessary spaces
# 		# and commas form our string
# 	except AttributeError:
# 		price = "NA"
# 	print("Products price = ", price)

# 	# saving
# 	File.write(f"{price},")

# 	# retreiving product rating
# 	try:
# 		rating = soup.find("i", attrs={
# 						'class': 'a-icon a-icon-star a-star-4-5'}).string.strip().replace(',', '')

# 	except AttributeError:

# 		try:
# 			rating = soup.find(
# 				"span", attrs={'class': 'a-icon-alt'}).string.strip().replace(',', '')
# 		except:
# 			rating = "NA"
# 	print("Overall rating = ", rating)

# 	File.write(f"{rating},")

# 	try:
# 		review_count = soup.find(
# 			"span", attrs={'id': 'acrCustomerReviewText'}).string.strip().replace(',', '')

# 	except AttributeError:
# 		review_count = "NA"
# 	print("Total reviews = ", review_count)
# 	File.write(f"{review_count},")

# 	# print availiblility status
# 	try:
# 		available = soup.find("div", attrs={'id': 'availability'})
# 		available = available.find("span").string.strip().replace(',', '')

# 	except AttributeError:
# 		available = "NA"
# 	print("Availability = ", available)

# 	# saving the availibility and closing the line
# 	File.write(f"{available},\n")

# 	# closing the file
# 	File.close()


# if __name__ == '__main__':
# # openning our url file to access URLs
# 	File = open('output.txt', 'w', encoding='utf-8')
# 	main('https://www.amazon.com/gp/product/B094LYBT52?pf_rd_r=3BQ2XGES1VCT264EXTJA&pf_rd_p=6fc81c8c-2a38-41c6-a68a-f78c79e7253f&pd_rd_r=8ee34fa6-470e-40ca-8166-ccb8886ba700&pd_rd_w=fETf0&pd_rd_wg=yvj4W&ref_=pd_gw_unk&customId=B0752XJYNL&th=1')

title = 'Pitbull Dog Resting Pit Face Cute Vintage Pitbull Lovers T-Shirt'
keyword = ['T-Shirt']

for key in keyword:
	result = title.find(key)
	while result != -1:
		title = title.replace(key,'')
		result = title.find(key)


