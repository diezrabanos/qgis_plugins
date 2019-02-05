"""
/***************************************************************************
      zoomtopastedialog  - A QGIS plugin to zoom the map canvas to a point
                         specified in the clippboard
                             -------------------
    begin                : 2014-10-14
    copyright            : (C) 2014 by GD
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

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from qgis.core import *

from .ui_zoomtopaste import Ui_zoomtopaste 

# create the dialog for zoom to point


class zoomtopastedialog(QDialog,Ui_zoomtopaste): 

    browsePathSetting="/plugins/zoom_sigmena"

    def __init__(self, iface):
        QDialog.__init__(self)
        self._iface = iface

        settings = QSettings()
        self._home = settings.value(zoomtopastedialog.browsePathSetting,'')

        # Set up the user interface from Designer.
        
        self.ui = Ui_zoomtopaste()
        self.setupUi(self)
        
        
