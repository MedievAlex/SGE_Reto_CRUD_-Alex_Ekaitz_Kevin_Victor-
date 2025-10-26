from odoo import fields, models

class Encuesta(models.Model):
    _name = "aplicacion_incidencias.encuesta"

    # [ CAMPOS SIMPLES ]
    puntuacion = fields.Integer(String="Puntuacion")
    comentario = fields.Text(String="Comentario")
    fecha_respuesta = fields.Date(String="Fecha de respuesta")

    # [ CAMPOS RELACIONALES ]
    # [primary key]
    #id_encuesta = fields.One2one(comodel_name='aplicacion_incidencias.encuesta', string="Encuesta", required=True, ondelete="cascade")
    # [foreign key]
    #id_incidencia = fields.One2one(comodel_name='aplicacion_incidencias.incidencia', string="Incidencia", required=False)
    # [foreign key]
    #id_empleado = fields.One2one(comodel_name='aplicacion_incidencias.incidencia', string="Incidencia", required=False)