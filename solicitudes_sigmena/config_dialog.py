# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ConfigDialog
                                 A QGIS plugin
Permite cargar la parcela o recintos del Sigpac correspondientes a una provincia, poligono y parcela dada, tanto con su codigo como con un desplegable como con una coordenada.
Generado con Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-01-29
        git sha              : $Format:%H$
        copyright            : (C) 2019 by javier diez
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

import os

from PyQt5 import uic
from PyQt5 import QtWidgets

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'config_dialog_base.ui'))



class ConfigDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ConfigDialog, self).__init__(parent)

        print("llega al config dialog")
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
class Plugin:
    """QGIS Plugin Implementation."""
    def __init__(self, iface):
    
        self.dlg.button.connect(self.open_new_dialog)
