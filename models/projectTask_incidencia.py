from odoo import fields, models

class ProjectTask_incidencia(models.Model):
    _inherit = "project.task"

    id_incidencia = fields.One2many(comodel_name='aplicacion_incidencias.incidencia', inverse_name='id_herencia',
                                    string='Incidencias')

    inc_name = fields.Text(comodel_name="aplicacion_incidencias.incidencia", related="id_incidencia.name")
    inc_descripction = fields.Text(comodel_name="aplicacion_incidencias.incidencia", related="id_incidencia.descripcion")