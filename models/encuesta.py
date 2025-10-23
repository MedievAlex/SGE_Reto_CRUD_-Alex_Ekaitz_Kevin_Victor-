from odoo import fields, models

class Encuesta(models.Model):
    _name = "aplicacion_incidencias.encuesta"

    # [ CAMPOS SIMPLES ]
    contenido = fields.Text(String="Encuesta")
    fecha_creacion = fields.Date(String="Fecha de creacion")

    # [ CAMPOS RELACIONALES ]
    # [primary key]
    #id_encuesta = fields.One2one(comodel_name='aplicacion_incidencias.encuesta', string="Encuesta", required=True)
    # [foreign key]
    #id_incidencia = fields.One2one(comodel_name='aplicacion_incidencias.incidencia', string="Encuesta", required=False)
    # [foreign key]
    #id_empleado = fields.