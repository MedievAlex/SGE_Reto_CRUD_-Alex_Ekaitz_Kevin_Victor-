from datetime import date

from odoo import fields, models, api

class Comentario(models.Model):
    _name = "aplicacion_incidencias.comentario"
    _description = "Tabla de Alex"

    # [ CAMPOS SIMPLES ]
    name = fields.Text(string="Nombre:")
    contenido = fields.Text(string="Comentario:")
    contenido_corto = fields.Text(string="Comentario:", compute="acortar_contenido")
    fecha_creacion = fields.Date(string="Fecha de creacion:", readonly=True, default=fields.Datetime.now)

    # [ CAMPOS RELACIONALES ]
    # [foreign key]
    id_incidencia = fields.Many2one(comodel_name="aplicacion_incidencias.incidencia", string="Incidencia", required=True, ondelete="cascade")

    inc_name = fields.Text(related="id_incidencia.name")
    inc_estado_actual = fields.Boolean(related="id_incidencia.estado_actual")

    @api.depends('contenido')
    def acortar_contenido(self):
        for com in self:
            if len(com.contenido) > 50:
                com.contenido_corto = com.contenido[0:50] + "...";
            else:
                com.contenido_corto = com.contenido;

    @api.onchange('fecha_creacion')
    def validar_fecha_creacion(self):
        fecha_hoy = date.today();
        if self.fecha_creacion > fecha_hoy:
            self.fecha_creacion = date.today();