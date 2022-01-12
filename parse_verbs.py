import lxml.etree as etree
doc = etree.parse('apertium-krc-eng.krc-eng.dix')
nodes = doc.xpath('//s[@n="v"]')
print(etree.tostring(nodes[2]))