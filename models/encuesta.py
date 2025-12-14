from odoo import fields, models, api
from odoo.exceptions import ValidationError
from datetime import date

class Encuesta(models.Model):
    _name = "aplicacion_incidencias.encuesta"
    _description = "Tabla de Ekaitz"

    # [ CAMPOS SIMPLES ]
    calificacion = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string="Calificación", default='5')
    comentario = fields.Text(string="Comentario")
    fecha_respuesta = fields.Date(string="Fecha", default=fields.Datetime.now)
    state = fields.Selection([
        ('publico', 'Público'),
        ('privado', 'Privado')
    ], string='Estado', default='publico', tracking=True)

    # [ CAMPOS RELACIONALES ]
    # [foreign key]
    x_incidencia_id = fields.Many2one(comodel_name="aplicacion_incidencias.incidencia", string="Incidencia", required=True, ondelete="cascade")

    @api.constrains('fecha_respuesta')
    def _check_fecha_respuesta_no_futura(self):
        for record in self:
            if record.fecha_respuesta and record.fecha_respuesta > date.today():
                raise ValidationError(
                    "La fecha no puede ser posterior a la de hoy."
                )