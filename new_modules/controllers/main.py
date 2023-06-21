from odoo import http
from odoo.http import request

class StudentData(http.Controller):
	@http.route(['/studentinfo/'], type="http", auth="public", website="True")
	def student_data(self, **post):
		student_data = request.env['student.info'].sudo().search([ ])
		values = {
			'records': student_data
			} 
		return request.render("new_modules.student_pages", values)