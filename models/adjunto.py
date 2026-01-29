from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Adjunto(models.Model):
    _name = "aplicacion_incidencias.adjunto"
    _description = "Tabla de Victor"

    # [ CAMPOS SIMPLES ]
    nombre_archivo = fields.Text(string="Nombre del archivo", required=True)
    ruta_archivo = fields.Text(string="Ruta del archivo")
    fecha_subida = fields.Datetime(string="Fecha de subida del archivo")

    # [ CAMPOS RELACIONALES ]
    id_comentario=fields.Many2one(comodel_name="aplicacion_incidencias.comentario", string="Comentario", required=True, ondelete="cascade")

    # [ herencia ]
    id_herencia = fields.Many2one(string="Tarea: ", comodel_name="project.task")

    @api.onchange('nombre_archivo')
    def _onchange_methods(self):
        if self.nombre_archivo:
            self.name = self.nombre_archivo
        else:
            self.name=''

    @api.constrains('nombre_archivo')
    def _check_name_lenght(self):
        for nombre in self:
            if nombre.nombre_archivo and len(nombre.nombre_archivo) <10:
                raise ValidationError ('El nombre del archivo es demasiado largo.')

    @api.model
    def create(self, vals):
        if 'fecha_subida' not in vals:
            vals['fecha_subida'] = fields.Datetime.now()
        if 'nombre_archivo' in vals and len(vals['nombre_archivo']) < 10:
            raise ValidationError('El nombre del archivo es demasiado corto.')
        return super(Adjunto,self).create(vals)

    def copy(self, default=None):
        if default is None:
            default = {}
        default['nombre_archivo'] = f"Copia de {self.nombre_archivo}"
        default['fecha_subida'] = fields.Datetime.now()
        default['ruta_archivo'] = f"Copia de {self.ruta_archivo}"
        return super(Adjunto, self).copy(default)

    def write(self, vals):
        if vals.nombre_archivo and len(vals.nombre_archivo) < 10:
            raise ValidationError('El nombre del archivo es demasiado largo.')
        return super(Adjunto,self).write(vals)