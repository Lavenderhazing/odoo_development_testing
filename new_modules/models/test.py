from odoo import models, fields, api, exceptions, _


class Test(models.Model):
    _name = "test.test"
    _description = "Test modules"

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    image = fields.Binary(strin="Photo", attachment=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
