from odoo import api, fields, models


class SchoolManagement(models.Model):
    _name = 'school.mng'

    info_collector = fields.Many2one(comodel_name='hr.employee',string='Select someone')

    category = fields.Selection(selection=[('teac', '1-Teacher'), ('adm', '2-Administration'), ('jan', '3-Janitor'), ('stud', '4-Student')])

    doc_grades = fields.Char(string='Grades')
    doc_courses = fields.Char(string='Courses')
    doc_total_hs = fields.Float(string='Total hs in School')
    doc_shift = fields.Selection(selection=[('mor', '1-Morning'), ('aft', '2-Afternoon'), ('ngt', '3-Night'), ('mxd', '4-Mixed')], string='Shift')
    doc_worked_days = fields.Char(string='Worked Days in School')
    doc_condition = fields.Selection(selection=[('act', '1-Active'), ('lic', '2-Under Licence'), ('inact', '3-Inactive')], string='Condition')
    doc_category = fields.Selection(selection=[('tit', '1-Titular'), ('int', '2-Interim'), ('sub','3-Substitute')], string='Category')
    doc_score = fields.Float(string='Score')

    ##########################################################

    non_doc_shift = fields.Selection(selection=[('mor', '1-Morning'), ('aft', '2-Afternoon'), ('ngt', '3-Night'), ('mxd', '4-Mixed')], string='Shift')
    non_doc_total_hs = fields.Float(string='Total hs in School')
    non_doc_condition = fields.Selection(selection=[('act', '1-Active'), ('lic', '2-Under Licence'), ('inact', '3-Inactive')], string='Condition')
    non_doc_category = fields.Selection(selection=[('tit', '1-Titular'), ('int', '2-Interim'), ('sub','3-Substitute')], string='Category')
    non_doc_score = fields.Float(string='Score')

    ########################################################

    student_grade = fields.Char(string='Grade')
    student_condition = fields.Selection(selection=[('prom','1-Promoted'), ('reg','2-Regular'), ('cond', '3-Conditional'), ('rep', '4-Repeater')], string='Condition')
    student_pend_course = fields.Char(string='Pending Courses', default='None')
    student_shift = fields.Selection(selection=[('mor', '1-Morning'), ('aft', '2-Afternoon'), ('ngt', '3-Night')], string='Shift')

