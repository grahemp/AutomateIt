#
import bs4, urllib2
page = urllib2.urlopen("https://www.packtpub.com/packt/offers/free-learning")
soup = bs4.BeautifulSoup(page, "lxml")
#Making the soup
dotd = soup.find(class_="dotd-title")
print dotd.text.strip()
