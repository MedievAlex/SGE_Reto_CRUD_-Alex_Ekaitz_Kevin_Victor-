from odoo import fields, models

class Comentario(models.Model):
    _name = "aplicacion_incidencias.comentario"
    _description = "Tabla de Alex"

    # [ CAMPOS SIMPLES ]
    name = fields.Text(string="Nombre:")
    contenido = fields.Text(string="Comentario:")
    fecha_creacion = fields.Date(string="Fecha de creacion:", readonly=True, default=fields.Datetime.now)

    # [ CAMPOS RELACIONALES ]
    # [foreign key]
    id_incidencia = fields.Many2one(comodel_name="aplicacion_incidencias.incidencia", string="Incidencia", required=True, ondelete="cascade")
    inc_name = fields.Text(related="id_incidencia.name")
    inc_estado_actual = fields.Boolean(related="id_incidencia.estado_actual")