from odoo import fields, models

class Incidencia(models.Model):
    _name = "aplicacion_incidencias.incidencia"
    _description = "Tabla de Alex"

    # [ CAMPOS SIMPLES ]
    name = fields.Text(string="Titulo de la incidencia:")
    descripcion = fields.Text(string="Descripcion de la incidencia:")
    fecha_creacion = fields.Date(string="Fecha de creacion:", default=fields.Datetime.now)
    estado_actual = fields.Boolean(string="Incompleta/Completa:", default=False)

    # [ CAMPOS RELACIONALES ]
    # [foreign key]
    estadisticas_ids = fields.Many2many(comodel_name="aplicacion_incidencias.estadisticas", relation="estadisticas_incidencia",
                                        column1="incidencia_id", column2="estadisticas_id", string="Estadísticas Relacionadas")
    id_comentario = fields.One2many(comodel_name="aplicacion_incidencias.comentario",
                                    inverse_name="id_incidencia",
                                    Sgtring="Comentario:",
                                    required=False,
                                    ondelete="cascade")
    com_contenido = fields.Text(related="id_comentario.contenido")
    com_fecha_creacion = fields.Date(related="id_comentario.fecha_creacion")