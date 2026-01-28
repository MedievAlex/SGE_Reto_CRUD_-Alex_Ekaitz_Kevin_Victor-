from odoo import fields, models

class ProjectTask_Estadisticas(models.Model):
    _inherit = "project.task"

    id_estadisticas = fields.One2many(comodel_name='aplicacion_incidencias.estadisticas', inverse_name='id_herencia', string='Estadisticas')