import bs4 as bs

#abre o arquivo
xml = open('index.xml')

#instancia
soup  = bs.BeautifulSoup(xml, 'xml')

#loop para percorrer todas as app 
for i in soup.findAll('application'):
	#pega o id da app. sempre sera a primeira linha id e sdkver
	print i.get('id'), " | ", i.package.sdkver.string 
	#loop para pegar todos os packages
	for j in i.findAll('package'):
		a = j.targetSdkVersion
		#verifica se existe o targetSdkVersion no package
		if a is not None:
			#imprime o id da app e o targetSdkVersion
			print i.get('id'), " | ",a.string