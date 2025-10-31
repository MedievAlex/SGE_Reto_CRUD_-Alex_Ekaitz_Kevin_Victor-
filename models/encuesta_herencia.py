from odoo import fields, models

class EncuestaHerencia(models.Model):
    _name = "aplicacion_incidencias.encuesta_herencia"
    _description = "Encuesta Herencia"
    _inherit = "aplicacion_incidencias.encuesta"

    # [ CAMPOS SIMPLES ]
    tiempo_realizacion = fields.Integer(string="Tiempo de Realización (minutos)")
    idioma = fields.Selection([('es', 'Español'), ('en', 'Inglés'), ('eu', 'Euskera')], string="Idioma", default='es')