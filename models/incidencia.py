from datetime import date, datetime

from odoo import fields, models, api

class Incidencia(models.Model):
    _name = "aplicacion_incidencias.incidencia"
    _description = "Tabla de Alex"

    # [ CAMPOS SIMPLES ]
    name = fields.Text(string="Titulo de la incidencia:")
    descripcion = fields.Text(string="Descripcion de la incidencia:", default="Descripción de la Incidencia.")
    descripcion_corta = fields.Text(string="Descripcion de la incidencia:", compute="acortar_descripcion")
    fecha_creacion = fields.Date(string="Fecha de creacion:", default=fields.Datetime.now)
    estado_actual = fields.Boolean(string="Incompleta/Completa:", default=False)

    # [ CAMPOS RELACIONALES ]
    # [foreign key]
    id_estadisticas = fields.Many2many(comodel_name="aplicacion_incidencias.estadisticas", relation="estadisticas_incidencia",
                                        column1="incidencia_id", column2="estadisticas_id", string="Estadísticas Relacionadas")
    id_comentario = fields.One2many(comodel_name="aplicacion_incidencias.comentario", inverse_name="id_incidencia",
                                    string="Comentario:", required=False, ondelete="cascade")

    est_fecha = fields.Date(related="id_estadisticas.fecha")

    com_name = fields.Text(related="id_comentario.name")
    com_contenido = fields.Text(related="id_comentario.contenido")
    com_fecha_creacion = fields.Date(related="id_comentario.fecha_creacion")

    # CAMPO CALCULADO
    @api.depends('descripcion')
    def acortar_descripcion(self):
        for inc in self:
            if len(inc.descripcion) > 50:
                inc.descripcion_corta = inc.descripcion[0:50] + "..."
            else:
                inc.descripcion_corta = inc.descripcion

    # VALIDACIONES
    @api.onchange('fecha_creacion')
    def validar_fecha_creacion(self):
        fecha_hoy = date.today()
        if self.fecha_creacion > fecha_hoy:
            self.fecha_creacion = date.today()

    # RESTRICCIONES
    @api.constrains('')


    # SOBRECARGA
    @api.model
    def create(self, vals):
        if 'name' in vals:
            vals['name'] = vals['name'].upper()
            if vals['descripcion'] is " " or "":
                vals['descripcion'] = "Sin descripción."
            else:
                vals['descripcion'] = vals['descripcion'].capitalize()

        return super(Incidencia, self).create(vals)