from odoo import fields, models

class ProjectTask_incidencia(models.Model):
    _inherit = "project.task"

    incidencia_id = fields.One2many(comodel_name='aplicacion_incidencias.incidencia', inverse_name='proyecto',
                                    string='Incidencias')

    nombre = fields.Char(comodel_name="Nombre", related="incidencia_id.name")
    descripcion = fields.Char(comodel_name="Descripcion", related="incidencia_id.descripcion")