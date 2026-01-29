from datetime import date
from odoo import fields, models, api
from odoo.exceptions import ValidationError

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

    # [ herencia ]
    id_herencia = fields.Many2one(string="Tarea: ", comodel_name="project.task")

    # =========================
    # VALIDACIONES
    # =========================

    # validación en formulario
    @api.onchange('incidencias_finalizadas', 'total_incidencias')
    def _onchange_incidencias(self):
        if self.incidencias_finalizadas > self.total_incidencias:
            self.incidencias_finalizadas = self.total_incidencias

    # validación en BD
    @api.constrains('total_incidencias', 'incidencias_finalizadas')
    def _check_incidencias(self):
        for record in self:
            if record.total_incidencias < 0:
                raise ValidationError("El total de incidencias no puede ser negativo.")
            if record.incidencias_finalizadas < 0:
                raise ValidationError("Las incidencias finalizadas no pueden ser negativas.")
            if record.incidencias_finalizadas > record.total_incidencias:
                raise ValidationError(
                    "Las incidencias finalizadas no pueden superar el total."
                )

    # =========================
    # SOBRECARGA
    # =========================

    @api.model
    def create(self, vals):
        # Asegurar fecha (seguimiento diario)
        if not vals.get('fecha'):
            vals['fecha'] = date.today()

        return super(Estadisticas, self).create(vals)