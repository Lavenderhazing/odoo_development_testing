from odoo import api, fields, models, tools

class OrderReport(models.Model):
    _name = 'order.report'
    _description = 'Order Report'
    _auto = False
   
    date = fields.Date(string='Order Date')
    student_id = fields.Many2one('student.info','Student Name')
    book_id = fields.Many2one('book.book','Book Name')
    book_number = fields.Integer(string="Number of Book")
    total_amount = fields.Float(string="Total Amount")

    def init(self):
        tools.drop_view_if_exists(self.env.cr, 'order_report')
        self.env.cr.execute(""" 
            CREATE OR REPLACE VIEW order_report AS (
                SELECT
                    row_number() OVER () AS id,
                    Line.student_id,
                    Line.book_id,
                    Line.book_number,
                    Line.total_amount,
                    Line.date
                    FROM (
                        SELECT
                            book_order.date as date,
                            book_order.student_id as student_id,
                            book_order.book_id as book_id,
                            book_order.number_of_book as book_number,
                            book_order.total_amount as total_amount
                            FROM book_order 
                            group by 
                            book_order.date,book_order.student_id,book_order.book_id,book_order.number_of_book,book_order.total_amount
                    ) as line 
            )
        """)