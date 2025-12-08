from odoo import fields, models

class Encuesta(models.Model):
    _name = "aplicacion_incidencias.encuesta"
    _description = "Tabla de Ekaitz"

    # [ CAMPOS SIMPLES ]
    puntuacion = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string="Puntuación", default='5')
    comentario = fields.Text(string="Comentario")
    fecha_respuesta = fields.Date(string="Fecha", default=fields.Datetime.now)

    # [ CAMPOS RELACIONALES ]
    # [foreign key]
    x_incidencia_id = fields.Many2one(comodel_name="aplicacion_incidencias.incidencia", string="Incidencia", required=True, ondelete="cascade")