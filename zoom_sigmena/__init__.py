#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
################################################################################
#
# Copyright 2016 geoplaning GmbH 
# All rights reserved
#
# This program is released under the terms of the new BSD license. See the 
# LICENSE file for more information.
#
################################################################################


from .zoomtopaste import zoomtopaste


def name():
    return "zoomtopaste"

def description():
    return "zoomtopaste"

def version():
    return "1.2"

def qgisMinimumVersion():
    return "3.0"

def authorName():
    return "F. Javier Diez Rabanos"

def classFactory(iface):
    return zoomtopaste(iface)


