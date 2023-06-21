from odoo import models, fields, api

class BookOrder(models.Model):
	_name="book.order"
	_inherit = ['mail.thread', 'mail.activity.mixin']
	_description="Book Order"

	date= fields.Date(String="Date", required=True)
	student_id= fields.Many2one("student.info", string="Student Name")
	book_id= fields.Many2one("book.book",string="Book Title")
	price= fields.Float(string="Price", related="book_id.price",readonly=True)
	number_of_book= fields.Integer(string="Number of Book")
	total_amount= fields.Float(string="Total Amount",compute="_compute_amount", store=True, readonly=True)
	amount = fields.Float(string="Copy Amount", compute="_compute_assign_amount",readonly=True)

	@api.depends('price','number_of_book')
	def _compute_amount(self):
		for rec in self:
			rec.total_amount = rec.price * rec.number_of_book


	@api.onchange('total_amount')
	def _compute_assign_amount(self):
		for rec in self:
			rec.amount = rec.total_amount