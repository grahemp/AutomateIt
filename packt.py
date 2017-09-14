#
import bs4, urllib2

def checkforbook():
    booklist = file('mybooks.txt')
    found = False
    for line in booklist:
        if dotd.text.strip() in line:
            found = True
            break

    return found

page = urllib2.urlopen("https://www.packtpub.com/packt/offers/free-learning")
soup = bs4.BeautifulSoup(page, "lxml")
#Making the soup
dotd = soup.find(class_="dotd-title")
print dotd.text.strip()

# if dotd.text.strip() in open('list.txt').read():
#     print "Already have this one!"
gotit = checkforbook()
if gotit:
    print "I have this one."
else:
    print "This is a new one!"
