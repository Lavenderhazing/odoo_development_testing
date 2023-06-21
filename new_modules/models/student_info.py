from odoo import models, fields, api, exceptions, _


class StudentInfo(models.Model):
    _name = "student.info"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Student Info"

    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='Age')
    nrc = fields.Char(string='Nrc')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone Number')
    image = fields.Binary(attachment=True)
    gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')],string='Gender')
    dob = fields.Date(string='Date of Birth')
    nationality = fields.Many2one('res.country',string='Nationality')
    address = fields.Char(string='Address')
    education = fields.Char(string='Major field of study')
    student_types = fields.Selection([
                    ('associate','Associate'),
                    ('bachelor','Bachelor'),
                    ('master','Master'),
                    ('phd','PhD')],string="Types of Students")
    button_age = fields.Integer(string="Value",compute='_compute_age',store=True)



    def action_test(self):
        self.student_types ="bachelor"

    def _compute_age(self):
        for rec in self:
            rec.button_age = 23
        

    def action_test2(self):
        return res

                
