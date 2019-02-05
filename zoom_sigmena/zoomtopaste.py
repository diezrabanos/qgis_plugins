"""
/***************************************************************************
      zoomtopastedialog  - A QGIS plugin to zoom the map canvas to a point
                         specified in the clippboard
                             -------------------
    begin                : 2018-10-14
    copyright            : (C) 2018 by GD
    email                : gd at geoplaning.de
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
# Import the PyQt and QGIS libraries
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from qgis.core import *
from qgis.gui import *
from win32com.client import Dispatch
 
# Initialize Qt resources from file resources.py
from . import resources

# Import the code for the dialog
from .zoomtopastedialog import zoomtopastedialog 

class zoomtopaste:
    def __init__(self, iface):
        # Save reference to the QGIS interface
        self._iface = iface

    def initGui(self):
        #import pydevd
        #pydevd.settrace('localhost', port=55130, stdoutToServer=True, stderrToServer=True)

        # Create action that will start plugin configuration
        icon_path = r'C:\Users\dierabfr\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins/zoom_sigmena/icon.png'
        icon = QIcon(icon_path)#':/plugins/foo/bar.png'
        self.action = QAction(icon, u"Zoom Sigmena",self._iface.mainWindow())
        self.action.setWhatsThis("Configuration for Zoom To Paste plugin")
        self.action.triggered.connect(self.run)
        
       
        # Add toolbar button and menu item
        self._iface.addToolBarIcon(self.action)
        self._iface.addPluginToMenu("&Sigmena", self.action)
       

       #self._iface.setAcceptDrops(True)

        #self.actionzoom = QAction(QIcon(":/plugins/zoom_sigmena/icon_now.png"),"Zoom Now",self._iface.mainWindow())
        #self.actionzoom.setWhatsThis("Zoom Now")
        #self.actionzoom.triggered.connect(self.zoomnow)

        # Add toolbar button and menu item
        #self._iface.addToolBarIcon(self.actionzoom)
        
        #self._iface.addPluginToMenu("&Zoom Now", self.actionzoom)

               
       #How to call a method by a key shortcut
        #self._iface.registerMainWindowAction(self.action, "F7")
        


        #self.actionopenfrm = QAction(QIcon(":/plugins/zoomtopaste/icon_frm.png"),"Open Form",self._iface.mainWindow())
        #self.actionopenfrm.triggered.connect(self.DoDumpAccessInfo)
       
        # Add toolbar button and menu item
        #self._iface.addToolBarIcon(self.actionopenfrm)
        #self._iface.addPluginToMenu("&AccessInfo", self.actionopenfrm)
   

        
        
    def unload(self):
        # Remove the plugin menu item and icon
       self._iface.removePluginMenu("&Sigmena", self.action)
       #self._iface.removePluginMenu("&Zoom Now", self.actionzoom)
       self._iface.removeToolBarIcon(self.action)
       #self._iface.removeToolBarIcon(self.actionzoom)
       self._iface.unregisterMainWindowAction(self.action)
       #self._iface.unregisterMainWindowAction(self.actionzoom)
        #self.iface.removeToolBarIcon(self.actionopenfrm)

    # run method that performs all the real work
    def run(self):

        # create and show the zoomtopaste dialog
        dlg = zoomtopastedialog(self._iface)
        # dlg.setupUi(self)
        # fetch the last used values from settings and intialize the
        # dialog with them
        settings = QSettings("MicroResources", "zoomtopaste")

        xValue = settings.value("coordinate/x", '')
        dlg.xCoord.setText(str(xValue))
        
        yValue = settings.value("coordinate/y", '')
        dlg.yCoord.setText(str(yValue))
        
        #scale = settings.value("zoom/scale", 4)
        #dlg.spinBoxScale.setValue(int(scale))
        
        #cbx = settings.value("zoom/checked", 0)
        #dlg.checkBox.setChecked(int(cbx))

        
        dlg.show()
        result = dlg.exec_()
        # See if OK was pressed
        if result == 1:
            scale=500
            # Get the coordinates and scale factor from the dialog
            x = dlg.xCoord.text()
            y = dlg.yCoord.text()
            #scale = dlg.spinBoxScale.value()


            rect = QgsRectangle(float(x) - scale,float(y) - scale,float(x) + scale,float(y) + scale)
            # Get the map canvas
            mc =self._iface.mapCanvas()
            # Set the extent to our new rectangle
            mc.setExtent(rect)

            #nuevo javi
            pt = QgsPoint(float(x),float(y))
            vl = QgsVectorLayer("Point", "Zoom", "memory")
            
            pr = vl.dataProvider()
            
            print ("ok creada la capa")
            vl.startEditing()
            # add fields
            pr.addAttributes([
                    QgsField("x",  QVariant.Int),
                    QgsField("y", QVariant.Double)])
            vl.updateFields()
            fet = QgsFeature()

            # tell the vector layer to fetch changes from the provider
            print ("ok creados los campos")
            # add a feature
            fet = QgsFeature()
            
            fet.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(float(x),float(y))))
            
            fet.setAttributes([float(x),float(y)])
            
            pr.addFeatures([fet])
            symbol = QgsMarkerSymbol.createSimple({'name': 'circle', 'color': 'orange','size': '2',})
            vl.renderer().setSymbol(symbol)
            vl.updateExtents()
            vl.commitChanges()
            vl.updateExtents()
            
            QgsProject.instance().addMapLayer(vl)
            
            """p = QgsPalLayerSettings()
            #p.readFromLayer(vl)
            p.enabled = True
            p.fieldName = '''concat('X: ',"X",' Y: ',"Y")'''
            p.isExpression = True
            p.placement = QgsPalLayerSettings.OverPoint
            p.displayAll = True

            layer_settings  = QgsPalLayerSettings()
            text_format = QgsTextFormat()

            text_format.setFont(QFont("Arial", 10))
            text_format.setSizeUnit(QgsUnitTypes.RenderMapUnits)
            text_format.setSize(100)
            #text_format.setSizeMapUnitScale(True) <-- wants a "QgsMapUnitScale"

            layer_settings.setFormat(text_format)

            layer_settings = QgsVectorLayerSimpleLabeling(layer_settings)
            vl.setLabeling(layer_settings)
            vl.setLabelsEnabled(True)"""
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
            vl.setLabelsEnabled(True)
            vl.setLabeling(layer_settings)
            vl.triggerRepaint()
            
            #p.setDataDefinedProperty(QgsPalLayerSettings.Size,True, True, "10", "")
            #p.textColor = QColor("orange")
            #p.quadOffset = QgsPalLayerSettings.QuadrantBelow
            #p.yOffset = 1
            #p.labelOffsetInMapUnits = False
            #p.writeToLayer(vl)
            #labelingEngine = QgsPalLabeling()
     
            #vl.updateFieldMap()
            
            # Refresh the map
            mc.refresh()

            
            # store the settings
            settings.setValue("coordinate/x", x)
            settings.setValue("coordinate/y", y)
            settings.setValue("zoom/scale", scale)

            #settings.setValue("zoom/checked", "1" if dlg.checkBox.isChecked() else "0")
        


 
                #QObject.connect(QApplication.clipboard(), SIGNAL("dataChanged()"), self.destroy)
            QApplication.clipboard().dataChanged.connect(self.destroy)
                #QApplication.clipboard().clear

            

#nuevo javi esta funcion
    
    def highlight(self,point):
            dlg = zoomtopastedialog(self._iface)
            #x = self.dlg.ui.mTxtX.text()
            #y = self.dlg.ui.mTxtY.text()
            x = dlg.xCoord.text()
            y = dlg.yCoord.text()
            print ("highlighting..")
            #canvas = self.canvas
            
            #currExt = canvas.extent()
            
            #leftPt = QgsPoint(currExt.xMinimum(),point.y())
            #rightPt = QgsPoint(currExt.xMaximum(),point.y())
            
            #topPt = QgsPoint(point.x(),currExt.yMaximum())
            #bottomPt = QgsPoint(point.x(),currExt.yMinimum())
            
            #horizLine = QgsGeometry.fromPolyline( [ leftPt , rightPt ] )
            #vertLine = QgsGeometry.fromPolyline( [ topPt , bottomPt ] )
            
            #self.crossRb.reset(QGis.Line)
            #self.crossRb.addGeometry(horizLine,None)
            #self.crossRb.addGeometry(vertLine,None)
            """
            if QGis.QGIS_VERSION_INT >= 10900:
                    rb = self.rubberBand
                    rb.reset(QGis.Point)
                    rb.addPoint(point)
            else:
                    self.vMarker = QgsVertexMarker(self.canvas)
                    self.vMarker.setIconSize(10)
                    self.vMarker.setCenter(point)
                    self.vMarker.show()
            """
            #lo nuevo
            
            vl = QgsVectorLayer("Point", "Zoom", "memory")
            
            pr = vl.dataProvider()
            
            print ("ok creada la capa")
            vl.startEditing()
            # add fields
            pr.addAttributes([
                    QgsField("x",  QVariant.Int),
                    QgsField("y", QVariant.Double)])
            vl.updateFields()
            fet = QgsFeature()

            # tell the vector layer to fetch changes from the provider
            print ("ok creados los campos")
            # add a feature
            fet = QgsFeature()
            
            fet.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(float(x),float(y))))
            
            fet.setAttributes([float(x),float(y)])
            
            pr.addFeatures([fet])

            #cambio la simbologia
            symbol = QgsMarkerSymbolV2.createSimple({'name': 'circle', 'color': 'orange','size': '2',})
            vl.rendererV2().setSymbol(symbol)

            # update layer's extent when new features have been added
            # because change of extent in provider is not propagated to the layer
            vl.updateExtents()
            vl.commitChanges()
            vl.updateExtents()
            canvas = self.canvas
            canvas.setExtent(vl.extent())
            QgsMapLayerRegistry.instance().addMapLayer(vl)
            canvas.refresh()
            #vl.updateFieldMap()


    #etiquetas

            p = QgsPalLayerSettings()
            p.readFromLayer(vl)
            p.enabled = True
            p.fieldName = '''concat('X: ',"X",' Y: ',"Y")'''
            p.isExpression = True
            #p.placement = QgsPalLayerSettings.OverPoint
            p.displayAll = True
            p.setDataDefinedProperty(QgsPalLayerSettings.Size,
                                     True, True, "10", "")
            p.textColor = QColor("orange")
            p.quadOffset = QgsPalLayerSettings.QuadrantBelow
            p.yOffset = 1
            p.labelOffsetInMapUnits = False
            p.writeToLayer(vl)
            labelingEngine = QgsPalLabeling()



    #etiquetas
            #lo viejo
            # wait .5 seconds to simulate a flashing effect
            QTimer.singleShot(500,self.resetRubberbands)



    """def dropChangedGo(self):

        # create and show the zoomtopaste dialog
        dlg = zoomtopastedialog(self._iface)

        clipboard = QApplication.clipboard()
        if not clipboard.mimeData().hasText():
            return False

        text = unicode(clipboard.text())
        print(text)
        # create and show the zoomtopaste dialog

        if text != "" and text.find(',')>0:
            #5744021,3503546
            str = text.split(",")
            print(str)

            x = str[1]
            y = str[0]
            if int(x) > 0 and int(y) > 0:

                dlg.xCoord.setText((x))
                dlg.yCoord.setText((y))

                scale = dlg.spinBoxScale.value()

                # Create a rectangle to cover the new extent
                rect = QgsRectangle(float(x) - scale, float(y) - scale, float(x) + scale, float(y) + scale)
                # Get the map canvas
                mc =self._iface.mapCanvas()
                # Set the extent to our new rectangle
                mc.setExtent(rect)
                # Refresh the map
                mc.refresh()

                settings = QSettings("MicroResources", "zoomtopaste")
                settings.setValue("coordinate/x", x)
                settings.setValue("coordinate/y", y)

        else:
           self._iface.messageBar().pushMessage("Error dropChangedGo", "Im Clipbord sind falsche Daten ", level = Qgis.Warning, duration = 3)
            #QMessageBox.information(self.iface.mainWindow(),text, "Im Clipbord sind falsche Daten")"""

#http://www.programcreek.com/python/example/4315/win32com.client.Dispatch

    def DoDumpAccessInfo(self):

        import daodump

        a = forms = None
        try:
            
            a=Dispatch("Access.Application")
            a.DoCmd.RunMacro('test')
            a.OpenCurrentDatabase(dbname)
            db = a.CurrentDb()
            daodump.DumpDB(db,1)

            forms = a.Forms
            lf=len(forms)



            #from win32com.client import Dispatch
            dbForm = 'FRM: _Haltungsdaten'
            filter ='id= "[% "ID_LSTRE" %]"'
            dbname ='reporter.mdb'


            objDB = a.CurrentDb()
            if objDB is None:
                a.OpenCurrentDatabase(dbname,True)

            #a.Visible = True
            #DoCmd.OpenForm "Employees", , ,"LastName = 'King'"

            a.DoCmd.OpenForm(dbForm,0,filter)
            #a.forms(dbForm).Filter = filter
            a.forms(dbForm).FilterOn = True

            # Uncommenting these lines means Access remains open.
            #               for form in forms:
            #                       print " %s" % form.Name
            reports = a.Reports
            rf=len(reports)

        finally:
            if not a is None:
               self._iface.messageBar().pushMessage("Error DoDumpAccessInfo", "Access nicht geoeffnet ", level=Qgis.Warning, duration=3)



    def destroy(self):
        pass
