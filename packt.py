#
import bs4, urllib2, sys
# import sys
reload(sys)
sys.setdefaultencoding('utf8')

def checkforbook():
    # this function will open the file with the list of books
    # and search through the list.
    # If the book is found (in other words, I have that book)
    # it returns True 
    # if not found, it returns false.
    
    booklist = file('mybooks.txt')
    found = False
    for line in booklist:
        # print line
        if dotdTitle in line:
            found = True
            break
    return found


page = urllib2.urlopen("https://www.packtpub.com/packt/offers/free-learning")
soup = bs4.BeautifulSoup(page, "lxml")

#Making the soup
dotd = soup.find(class_="dotd-title")
dotdTitle = dotd.text.strip()
# print dotd.text.strip()
print "The name of the free book for todday is: " + dotdTitle

# if dotd.text.strip() in open('list.txt').read():
#     print "Already have this one!"
gotit = checkforbook()
if gotit:
    print "I have this one."
else:
    print "This is a new one!"

#