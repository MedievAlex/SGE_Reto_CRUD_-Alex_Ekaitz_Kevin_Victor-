from odoo import fields, models

class Estadisticas(models.Model):
    _name = "aplicacion_incidencias.estadisticas"
    _description = 'Tabla de Kevin'

    # [ CAMPOS SIMPLES ]
    fecha = fields.Date(String="Fecha")
    total_incidencias = fields.Integer(String="Total Incidencias")
    incidencias_finalizadas = fields.Integer(String="Finalizadas")
    tiempo_promedio_resolucion = fields.Integer(String="Promedio Resolucion")

    # [ CAMPOS RELACIONALES ]
    # [primary key]
    # id_comentario