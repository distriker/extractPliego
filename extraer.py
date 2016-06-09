#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
-- Extractor de datos de Pliego --
---- Para más información, leer el README ----
'''

from bs4 import BeautifulSoup as bs
from subprocess import call
from urllib2 import urlopen
from urllib import urlretrieve
import urlparse
import csv, os, re, sys, time

def extract(url, destino, urlI):
    ''' Acceso al sitio web '''
    soup = bs(urlopen(url), 'html.parser')
    parsed = list(urlparse.urlparse(url))
    ''' Descarga de las img. '''

    for img in soup.findAll(True, {'class':['list_logo']}):
        print "Guardando imagen..."
        print ">> %(src)s" % img
        imgUrl = urlparse.urljoin(url, img['src'])
        imgFile = img["src"].split("/")[-1]
        imgDir = os.path.join(destino, imgFile)
        urlretrieve(imgUrl, imgDir)
        with open(fileLink, 'a') as f:
            data = [urlI, imgUrl]
            f = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
            f.writerow(data)
            print "Link guardado"

    ''' Acceso a la descr. y escritura en el csv '''
    #description = soup.findAll(True, {'class':['description']})
    for text in soup.select(".description"):
        loteNum = text.contents[1]
        loteDat = text.contents[3]
        detalle = text.contents[6].strip()
        detalleE = detalle.encode("iso-8859-1")
        loteNumS = str(loteNum).lstrip("<b>i>").rstrip("</i>b>")
        loteDatS = str(loteDat).lstrip("<span>").rstrip("</span>")
        data = [urlI, loteNumS, loteDatS, detalleE]
        with open(fileData, 'a') as f:
            f = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
            f.writerow(data)
            tL = "\n-----------------------\n"
            print "\n>> " + urlI + " | Lote: " + loteNumS + " - " + loteDatS
            print "\n>> " + detalle + tL

def getUrl(opt, baseUrl):
    ''' "i" es cada una de las cifras del rango (1, 2, 3, 4...);
        "urlI es "i" convertido en cadena;
        "r" ceros anteriores a i para cada rango (esencial para el script);
        "url" es la suma de la url base más "r" e "i" '''
    path = "/img"
    destino = os.path.basename(path)
    optSel = int(input(opt))

    ''' Importante: en el hipotético caso de que la terminal se sobrecarge con
        los rangos 3, 4 y 5, estos se pueden reducir y repartir en más opciones;
        no es complicado '''
    # Primer rango: 00001 - 00009
    if optSel == 1:
        try:
            for i in range(1,10):
                r = str(0).zfill(4)
                urlI = r + str(i)
                url = baseUrl + r + urlI
                extract(url, destino, urlI)
        except ValueError:
            print "Introduce el rango correcto"
    # Segundo rang: 00010 - 00099
    elif optSel == 2:
        try:
            for i in range(10,100):
                r = str(0).zfill(3)
                urlI = r + str(i)
                url = baseUrl + r + urlI
                extract(url, destino)
        except ValueError:
            print "Introduce el rango correcto"
    # Tercero rango: 00100 - 00999
    elif optSel == 3:
        try:
            for i in range(100,1000):
                r = str(0).zfill(2)
                urlI = r + str(i)
                url = baseUrl + r + urlI
                extract(url, destino)
        except ValueError:
            print "Introduce el rango correcto"
    # Cuarto rango: 01000 - 09999
    elif optSel == 4:
        try:
            for i in range(1000,10000):
                r = str(0).zfill(1)
                urlI = r + str(i)
                url = baseUrl + r + urlI
                extract(url, destino)
        except ValueError:
            print "Introduce el rango correcto"
    # Quinto rango: 10000 - 18510
    elif optSel == 5:
        try:
            for i in range(10000,18510):
                urlI = r + str(i)
                url = baseUrl + urlI
                extract(url, destino)
        except ValueError:
            print "Introduce el rango correcto"
    elif optSel == 0:
        try:
            for i in range(0,10):
                r = str(0).zfill(4)
                urlI = r + str(i)
                url = baseUrl + r + urlI
                extract(url, destino)
                return i
            for i in range(10,100):
                r = str(0).zfill(3)
                urlI = r + str(i)
                url = baseUrl + r + urlI
                extract(url, destino)
            for i in range(100,1000):
                r = str(0).zfill(2)
                urlI = r + str(i)
                url = baseUrl + r + urlI
                extract(url, destino)
            for i in range(1000,10000):
                r = str(0).zfill(1)
                urlI = r + str(i)
                url = baseUrl + r + urlI
                extract(url, destino)
            for i in range(10000,18510):
                urlI = r + str(i)
                url = baseUrl + urlI
                extract(url, destino)
        except ValueError:
            print "Introduce el rango correcto"
    else:
        print "Algo ha salido mal"

if __name__ == "__main__":
    print "-- Extractor de imágenes y detalles de las fichas de Pliego\n"
    doc = raw_input("Introduce el nombre para el archivo (solo nombre, no extensión): ")
    ''' Introducción de la cabecera de datos '''
    fileData = 'datos/' + doc + '.csv'
    fileLink = 'datos/' + doc + '-links.csv'
    print 'Los datos extraídos se guardarán en ' + fileData
    print 'Los links de las imágenes en ' + fileLink
    conf = raw_input("Confirma para continuar ([S]í o [N]o): ")
    if conf == "s":
        with open(fileData, 'a') as f:
            desc = u'Descripci\u00F3n detallada'.encode("iso-8859-1")
            header = ['N. ficha', 'Lote', '"Rey"', desc]
            f = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
            f.writerow(header)
        ''' Inicio del proceso: obtención de la url:
            Recomiendo que no se cambie la "baseUrl" ya que el script está hecho
            especificamente para trabajar en ese sitio web. '''
        baseUrl = "http://subastas.numismaticaycoleccionismo.es/index/viewBatch/"
        getUrl("\nElige: 1 [00001 al 00010], 2 [00010 al 00099], \n       3 [00100 al 00999], 4 [01000 al 09999] o 5 [10000 al 18510]: ", baseUrl)
    elif conf == "n":
        print "Se reiniciará el script en 5 segundos...\n"
        time.sleep(5)
        reset = os.execv(__file__, sys.argv)
    else:
        print "Por favor, escriba s (sí) o n (no) para confirmar"
        print "Se reiniciará el script en 5 segundos...\n"
        time.sleep(5)
        reset = os.execv(__file__, sys.argv)
sys.exit('¡Fin de la extracción!\n')
