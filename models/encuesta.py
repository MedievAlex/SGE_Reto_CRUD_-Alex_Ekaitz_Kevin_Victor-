from odoo import fields, models, api
from odoo.exceptions import ValidationError
from datetime import date

class Encuesta(models.Model):
    _name = "aplicacion_incidencias.encuesta"
    _description = "Tabla de Ekaitz"

    # [ CAMPOS SIMPLES ]
    calificacion = fields.Selection([
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5")
    ], string="Calificación", default="5")
    comentario = fields.Text(string="Comentario")
    comentario_corto = fields.Text(string="Comentario", compute="_depends_acortar_comentario")
    fecha_respuesta = fields.Date(string="Fecha", required=True)
    estado = fields.Selection([
        ("publico", "Público"),
        ("privado", "Privado")
    ], string="Estado", default="privado", tracking=True)

    # [ CAMPOS RELACIONALES ]
    # [foreign key]
    x_incidencia_id = fields.Many2one(comodel_name="aplicacion_incidencias.incidencia", string="Incidencia", required=True, ondelete="cascade")
    inc_name = fields.Text(related="x_incidencia_id.name")

     # [ herencia ]
    id_herencia = fields.Many2one(string="Tarea: ", comodel_name="project.task")

    # VALIDACIONES
    @api.constrains("fecha_respuesta")
    def _check_fecha_respuesta_no_futura(self):
        for record in self:
            if record.fecha_respuesta and record.fecha_respuesta > date.today():
                raise ValidationError(
                    "La fecha no puede ser posterior a la de hoy."
                )

    @api.onchange("fecha_respuesta")
    def _onchange_fecha_respuesta(self):
        if not self.fecha_respuesta and self._origin.fecha_respuesta:
            return {
                "warning": {
                    "title": "Atención",
                    "message": "No puede dejar la fecha vacía."
                }
            }
        return None

    @api.depends("comentario")
    def _depends_acortar_comentario(self):
        for enc in self:
            if enc.comentario:
                if len(enc.comentario) > 100:
                    enc.comentario_corto = enc.comentario[:100] + "..."
                else:
                    enc.comentario_corto = enc.comentario
            else:
                enc.comentario_corto = ""

    # SOBRECARGA
    @api.model
    def create(self, vals):
        comentario = vals.get("comentario")
        if comentario:
            vals["comentario"] = comentario.capitalize()
        return super().create(vals)
