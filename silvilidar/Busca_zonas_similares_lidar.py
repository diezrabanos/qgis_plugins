import numpy as np
import matplotlib.pyplot as plt
import os

import processing
import webbrowser
    


carpeta="d:/pruebas/lidar/veinte23/"

os.makedirs(carpeta, exist_ok=True)


mapcanvas = iface.mapCanvas()

#capa vectorial 
layers = mapcanvas.layers()
layervectorial=qgis.utils.iface.activeLayer()
feats = [ feat for feat in layervectorial.getFeatures() ]#[ feat for feat in layers[0].getFeatures() ]


#raster layer
capas_raster_de_interes=['HM','HBC','LC','RC','FCC']

#para sacar las estadisticas de todos los poligonos juntos
def simplificar_lista(lista):
    listanueva=[]
    for elemento in lista:
        if type(elemento)==list:
            for element in elemento:
                if type(element)==list:
                    for elemen in element:
                        if type(elemen)==list:
                            pass
                        else:
                            listanueva.append(elemen)
                else:
                    listanueva.append(element)
        else:
            listanueva.append(elemento)
    return listanueva
    
def estadisticas_lista(lista,coeficiente):
    estadisticos=[np.size(lista),np.mean(lista),np.std(lista)]
    rango=[np.mean(lista)-coeficiente*np.std(lista),np.mean(lista)+coeficiente*np.std(lista)]
    """print('TOTAL-------N Pixels: {} Media: {:.2f} Desviacion Estandar: {:.2f}'.format(np.size(lista), np.mean(lista), np.std(lista)))
    print("Rango de valores objetivo entre ---------{:.2f} y {:.2f}---------".format(rango[0],rango[1]))"""
    return rango,estadisticos

def crea_tabla(datos):
    texto = '<table class="default">'
    texto += ' <tr> \
    <th scope="row">Datos de la muestra</th> \
    <th>media</th> \
    <th>desviacion estandar</th> \
    </tr>'
    n = 1
    for dato in datos[1]:
        texto += '<tr> \
                 <th > Parcela {} </th> \
                 <td > {} </' \
                 'td> \
                 <td > {} </td> \
                 </tr >'.format(n, round(dato[0],1), round(dato[1],1))
        n = n + 1
    if len(datos[1]) > 0:
        #print('meter los datos finales con la media y desviacion estandar total')
        texto += '<tr> \
                         <th > Todas las parcelas </th> \
                         <td > {} </' \
                 'td> \
                 <td > {} </td> \
                 </tr >'.format(round(np.mean(simplificar_lista(datos[0])),1),round(np.std(simplificar_lista(datos[0])),1)) # meter la media y desviacion media del conjunto de datos.
    texto += '</table>'
    return texto

def grafica_histograma(datos, intervalo_min, intervalo_max, nombre):
    fig, ax = plt.subplots()
    ax.hist(datos, 10)  # np.arange(0,np.amax(datos)))
    ax.axvline(intervalo_min, color='red', linestyle='dashed', linewidth=1)
    ax.axvline(intervalo_max, color='red', linestyle='dashed', linewidth=1)
    #plt.show()
    plt.savefig(carpeta+nombre+'.png')
    return carpeta+nombre+'.png'



def crea_html(lista_elementos, lista_tablas,lista_graficas):
    texto = '<head>\
    <title>Estadisticos de la Muestra</title>\
     <meta name="keywords" content="EstadÃ­sticos de la muestra">\
     <meta name="description" content="Resumen de datos estadÃ­sticos de la muestra">\
     <meta name="Author" content="Javi">\
     <style>\
        table {\
  table-layout: fixed;\
  width: 80%;\
  border-collapse: collapse;\
  border: 3px solid black;\
}\
thead th:nth-child(1) {\
  width: 30%;\
}\
thead th:nth-child(2) {\
  width: 20%;\
}\
thead th:nth-child(3) {\
  width: 15%;\
}\
thead th:nth-child(4) {\
  width: 35%;\
}\
th, td {\
  padding: 20px;\
}\
th, td {\
   width: 25%;\
   text-align: left;/\
   vertical-align: top;\
   border: 1px solid ;\
   border-collapse: collapse;\
   padding: 0.3em;\
   caption-side: bottom;\
}\
     </style>\
    <script>\
    </script>\
    </head> \
    <body><h1>DATOS DE LAS MUESTRAS</h1>'
    n = 0
    if len(lista_elementos) > 0:
        for i in range(0, len(lista_elementos)):
            texto += '<h2>{} </h2> \
                     {}  \
                     <br>\
                     <img src={}>'.format(lista_elementos[i], lista_tablas[i],lista_graficas[i])
            n = n + 1
    texto += '</body></html>'
    archivo_html=open(carpeta+"Datos_Muestra.html","w") 
    archivo_html.write(texto) 
    archivo_html.close() 
    webbrowser.open_new(carpeta+"Datos_Muestra.html")
    #return texto


def filtro_raster_intervalo(nombre_raster,intervalo):
    for layer in iface.mapCanvas().layers():
        if layer.type() == QgsMapLayer.RasterLayer and layer.name()== nombre_raster:
            rlayer=layer
            #intervalo=[min,max]
            
            minimo=intervalo[0]
            #print(minimo)
            maximo=intervalo[1]
            entries = []
            input_raster = rlayer#QgsRasterLayer('D:\pruebas\lidar\leon\HM.vrt', 'raster') #rlayer#QgsRasterLayer('path/to/your/input/raster', 'raster')      
            output_raster = "D:/pruebas/lidar/"+nombre_raster+"filtro.tif"#"D:/pruebas/lidar/mi_capa6.tif"
            # Define band1
            layer1 = QgsRasterCalculatorEntry()
            layer1.ref = 'layer1@1'
            layer1.raster = rlayer
            layer1.bandNumber = 1
            entries.append( layer1 )
 
            calc = QgsRasterCalculator('(layer1@1 > '+str(minimo)+ ' AND layer1@1 < '+str(maximo)+') ', 
                            output_raster, 
                            'GTiff', 
                            rlayer.extent(), 
                            rlayer.width(), 
                            rlayer.height(), 
                            entries )
                             
            calc.processCalculation()
            nuevalayer= QgsRasterLayer(output_raster,nombre_raster.lower()+"_filtro")
            #QgsProject.instance().addMapLayers([nuevalayer])
            return nuevalayer


def multiplica_rasters(rlayer1,rlayer2,rlayer3,rlayer4,rlayer5):
    entries = []    
    output_raster = carpeta+"multilpicado.tif"#"D:/pruebas/lidar/mi_capa6.tif"
    # Define band1
    layer1 = QgsRasterCalculatorEntry()
    layer1.ref = 'layer1@1'
    layer1.raster = rlayer1
    layer1.bandNumber = 1
    entries.append( layer1 )
    # Define band2
    layer2 = QgsRasterCalculatorEntry()
    layer2.ref = 'layer2@1'
    layer2.raster = rlayer2
    layer2.bandNumber = 1
    entries.append( layer2 )
    # Define band3
    layer3 = QgsRasterCalculatorEntry()
    layer3.ref = 'layer3@1'
    layer3.raster = rlayer3
    layer3.bandNumber = 1
    entries.append( layer3 )
    # Define band4
    layer4 = QgsRasterCalculatorEntry()
    layer4.ref = 'layer4@1'
    layer4.raster = rlayer4
    layer4.bandNumber = 1
    entries.append( layer4 )
    # Define band5
    layer5 = QgsRasterCalculatorEntry()
    layer5.ref = 'layer5@1'
    layer5.raster = rlayer5
    layer5.bandNumber = 1
    entries.append( layer5 )

    calc = QgsRasterCalculator('(layer1@1 * layer2@1 * layer3@1 * layer4@1 * layer5@1 )',   output_raster,  'GTiff',    rlayer1.extent(),     rlayer1.width(),                     rlayer1.height(),                     entries )            
    calc.processCalculation()
    nuevalayer= QgsRasterLayer(output_raster,"multiplicado")
    QgsProject.instance().addMapLayers([nuevalayer])
    return nuevalayer


def vectorizar(raster,salida):
    parameters = {'INPUT': raster.source(),'BAND': 1, 'EXTRA' : '', 'FIELD': "DN",  'EIGHT_CONNECTEDNESS':False, 'OUTPUT': carpeta+'vectorizado.shp'}
    processing.run("gdal:polygonize",parameters)#.runAndLoadResults("gdal:polygonize",parameters)
    #seleciono lo que me interesa
    lyr=QgsVectorLayer(carpeta+'vectorizado.shp',"nombre","ogr")
    #hago una selecion de los elementos con dn=1, anado la informacion a la tabla y creo una capa nueva  ojo deberia hacer una funcion para emplearlo mas veces. 
    layer = lyr #iface.activeLayer()
    expression = QgsExpression( u'"DN" = 1' )
    context = QgsExpressionContext()
    scope = QgsExpressionContextScope()
    context.appendScope(scope)
    layer = lyr
    feats=[]
    ids=[]
    for feat in layer.getFeatures():
        scope.setFeature(feat)
        result = expression.evaluate(context)
        if result:
            feats.append(feat)
            ids.append(feat.id())
            #areas.append(feat.geometry().area() )
    if len(ids)>0:
        #exporto la seleccion
        layer.selectByIds(ids)
        output_path=carpeta+"vectorial2.shp"
        
        QgsVectorFileWriter.writeAsVectorFormat(layer, output_path, "CP120", layer.crs(), "ESRI Shapefile", onlySelected=True)
        lyr2=QgsVectorLayer(output_path,"vectorial2","ogr")
        #QgsProject.instance().addMapLayer(lyr2)
        #simplifico 
        #calcula la superficie de esta capa pero no la refresca.
        layer=QgsVectorLayer(output_path,"poligonos","ogr")
        provider = layer.dataProvider()
        areas = [ feat.geometry().area()  for feat in layer.getFeatures() ]
        indice = [ feat.id()  for feat in layer.getFeatures() ]
        field = QgsField("area", QVariant.Int)
        provider.addAttributes([field])
        layer.updateFields()
        idx = layer.fields().indexFromName('area')
        long=len(indice)
        i=0
        while i<long:
            new_values = {idx : float(areas[i])}
            provider.changeAttributeValues({indice[i]:new_values})
            i=i+1           
        layer.updateFields()

        #selecciono las teselas mayor de una superficie dada.
        #hago una selecion de los elementos con dn=1, anado la informacion a la tabla y creo una capa nueva  ojo deberia hacer una funcion para emplearlo mas veces. 
        expression = QgsExpression( u'"area" > 1000')
        context = QgsExpressionContext()
        scope = QgsExpressionContextScope()
        context.appendScope(scope)
        feats=[]
        ids=[]
        for feat in layer.getFeatures():
            scope.setFeature(feat)
            result = expression.evaluate(context)
            if result:
                feats.append(feat)
                ids.append(feat.id())
                #areas.append(feat.geometry().area() )
        if len(ids)>0:
            lyr2.selectByIds(ids)
            ruta_vectorial3=carpeta+"vectorial3.shp"
            output_path=ruta_vectorial3
            QgsVectorFileWriter.writeAsVectorFormat(lyr2, output_path, "CP120", lyr.crs(), "ESRI Shapefile", onlySelected=True)
            lyr3=QgsVectorLayer(ruta_vectorial3,"Zonas similares","ogr")
            QgsProject.instance().addMapLayer(lyr3)
    if len(ids)==0:
        print('no hay nada seleccionado')


def agrega(rlayer):
    #suavizado 
    parametros={ 'INPUT' : rlayer.source(), 'METHOD' : 0, 'MODE' : 1, 'RADIUS' : 4, 'RESULT' : carpeta+"suavizado.sdat" }      
    suavizado=processing.run('saga:simplefilter', parametros)['RESULT']
    rlayer1=QgsRasterLayer(suavizado,"suavizado")
    QgsProject.instance().addMapLayers([rlayer1])
    #filtrado
    entries = []
    layer1 = QgsRasterCalculatorEntry()
    layer1.ref = 'layer1@1'
    layer1.raster = rlayer1
    layer1.bandNumber = 1
    entries.append( layer1 )
    #mayor de umbral
    output_raster=carpeta+"suavizado_seleccionado.tif"
    calc = QgsRasterCalculator('(layer1@1 > 0.2 )',   output_raster,  'GTiff',    rlayer1.extent(),     rlayer1.width(),                     rlayer1.height(),                     entries )
    calc.processCalculation()
    rlayer2=QgsRasterLayer(output_raster,"suavizado_seleccionado")
    QgsProject.instance().addMapLayers([rlayer2])
    #suavizado2
    parametros={ 'INPUT' : rlayer2.source(), 'METHOD' : 0, 'MODE' : 1, 'RADIUS' : 2, 'RESULT' : carpeta+"suavizado2.sdat" }      
    suavizado2=processing.run('saga:simplefilter', parametros)['RESULT']
    rlayer3=QgsRasterLayer(suavizado2,"suavizado2")
    QgsProject.instance().addMapLayers([rlayer3])
    #filtrado2
    entries = []
    layer2 = QgsRasterCalculatorEntry()
    layer2.ref = 'layer2@1'
    layer2.raster = rlayer3
    layer2.bandNumber = 1
    entries.append( layer2 )
    #mayor de umbral
    output_raster=carpeta+"suavizado_seleccionado2.tif"
    calc = QgsRasterCalculator('(layer2@1 > 0.5 )',   output_raster,  'GTiff',    rlayer3.extent(),     rlayer3.width(),                     rlayer3.height(),                     entries )
    calc.processCalculation()
    rlayer4=QgsRasterLayer(output_raster,"suavizado_seleccionado2")
    QgsProject.instance().addMapLayers([rlayer4])
    return rlayer4


def saca_valores_raster(nombre_raster,feats):
    #print('empiezo saca valores raster')
    resultado=[] # lista con todos los valores
    resumen=[] #lista con la media y desviacion de cada parcela.
    for layer in iface.mapCanvas().layers():
        if layer.type() == QgsMapLayer.RasterLayer and layer.name()== nombre_raster:
            rlayer=layer
            #saco puntos
            xsize = rlayer.rasterUnitsPerPixelX()
            ysize = rlayer.rasterUnitsPerPixelY()
            provider = rlayer.dataProvider()
            points = []
            values = [ [] for i in range(len(feats)) ]
            print (" ")
            print ("Sacando Datos...")
            print (nombre_raster)
            for k, feat in enumerate(feats):
                extent = feat.geometry().boundingBox()
                xmin = extent.xMinimum()
                ymax = extent.yMaximum()
                xmax = extent.xMaximum()
                ymin = extent.yMinimum()
     
                rows = int((ymax - ymin)/ysize)
                cols = int((xmax - xmin)/xsize)
                #print(rows)
                #print(cols)
     
                x = xmin
                y = ymax
     
                geom_feat = feat.geometry()
     
                for i in range(rows+1):
                    for j in range(cols+1):
                        pt = QgsPointXY(x,y)
                        tmp_pt = QgsGeometry.fromPointXY(pt)
                        if tmp_pt.within(geom_feat):
                            value = provider.identify(pt,QgsRaster.IdentifyFormatValue).results()[1]
                            #print(value)
                            if value==None:
                                pass
                            else:
                                values[k].append(value)
                                points.append(tmp_pt.asPoint())
                 
                        x += xsize
                    x = xmin
                    y -= ysize
            resultado.append(values)
            for value in values:
                resumen.append([np.mean(value), np.std(value)])
                #print ('   Parcela-----N Pixels: {} Media: {:.2f} Desviacion Estandar: {:.2f}'.format(np.size(value), np.mean(value), np.std(value)))
    return resultado,resumen


for nombre in capas_raster_de_interes:
    if nombre=='HM':
        resultado_hm=saca_valores_raster(nombre,feats)
        resultado_hm_simplificado=simplificar_lista(resultado_hm[0])
        tabla_hm=crea_tabla(resultado_hm)
        #print('estadisticas_lista[0][0]', estadisticas_lista[0][0])
        grafica_hm=grafica_histograma(resultado_hm_simplificado, estadisticas_lista(resultado_hm_simplificado,1)[0][0],estadisticas_lista(resultado_hm_simplificado,1)[0][1],"hm",)
        filtrado_hm=filtro_raster_intervalo(nombre,estadisticas_lista(resultado_hm_simplificado,1)[0] )
        
    if nombre=='HBC':
        resultado_hbc=saca_valores_raster(nombre,feats)
        resultado_hbc_simplificado=simplificar_lista(resultado_hbc[0])
        tabla_hbc=crea_tabla(resultado_hbc)
        grafica_hbc=grafica_histograma(resultado_hbc_simplificado,estadisticas_lista(resultado_hbc_simplificado,1)[0][0],estadisticas_lista(resultado_hbc_simplificado,1)[0][1],"hbc")
        filtrado_hbc=filtro_raster_intervalo(nombre,estadisticas_lista(resultado_hbc_simplificado,1)[0] )
    if nombre=='LC':
        resultado_lc=saca_valores_raster(nombre,feats)
        resultado_lc_simplificado=simplificar_lista(resultado_lc[0])
        tabla_lc=crea_tabla(resultado_lc)
        grafica_lc=grafica_histograma(resultado_lc_simplificado,estadisticas_lista(resultado_lc_simplificado,1)[0][0],estadisticas_lista(resultado_lc_simplificado,1)[0][1],"lc")
        filtrado_lc=filtro_raster_intervalo(nombre,estadisticas_lista(resultado_lc_simplificado,1)[0] )
    if nombre=='RC':
        resultado_rc=saca_valores_raster(nombre,feats)
        resultado_rc_simplificado=simplificar_lista(resultado_rc[0])
        tabla_rc=crea_tabla(resultado_rc)
        grafica_rc=grafica_histograma(resultado_rc_simplificado,estadisticas_lista(resultado_rc_simplificado,1)[0][0],estadisticas_lista(resultado_rc_simplificado,1)[0][1],"rc")
       
        filtrado_rc=filtro_raster_intervalo(nombre,estadisticas_lista(resultado_rc_simplificado,1)[0] )
    if nombre=='FCC':
        resultado_fcc=saca_valores_raster(nombre,feats)
        resultado_fcc_simplificado=simplificar_lista(resultado_fcc[0])
        tabla_fcc=crea_tabla(resultado_fcc)
        grafica_fcc=grafica_histograma(resultado_fcc_simplificado,estadisticas_lista(resultado_fcc_simplificado,1)[0][0],estadisticas_lista(resultado_fcc_simplificado,1)[0][1],"fcc")
        filtrado_fcc=filtro_raster_intervalo(nombre,estadisticas_lista(resultado_fcc_simplificado,1)[0] )
crea_html(['HM','FCC','RC','HBC','LC'],[tabla_hm,tabla_fcc,tabla_rc,tabla_hbc,tabla_lc],[grafica_hm,grafica_fcc,grafica_rc,grafica_hbc,grafica_lc] )       # [] 
#busca las celdas que encuentran lo anterior (multiplica)
multiplicado=multiplica_rasters(filtrado_hm,filtrado_hbc,filtrado_lc,filtrado_rc,filtrado_fcc)
raster=agrega(multiplicado)
vectorizar(raster,carpeta+"similar3.shp")

    
#print(resultado) 
epsg = layervectorial.crs().postgisSrid()








"""
#para crear una capa de puntos en cada celda
#points
uri = "Point?crs=epsg:" + str(epsg) + "&field=id:integer""&index=yes"
 
mem_layer = QgsVectorLayer(uri,
                           'point',
                           'memory')
 
prov = mem_layer.dataProvider()
 
feats = [ QgsFeature() for i in range(len(points)) ]
 
for i, feat in enumerate(feats):
    feat.setAttributes([i])
    feat.setGeometry(QgsGeometry.fromPointXY(points[i]))
 
prov.addFeatures(feats)
 
QgsProject.instance().addMapLayer(mem_layer)"""
 
            
