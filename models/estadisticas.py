from odoo import fields, models

class Estadisticas(models.Model):
    _name = "aplicacion_incidencias.estadisticas"
    _description = "Tabla de Kevin"

    # [ CAMPOS SIMPLES ]
    fecha = fields.Date(string="Fecha")
    total_incidencias = fields.Integer(string="Total Incidencias")
    incidencias_finalizadas = fields.Integer(string="Finalizadas")
    tiempo_promedio_resolucion = fields.Integer(string="Promedio Resolucion")

    # [ CAMPOS RELACIONALES ]
    # [foreign key]
    incidencia_ids = fields.Many2many(comodel_name="aplicacion_incidencias.incidencia", relation="estadisticas_incidencia",
                                        column1="estadisticas_id", column2="incidencia_id", string="Incidencias Relacionadas", required=True)