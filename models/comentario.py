from odoo import fields, models

class Comentario(models.Model):
    _name = "aplicacion_incidencias.comentario"
    _description = 'Tabla de Alex'

    # [ CAMPOS SIMPLES ]
    contenido = fields.Text(String="Comentario")
    fecha_creacion = fields.Date(String="Fecha de creacion")

    # [ CAMPOS RELACIONALES ]
    # [primary key]
    #id_comentario
    # [foreign key]
    id_incidencia = fields.Many2one(comodel_name='aplicacion_incidencias.incidencia', string="Incidencia", required=True, ondelete="cascade")
    # [foreign key]
    #id_adjunto = fields.One2many(comodel_name='aplicacion_incidencias.adjunto', string="Adjunto", required=True, ondelete="cascade")