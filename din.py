import mechanize
import re

br = mechanize.Browser()
#br.set_all_readonly(False)    # allow everything to be written to
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders =  [('User-agent', 'Firefox')] 	      	# [('User-agent', 'Firefox')]
url = 'http://www.dinamani.com/editorial/'
response = br.open(url)
html =  response.read()      # the text of the page
response1 = br.response()  # get the response again
html2 = response1.read()     # can apply lxml.html.fromstring()

replacements = dict()
c = '\<a href="(http:\/\/www\.dinamani\.com\/editorial.*.ece)"'
for link in br.links():
    #print link.url
    replacements[url] = re.findall(c, html)
print len(replacements)

