#!/usr/bin/env python3

import bs4 as bs
import urllib
from urllib import request

#abre o arquivo
xml = open('index.xml')

#instancia
soup  = bs.BeautifulSoup(xml, 'xml')

URL_PLAY = "http://play.google.com/store/apps/details?id="

print("app | sdkever | targetsdk | source | numDownloads")
#loop para percorrer todas as app 
for app in soup.findAll('application'):
    #pega o id da app. sempre sera a primeira linha id e sdkver
    id = app.get('id')
    
    url_app = URL_PLAY + id
    
    try:
        r = request.urlopen(url_app)
        soup_html = bs.BeautifulSoup(r.read(), 'html.parser')
        num_downloads = soup_html.find_all("div", attrs={"itemprop":"numDownloads"}) 
        # some app doesn't have numDownloads
        if num_downloads:
            source = app.source.string
            #loop para pegar todos os packages
            for pkg in app.findAll('package'):
                targetSdk = pkg.targetSdkVersion.string if pkg.targetSdkVersion!=None else ""
                print(id, "|", pkg.sdkver.string, "|", targetSdk, "|", source, "|", num_downloads[0].string)
    except urllib.error.HTTPError as e:
        pass
