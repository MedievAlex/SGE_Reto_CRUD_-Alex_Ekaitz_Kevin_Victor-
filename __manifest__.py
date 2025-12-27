# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'aplicacion_incidencias',
    'version': '1.0',
    'description': """
Aplicación de incidencias del RETO 1 - CRUD de grupo compuesto por Alex, Ekaitz, Kevin y Victor.
    """,
    'depends': ['base'],
    'data': [
        "security/aplicacion_incidencias_security.xml",
        "security/ir.model.access.csv",
        "views/encuesta_views.xml",
        "views/menu.xml"
    ],
    'license': 'LGPL-3',
}