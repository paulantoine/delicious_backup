# Copyright (c) 2017 Paul-Antoine Nguyen

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import requests
from bs4 import BeautifulSoup
import string
from dateutil.parser import parse
import time

base_url = 'https://del.icio.us/'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
# fill username and userpassword...
username =...
userpassword = ...
auth = (username,userpassword)
bookmark_file_header = """<!DOCTYPE NETSCAPE-Bookmark-file-1>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<!-- This is an automatically generated file.
It will be read and overwritten.
Do Not Edit! -->
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>
<DL><p>"""



def print_links(page):
	url = base_url + username + '?&page='+ str(page)
	r = requests.get(url, headers=headers, auth=auth)
	c = r.content
	soup = BeautifulSoup(c, "lxml")
	for div in soup.find_all("div", "articleThumbBlockOuter"):
		link_title = div.find("h3").get_text()
	
		div_infopan = div.find("div","articleInfoPan")
		link_url = div_infopan.find("a").get("href")
		date_string = div_infopan.find_all("p")[2].get_text()
		position = date_string.rfind("paulantoine")
		link_date_string = date_string[position+14:]
		link_date = str(int(parse(link_date_string).timestamp()))
	
		div_descr = div.find("div", "thumbTBriefTxt")

		link_tags = []
		if div_descr.find("ul"):
			for li in div_descr.find("ul").find_all("li"):
				link_tags.append(li.get_text())

		link_comment = ""	
		for p in div_descr.find_all("p"):
			link_comment += p.get_text()

		text = '<DT><A HREF="' + link_url + '" ADD_DATE="'+ link_date +'" PRIVATE="0" TAGS="' + ",".join(link_tags) + '">' + link_title + '</A>'
		print(text)
	
		if link_comment != "" :
			print('<DD>'+link_comment)
		

print(bookmark_file_header)
for p in range(1,276):
	print_links(p)
	time.sleep(1)
print("</DL><p>")
	
