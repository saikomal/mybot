from bs4 import BeautifulSoup
import requests


def get_news():
	url='http://indiatoday.intoday.in/section/120/1/top-stories.html'
	res=requests.get(url)
	
	while(res.status_code!=200):
		try:
			res=requests.get('url')
		except:
			pass

	soup=BeautifulSoup(res.text,'lxml')
	long_news = soup.find_all('h3', {'class': ''})
	heading_data = []
	for i in range(len(long_news)):
		heading_data.append(long_news[i].text)
	return heading_data
#	short_news=soup.find('ul',{'class':'topstr-list gap topmarging'}).find_all('a')
#	long_news=soup.find_all('h3',{'class':''})
	# return (short_news,long_news)



def short_news():
	return(get_news()[0])

def long_news():
	return(get_news())
