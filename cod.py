#!/usr/bin/env python2

import bs4 as bs

#abre o arquivo
xml = open('index.xml')

#instancia
soup  = bs.BeautifulSoup(xml, 'xml')

print "app | sdkever | targetsdk"
#loop para percorrer todas as app 
for app in soup.findAll('application'):
    #pega o id da app. sempre sera a primeira linha id e sdkver
    id = app.get('id')
    #loop para pegar todos os packages
    for pkg in app.findAll('package'):
        targetSdk = pkg.targetSdkVersion.string if pkg.targetSdkVersion!=None else ""
        print id, "|", pkg.sdkver.string, "|", targetSdk
