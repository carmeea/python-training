import urllib
import pydoc

# linkk = 'http://example.com/ceva/ceva2.html'
# x= linkk.split('/')
# print(x)
# y=x[3]
# print(y)

dictionary = {'pufuleti cu sare': [('https://www.mega-image.ro/Dulciuri-si-snacks/Ciocolata/Batoane/Baton-de-ciocolata-cu-crema-de-rom-30g/p/28815', '100gr', 'calorii')], 'baton cu arahide': [('https://www.mega-image.ro/Dulciuri-si-snacks/Napolitane-biscuiti-si-prajituri/Prajituri-si-rulade/Prajitura-cu-lapte-30g/p/64686', '200gr', 'calorii mici')]}
def getSubcategory(subcategory):
    for val in (i[0] for i in dictionary.values()):
        link = val[0]
        segment = link.split('/')
        subcategory =  segment[4]
        return subcategory
    
