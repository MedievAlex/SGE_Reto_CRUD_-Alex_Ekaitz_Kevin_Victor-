from odoo import fields, models

class ProjectTask_encuesta(models.Model):
    _inherit = "project.task"

    id_encuesta = fields.One2many(comodel_name='aplicacion_incidencias.encuesta', inverse_name='id_herencia', string='Encuesta')