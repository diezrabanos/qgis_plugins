# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Alidadas
                                 A QGIS plugin
 esto es lo que hace Alidadas
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2019-03-29
        git sha              : $Format:%H$
        copyright            : (C) 2019 by Javier Diez Rabanos
        email                : dierabfr@jcyl.es
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
#from PyQt5.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
#from PyQt5.QtGui import QIcon
#from PyQt5.QtWidgets import QAction

from qgis.PyQt.QtCore import QSettings, QTranslator, qVersion, QCoreApplication#,QFileInfo
from qgis.PyQt.QtGui import QIcon, QColor,QFont
from qgis.PyQt.QtWidgets import QAction, QFileDialog
from PyQt5.QtWidgets import QMessageBox

# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .gpsDescargaCarga_dialog import GpsDescargaCargaDialog
import os.path

#import para procesar
import qgis.core as qgisCore
from qgis.core import QgsProject, QgsVectorLayer,QgsField,QgsExpression,QgsExpressionContext,QgsExpressionContextScope,QgsVectorFileWriter, QgsMarkerSymbol,QgsRendererCategory,QgsCategorizedSymbolRenderer,QgsPointXY, QgsPoint,QgsFeature,QgsGeometry,QgsLineSymbol,QgsExpressionContextUtils,QgsPalLayerSettings,QgsTextFormat,QgsVectorLayerSimpleLabeling,QgsExpressionContextUtils,QgsCoordinateTransform,QgsCoordinateReferenceSystem
from qgis.PyQt.QtCore import QVariant
from qgis.utils import iface
#from PyQt5.QtWidgets import QMessageBox
#from PyQt5.QtCore import QFileInfo
#from qgis.PyQt.QtCore import QFileInfo

import processing
import os
import glob
import re
import sys
#from qgis import *

import math
import time



class GpsDescargaCarga:
    """QGIS Plugin Implementation."""
    def __init__(self, iface):
        """Constructor.
        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'ZoomSigmena_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        self.dlg = GpsDescargaCargaDialog()

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Sigmena')
        
        #self.toolbar = self.iface.addToolBar(u'Sigmena')             #creo que no hace nada
        #self.toolbar.setObjectName(u'Sigmena')            #creo que no hace nada
        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None
        #self.dlg.pushButton_select_path.clicked.connect(self.select_laz_folder)

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('GpsDescargaCarga', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        
    

        
        #cambio el icon path para mi equipo.
        usuario=QgsExpressionContextUtils.globalScope().variable('user_account_name')
        icon_path=os.path.join(r"C:\Users",usuario,r"AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\gpsDescargaCarga\icon.png")
        #icon_path=r"C:\Users\dierabfr\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\alidadas\icon.png"
        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)
            #self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/gpsDescargaCarga/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'gpsDescargaCarga'),
            callback=self.run,
            parent=self.iface.mainWindow())

        # will be set False in run()
        self.first_start = True
        

    
    



    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Sigmena'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        #del self.toolbar        #PUEDO PROBAR A BORRAR COSAS
        #del self.menu
        #del self.dlg




    

    


    def run(self):
        print ("paso por el run")
       
        #coloco el puntero arriba del todo
        QgsProject.instance().layerTreeRegistryBridge().setLayerInsertionPoint( QgsProject.instance().layerTreeRoot(), 0 )
   
        
     
        
        """Run method that performs all the real work"""

        # Create the dialog with elements (after translation) and keep reference
        # Only create GUI ONCE in callback, so that it will only load when the plugin is started
        if self.first_start == True:
            self.first_start = False
            #self.dlg = SilvilidarDialog()
            #la siguiente linea inicia el boton de cargar carpetas, peta al cerrar el qgis, deberia poner algun close o algo
            #self.dlg.pushButton_select_path.clicked.connect(self.select_laz_folder)
            #print("inicio el boton en el gui")
            #self.dlg.pushButton_select_path.setEnabled(True)
            #print ("pone le boton como habiltado")
            

        # show the dialog
        self.dlg.show()
        
        #self.dlg.pushButton_select_path.clicked.connect(self.select_laz_folder)

        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:

            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            #print ("lo imprime si le doy a aceptar en el dialogo")
            
            #la carpeta la he cogido al pulsar el boton de la carpeta

             #saco de  aqui variables que estan en las cajitas
            #src_seleccionado=self.dlg.comboBox_src.currentIndex()
             
            # Get the coordinates and scale factor from the dialog
            nombre=self.dlg.nombrearchivo.text()##displayText()
           
            
            #nombre=nombre.replace(' ','_')
            
            print (nombre)
            
            path = r'C:/sigmena/gps/'+nombre+'.gpx'
            usuario=QgsExpressionContextUtils.globalScope().variable('user_account_name')
            comando=os.path.join(r"C:\Users",usuario,r"AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/gpsDescargaCarga/cmdbabel/descargagps.bat")
            #comando= "C:/Users/descargagps.bat"

            os.system(comando+" "+ path)


            
            
            names =["waypoint", "track", "route"]

    
            dest_crs = QgsCoordinateReferenceSystem(25830)

            for name in names:
                #iface.addVectorLayer(ruta+"?type="+name, name, "gpx")
                vectorLyr =QgsVectorLayer(path+"?type="+name, name, "gpx")
                QgsVectorFileWriter.writeAsVectorFormat(vectorLyr,str(path[:-4])+"_"+name,"utf-8",dest_crs,"ESRI Shapefile")
                iface.addVectorLayer(str(path[:-4])+"_"+name+".shp", str(nombre)+"_"+name, "ogr")
            

            #creo una capa temporal con las coordenadas
            """
            # create layer
            vl2 = QgsVectorLayer("Point?crs=EPSG:"+src, "Zoom", "memory")
            pr2 = vl2.dataProvider()
            
            vl2.startEditing()
            # add fields
            pr2.addAttributes([
                            QgsField("x",  QVariant.Double),
                            QgsField("y", QVariant.Double)])
            vl2.updateFields() 
            # tell the vector layer to fetch changes from the provider
            
            #$add a feature
            fet = QgsFeature()
            fet.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(float(x),float(y))))
            fet.setAttributes([ float(x),float( y)])
            pr2.addFeatures([fet])
            
            
           
            #cambio la simbologia
            symbol = QgsMarkerSymbol.createSimple({'name': 'circle', 'color': 'red','size': '3',})
            vl2.renderer().setSymbol(symbol)

            # update layer's extent when new features have been added
            # because change of extent in provider is not propagated to the layer

            layer_settings  = QgsPalLayerSettings()
            text_format = QgsTextFormat()

            text_format.setFont(QFont("Arial", 12))
            text_format.setSize(12)
            text_format.setColor(QColor("Orange"))

            #buffer_settings = QgsTextBufferSettings()
            #buffer_settings.setEnabled(True)
            #buffer_settings.setSize(0.10)
            #buffer_settings.setColor(QColor("Orange"))

            #text_format.setBuffer(buffer_settings)
            layer_settings.setFormat(text_format)
            #myexp=QgsExpression('''concat('X: ',"X",' Y: ',"Y")''')
            layer_settings.fieldName = '''concat('X: ',"X",' Y: ',"Y")'''
            layer_settings.isExpression = True
            #layer_settings.placement = 7
            #layer_settings.quadOffset = QgsPalLayerSettings.QuadrantBelow
            #layer_settings.yOffset = 1

            layer_settings.enabled = True

            layer_settings = QgsVectorLayerSimpleLabeling(layer_settings)
            vl2.setLabelsEnabled(True)
            vl2.setLabeling(layer_settings)
            vl2.triggerRepaint()



            


            


                
            # update layer's extent when new features have been added
            # because change of extent in provider is not propagated to the layer
            vl2.updateExtents()
            vl2.commitChanges()
            vl2.updateExtents()
            canvas = self.iface.mapCanvas()
            canvas.setExtent(vl2.extent())
         
            crsSrc = QgsCoordinateReferenceSystem('EPSG:'+str(src))
            crsDest = QgsProject.instance().crs()

            if crsSrc!=crsDest:
                print("paso por aqui")
                xform = QgsCoordinateTransform(crsSrc, crsDest, QgsProject.instance())
                canvas.setExtent(xform.transform(vl2.extent()))
            
            self.iface.mapCanvas().zoomScale(10000)
          

            """
            #QgsProject.instance().addMapLayer(vl2)
            
        