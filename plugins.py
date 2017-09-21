# This program will read the list of UCD plugins and make note of new plugins
# or plugins that have a new version.
#

import bs4
import urllib2
import csv
import json

# infile = open("plugins.csv",'rt')
# outfile = open("plugins.csv",'wt')
# https://stackoverflow.com/questions/33858989/how-to-read-a-csv-into-a-dictionary-in-python

# pluginfile = open("plugin-list.csv","rt")
with open("plugin-list.csv", "rt") as pluginfile:
    reader = csv.reader(pluginfile)
    next(reader)
    results = dict(reader)

# print results


# writer = csv.writer(pluginfile)
# writer.writerow( ('Plugin Name', 'Version'))

page = urllib2.urlopen("https://developer.ibm.com/urbancode/plugins/ibm-urbancode-deploy/")
soup = bs4.BeautifulSoup(page, "lxml")

all_plugins = soup.find_all(class_="mix")
all_versions = soup.find_all(class_="plugin-version")
nu_plugins = len(all_plugins)
#for i in range(nu_plugins):
#    print "Plugin name" + all_plugins[i].text + "Plugin version" + all_versions[i].text

for plugin in all_plugins:
    # print plugin
    # plugin_span = plugin.span
    # print plugin.plugin-title
    version = "-"
    title = plugin.find(class_="plugin-title").text.encode('ascii','ignore').decode('ascii')
    #     title = plugin.find(class_="plugin-title").text
    # print plugin.find(class_="plugin-version")
    if plugin.find(class_="plugin-version"):
        version = plugin.find(class_="plugin-version").text

    if title in results:
        if version != results[title]:
            print "New Version for " + title + "  Old: " + results[title] + "  New: " + version
    else:
        print "not found"

    #stored-version = results[title]
    #if stored-version != version:
    #    print "new version!"

    # print title + ","  + version
    # writer.writerow( (title, version) )
    # print ""

# outfile.close()
