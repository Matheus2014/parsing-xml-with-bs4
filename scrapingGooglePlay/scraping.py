import bs4 as bs
import urllib

id="org.berlin_vegan.bvapp"

content = urllib.urlopen("https://play.google.com/store/apps/details?id="+id).read()

soup  = bs.BeautifulSoup(content, 'html')
print "titulo | conteudo | "+id

for i in soup.find_all(class_="meta-info"):
	cont=i.find(class_="content")
	title=i.find(class_="title")
	if cont!=None and title!=None:
		print title.string, " | ", cont.string 
	else:	 
		print ""