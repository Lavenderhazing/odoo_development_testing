# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class new_modules(models.Model):
#     _name = 'new_modules.new_modules'
#     _description = 'new_modules.new_modules'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
