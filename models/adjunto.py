from odoo import fields, models

class Adjunto(models.Model):
    _name = "aplicacion_incidencias.adjunto"
    _description = 'Tabla de Victor'

    # [ CAMPOS SIMPLES ]
    nombre_archivo=fields.Char(string="Nombre del archivo", required=True)
    ruta_archivo=fields.Reference(string="Ruta del archivo")
    fecha_subida=fields.Datetime(string="Fecha de subida del archivo")

    # [ CAMPOS RELACIONALES ]
    id_comentario=fields.Many2one(comodel_name="plicacion_incidencias.comentario", string="Recibe el id del comentario", required=True, ondelete="cascade")