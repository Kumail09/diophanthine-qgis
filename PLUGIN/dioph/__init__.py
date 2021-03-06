# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Calculator
                                 A QGIS plugin
 Solves the Linear Dipohantine Equation
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-03-31
        copyright            : (C) 2021 by Kumail Raza
        email                : kumail0691@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Calculator class from file Calculator.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Dioph import Calculator
    return Calculator(iface)
