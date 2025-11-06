from odoo import fields, models

class Comentario(models.Model):
    _name = "aplicacion_incidencias.comentario"
    _description = "Tabla de Alex"

    # [ CAMPOS SIMPLES ]
    contenido = fields.Text(string="Comentario")
    fecha_creacion = fields.Date(string="Fecha de creacion")

    # [ CAMPOS RELACIONALES ]
    # [foreign key]
    id_incidencia = fields.Many2one(comodel_name="aplicacion_incidencias.incidencia", string="Incidencia", required=True, ondelete="cascade")