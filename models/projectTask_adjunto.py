from odoo import fields, models


class ProjectTaskAdjunto(models.Model):
    _inherit = "project.task"

    # Campo One2many para adjuntos
    id_adjunto=fields.One2many(comodel_name="aplicacion_incidencias.adjunto",inverse_name="id_herencia")

    adj_nombre_archivo=fields.Text(string="Nombre del archivo", related="id_adjunto.nombre_archivo")
    adj_ruta_archivo = fields.Text(string="Ruta del archivo", related="id_adjunto.ruta_archivo")
    adj_fecha_subida = fields.Datetime(string="Fecha de subida del archivo", related="id_adjunto.fecha_subida")