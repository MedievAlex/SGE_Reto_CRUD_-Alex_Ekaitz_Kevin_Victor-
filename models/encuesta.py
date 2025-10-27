from odoo import fields, models

class Encuesta(models.Model):
    _name = "aplicacion_incidencias.encuesta"
    _description = "Encuesta de Satisfacción"

    # [ CAMPOS SIMPLES ]
    puntuacion = fields.Integer(string="Puntuación")
    comentario = fields.Text(string="Comentario")
    fecha_respuesta = fields.Date(string="Fecha de respuesta")

    # Relación con Incidencia (Many2one - FK)
    incidencia_id = fields.Many2one(
        comodel_name='aplicacion_incidencias.incidencia',
        string="Incidencia",
        required=True,
        ondelete="cascade"
    )

    # Relación con Empleado (Many2one - FK)
    empleado_id = fields.Many2one(
        comodel_name='aplicacion_incidencias.empleado',
        string="Empleado",
        required=True
    )