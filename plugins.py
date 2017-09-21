# This program will read the list of UCD plugins and make note of new plugins
# or plugins that have a new version.

import bs4, urllib2
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
    version = ""
    title = plugin.find(class_="plugin-title").text
    # print plugin.find(class_="plugin-version")
    if plugin.find(class_="plugin-version"):
        version = plugin.find(class_="plugin-version").text
    print title + " : "  + version
    # print ""
