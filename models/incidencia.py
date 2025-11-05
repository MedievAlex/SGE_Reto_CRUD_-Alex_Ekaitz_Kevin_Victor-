from odoo import fields, models

class Incidencia(models.Model):
    _name = "aplicacion_incidencias.incidencia"
    _description = 'Tabla de Alex'

    # [ CAMPOS SIMPLES ]
    titulo = fields.Text(string="Titulo de la incidencia")
    descripcion = fields.Text(string="Descripcion de la incidencia")
    fecha_creacion = fields.Date(string="Fecha de creacion")
    estado_actual = fields.Boolean(string="Estado (Completa/Incompleta)")

    # [ CAMPOS RELACIONALES ]
    # [primary key]
    #id_incidencia = fields.Many2one(comodel_name='aplicacion_incidencias.incidencia', string="Incidencia", required=True, ondelete="cascade")
    # [foreign key]
    #id_departamento = fields.Many2one(comodel_name='departamento', string="Incidencia", required=True, ondelete="cascade")
    # [foreign key]
    #id_empleado_origen = fields.Many2one(comodel_name='empleado_origen', string="Incidencia", required=True, ondelete="cascade")