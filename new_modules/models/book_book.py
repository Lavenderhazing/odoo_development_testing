from odoo import models,fields,api

class Book(models.Model):
	_name = "book.book"
	_inherit = ['mail.thread', 'mail.activity.mixin']
	_description = "Book Info"
	_rec_name = "title"
     
   
	title = fields.Char(string="Book Title")
	author = fields.Char(string="Book's Author")
	category = fields.Selection([('history','History'),('potery','Potery'),('bio','Biography'),('sci','Science'),('art','Art'),('Novel','novel'),('other','Other')],string="Category")
	pages = fields.Text(string="Number of Pages")
	language = fields.Selection([('eng','English'),('myan','myanmar'),('korea','korea')],string="Language")
	country = fields.Many2one('res.country',string="Country")
	price = fields.Float(string="Price")
	image = fields.Binary(string='Photo', attachment=True)
	page = fields.Integer(string="Number of Pages")
