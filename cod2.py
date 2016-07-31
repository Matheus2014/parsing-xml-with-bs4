import untangle

obj = untangle.parse('index.xml')

print obj.application['id']