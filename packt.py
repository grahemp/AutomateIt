#
import bs4, urllib2
# import urllib2
page = urllib2.urlopen("https://www.packtpub.com/packt/offers/free-learning")
# myfile = open('page.html')
soup = bs4.BeautifulSoup(page, "lxml")
#Making the soup
# print "BeautifulSoup Object:", type(soup)
dotd = soup.find(class_="dotd-title")
# print(type(dotd))
print dotd.text.strip()
#book-title = dotd.text
#print book-title.strip()
#print "Book Title:", soup.find("class",{"id":"dotd-title"}).getText()
