from odoo import fields, models

class Adjunto(models.Model):
    _name = "aplicacion_incidencias.adjunto"
    _description = "Tabla de Victor"

    # [ CAMPOS SIMPLES ]
    nombre_archivo = fields.Text(string="Nombre del archivo", required=True)
    ruta_archivo = fields.Text(string="Ruta del archivo")
    fecha_subida = fields.Datetime(string="Fecha de subida del archivo")

    # [ CAMPOS RELACIONALES ]
    id_comentario=fields.Many2one(comodel_name="aplicacion_incidencias.comentario", string="Comentario", required=True, ondelete="cascade")