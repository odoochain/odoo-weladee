# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging
_logger = logging.getLogger(__name__)

from odoo import osv
from odoo import models, fields, api

class weladee_task(models.Model):
    _inherit = 'project.task'

    weladee_id = fields.Char(string="Weladee ID",copy=False)
    hide_edit_btn_css = fields.Html(string='css', sanitize=False, compute='_compute_css')

    @api.model
    def create(self, vals):
        name_th = vals.get('name-th', '') 
        if 'name-th' in vals: del vals['name-th']
        ret = super(weladee_task, self).create(vals)
        irobj = self.env['ir.translation']

        irobj._set_ids('project.task,name','model','en_US', [ret.id], vals.get('name', ''))
        irobj._set_ids('project.task,name','model','th_TH', [ret.id], name_th)

        return ret
    
    @api.depends('weladee_id')
    def _compute_css(self):
        for record in self:
            if self.weladee_id:
                record.hide_edit_btn_css = '<style>.o_form_button_edit {display: none !important;}</style>'
            else:
                record.hide_edit_btn_css = False