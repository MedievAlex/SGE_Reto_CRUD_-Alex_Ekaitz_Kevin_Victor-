# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'aplicacion_incidencias',
    'version': '1.4.2',
    'description': """
Aplicación de incidencias del RETO 2 - CRUD Avanzado de grupo compuesto por Alex, Ekaitz, Kevin y Victor.
    """,
    'depends': ['base', 'project'],
    'images': ['static/description/icon.png'],
    'data': [
        "security/aplicacion_incidencias_security.xml",
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/incidencias_views.xml",
        "views/comentarios_views.xml",
        "views/encuesta_views.xml",
        "views/herencia_incidencias_views.xml",
        "views/herencia_encuesta_views.xml"
    ],
    'license': 'LGPL-3',
}