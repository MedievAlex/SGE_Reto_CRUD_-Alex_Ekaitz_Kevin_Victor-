from odoo import fields, models

class Incidencia(models.Model):
    _name = "aplicacion_incidencias.incidencia"
    _description = "Tabla de Alex"

    # [ CAMPOS SIMPLES ]
    titulo = fields.Text(string="Titulo de la incidencia:")
    descripcion = fields.Text(string="Descripcion de la incidencia:")
    fecha_creacion = fields.Date(string="Fecha de creacion:", default=fields.Datetime.now)
    estado_actual = fields.Boolean(string="Incompleta/Completa:", default=False)

    # [ CAMPOS RELACIONALES ]
    # [foreign key]
    estadisticas_ids = fields.Many2many(comodel_name="aplicacion_incidencias.estadisticas", relation="estadisticas_incidencia",
                                        column1="incidencia_id", column2="estadisticas_id", string="Estadísticas Relacionadas")
    # [foreign key]
    # id_empleado = fields.Many2one(comodel_name='hr.hr_employee', string="Incidencia", required=True, ondelete="cascade")
    # [foreign key]
    # id_departamento = fields.Many2one(comodel_name='hr.hr_department', string="Incidencia", required=True, ondelete="cascade")