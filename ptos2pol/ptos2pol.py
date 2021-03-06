# -*- coding: utf-8 -*-
"""
/***************************************************************************
ptos2pol
                                 A QGIS plugin
Permite crear una capa de poligonos partiendo de los elementos de una capa de puntos. Si se seleccionan ciertos elemento solo se tendran estos en cuenta.
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


from qgis.PyQt.QtCore import QSettings, QTranslator, qVersion, QCoreApplication#,QFileInfo
from qgis.PyQt.QtGui import QIcon, QColor,QFont
from qgis.PyQt.QtWidgets import QAction, QFileDialog
from PyQt5.QtWidgets import QMessageBox

# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .ptos2pol_dialog import ptos2polDialog
import os.path

#import para procesar
import qgis.core as qgisCore
from qgis.core import QgsProject, QgsVectorLayer,QgsField,QgsExpression,QgsExpressionContext,QgsExpressionContextScope,QgsVectorFileWriter, QgsMarkerSymbol,QgsRendererCategory,QgsCategorizedSymbolRenderer,QgsPointXY, QgsPoint,QgsFeature,QgsGeometry,QgsLineSymbol,QgsExpressionContextUtils,QgsPalLayerSettings,QgsTextFormat,QgsVectorLayerSimpleLabeling,QgsExpressionContextUtils,QgsCoordinateTransform,QgsCoordinateReferenceSystem,QgsApplication,QgsRectangle,QgsMarkerSymbol,QgsRendererCategory,QgsCategorizedSymbolRenderer,QgsLineSymbol,QgsFillSymbol,QgsSingleSymbolRenderer,QgsPalLayerSettings,QgsTextFormat ,QgsVectorLayerSimpleLabeling, QgsExpressionContextUtils
from qgis.PyQt.QtCore import QVariant
from qgis.utils import iface


import processing
import os
import glob
import re
import sys


import math
import time



class ptos2pol:
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
            'ptos2pol_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        self.dlg = ptos2polDialog()

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Sigmena')
        
       
        self.first_start = None
        #self.dlg.pushButton_select_file.clicked.connect(self.cargacapadepuntos)
        

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
        return QCoreApplication.translate('ptos2pol', message)


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
        usuario=QgsApplication.qgisSettingsDirPath()
        icon_path=os.path.join(usuario,r"python\plugins\ptos2pol\icon.png")
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

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/ptos2pol/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'ptos2pol'),
            callback=self.run,
            parent=self.iface.mainWindow())

        # will be set False in run()
        self.first_start = True
        
    def cargacapadepuntos(self):
        """seleciono la capa de puntos con los datos de entrada""" 
        capaptos = QFileDialog.getOpenFileName( self.dlg , "Selecciona capa de puntos",filter = "shp(*.shp)")
        self.dlg.rutaptos.setText(capaptos[0])
        print (capaptos[0])

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Sigmena'),
                action)
            self.iface.removeToolBarIcon(action)

    def run(self):
        print ("paso por el run")
       
        #coloco el puntero arriba del todo
        QgsProject.instance().layerTreeRegistryBridge().setLayerInsertionPoint( QgsProject.instance().layerTreeRoot(), 0 )
   
             
        
        """Run method that performs all the real work"""

        
        #genero una lista con las columnas de la capa de puntos
        vl2=iface.activeLayer()
        if vl2 is None:
            iface.messageBar().pushMessage("ATENCION", "Selecciona una capa de puntos", duration=10)
        #if vl2.wkbType()< 1 or vl2.wkbType() > 1:
            #iface.messageBar().pushMessage("ATENCION", "Selecciona una capa de puntos", duration=10)
        #else:
        if vl2.wkbType()== 1 or vl2.wkbType()==1001:
            misdatos=[]
            misdatos = [f.name() for f in vl2.fields()]
            
            #trato de rellenar el desplegable con las columnas
            #anado un elemneto en blanco en el desplegable
            self.dlg.cb1.clear()
            self.dlg.cb1.addItem( "")
            for element in misdatos:
                self.dlg.cb1.addItem( element)
                
            # Create the dialog with elements (after translation) and keep reference
            # Only create GUI ONCE in callback, so that it will only load when the plugin is started
            if self.first_start == True:
                self.first_start = False

            # show the dialog
            self.dlg.show()
            
            # Run the dialog event loop
            result = self.dlg.exec_()
            # See if OK was pressed
            if result:
                column = self.dlg.cb1.currentIndex()
                columna=misdatos[int(column)-1]                

                #parece que lo mejor sera la seleccion de una capa y dentro de ella de los elementos en ella seleccionados solo. Para ello habria que crear una capa temporal con solo los seleccioandos      
                #if vl2.wkbType()== 1 or vl2.wkbType()==1001:
                selection = vl2.selectedFeatures()
                elementosseleccionados=len(selection)

                if elementosseleccionados ==0:
                    vl2.selectAll()
                if elementosseleccionados ==1 or elementosseleccionados ==2:
                    iface.messageBar().pushMessage("ATENCION", "Tienes algun elemento seleccionado pero no los suficientes para crear un poligono", duration=10)
                    
                #onlySelectedFeatures
                results0=processing.run("native:saveselectedfeatures", {'INPUT':vl2,'OUTPUT':'memory:puntos_seleccionados_ptos2pol'})
                result_layer0 = results0['OUTPUT']
                entrada=result_layer0
                QgsProject.instance().addMapLayer(result_layer0)
            
                #hay que hacer que cree una columna con el orden el solo por si por defecto no se pone ninguna
                params={'INPUT':entrada,'GROUP_FIELD':None,'ORDER_FIELD':columna,'DATE_FORMAT':'', 'OUTPUT':'memory:lineas_ptos2pol'}
                results=processing.run("qgis:pointstopath", params)
                result_layer = results['OUTPUT']
                QgsProject.instance().addMapLayer(result_layer)
                params={'INPUT':result_layer,'OUTPUT':'memory:poligono_ptos2pol '}
                results2=processing.run("qgis:linestopolygons", params )
                result_layer2 = results2['OUTPUT']
               
                #por el mismo precio calculo la superficie
                #ADDING NEW FIELD
                layer_provider=result_layer2.dataProvider()
                layer_provider.addAttributes([QgsField("hectarea",QVariant.Double, "double", 10, 4)])
                result_layer2.updateFields()
                #UPDATING/ADD ATTRIBUTE VALUE
                result_layer2.startEditing()
                features = result_layer2.getFeatures()
                for f in features:
                    id=f.id()
                    area=f.geometry().area()/10000
                    fieldindex = result_layer2.dataProvider().fieldNameIndex("hectarea")
                    attr_value={fieldindex:area}#fieldindex, antes era 2
                    layer_provider.changeAttributeValues({id:attr_value})
                result_layer2.commitChanges()
                
                #tendra que etiquetar la superficie con dos decimales y cambiar la simbologia, ya que estamos.
                sym1 = QgsFillSymbol.createSimple({'style': 'vertical','color': '0,0,0,0', 'outline_color': 'red'})
                renderer=QgsSingleSymbolRenderer(sym1)
                #etiqueto
                layer_settings  = QgsPalLayerSettings()
                text_format = QgsTextFormat()
                text_format.setFont(QFont("Arial", 12))
                text_format.setSize(12)
                text_format.setColor(QColor("Red"))
                layer_settings.setFormat(text_format)
                layer_settings.fieldName = '''concat(round("hectarea",2),' ha.')'''            
                layer_settings.isExpression = True
                layer_settings.enabled = True
                layer_settings = QgsVectorLayerSimpleLabeling(layer_settings)
                result_layer2.setLabelsEnabled(True)
                result_layer2.setLabeling(layer_settings)
                result_layer2.triggerRepaint()
                result_layer2.setRenderer(renderer)

                QgsProject.instance().addMapLayer(result_layer2)
        else:
            print(vl2.wkbType())
            iface.messageBar().pushMessage("ATENCION", "Selecciona una capa de puntos", duration=10)



        

