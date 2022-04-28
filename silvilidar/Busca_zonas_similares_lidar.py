import numpy as np
import os

import processing
    


carpeta="d:/pruebas/lidar/veinte5/"

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
    print('TOTAL-------N Pixels: {} Media: {:.2f} Desviacion Estandar: {:.2f}'.format(np.size(lista), np.mean(lista), np.std(lista)))
    print("Rango de valores objetivo entre ---------{:.2f} y {:.2f}---------".format(rango[0],rango[1]))
    return rango,estadisticos

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
    resultado=[]
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
                print ('   Parcela-----N Pixels: {} Media: {:.2f} Desviacion Estandar: {:.2f}'.format(np.size(value), np.mean(value), np.std(value)))
    return resultado


for nombre in capas_raster_de_interes:
    if nombre=='HM':
        resultado_hm=saca_valores_raster(nombre,feats)
        resultado_hm_simplificado=simplificar_lista(resultado_hm)
        filtrado_hm=filtro_raster_intervalo(nombre,estadisticas_lista(resultado_hm_simplificado,1)[0] )
        
    if nombre=='HBC':
        resultado_hbc=saca_valores_raster(nombre,feats)
        resultado_hbc_simplificado=simplificar_lista(resultado_hbc)
        filtrado_hbc=filtro_raster_intervalo(nombre,estadisticas_lista(resultado_hbc_simplificado,1)[0] )
    if nombre=='LC':
        resultado_lc=saca_valores_raster(nombre,feats)
        resultado_lc_simplificado=simplificar_lista(resultado_lc)
        filtrado_lc=filtro_raster_intervalo(nombre,estadisticas_lista(resultado_lc_simplificado,1)[0] )
    if nombre=='RC':
        resultado_rc=saca_valores_raster(nombre,feats)
        resultado_rc_simplificado=simplificar_lista(resultado_rc)
        filtrado_rc=filtro_raster_intervalo(nombre,estadisticas_lista(resultado_rc_simplificado,1)[0] )
    if nombre=='FCC':
        resultado_fcc=saca_valores_raster(nombre,feats)
        resultado_fcc_simplificado=simplificar_lista(resultado_fcc)
        filtrado_fcc=filtro_raster_intervalo(nombre,estadisticas_lista(resultado_fcc_simplificado,1)[0] )
        
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
 
            

