# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, _

CONST_SETTING_APIKEY = 'weladee-api_key'
CONST_SETTING_HOLIDAY_STATUS_ID = 'weladee-holiday_status_id'
CONST_SETTING_SYNC_EMAIL = 'weladee-sync-email'
CONST_SETTING_APIDB = 'weladee-api_db'

def get_api_key(self):
  '''
  get api key from settings
  return authorization, holiday_status_id

  '''
  line_ids = self.env['ir.config_parameter'].search([('key','like','weladee-%')])
  authorization = False
  holiday_status_id = False
  api_db = False

  for dataSet in line_ids:
      if dataSet.key == CONST_SETTING_APIKEY :
          authorization = [("authorization", dataSet.value)]
      elif dataSet.key == CONST_SETTING_HOLIDAY_STATUS_ID:
          try:
            holiday_status_id = int(float(dataSet.value))
          except:
            pass  
      elif dataSet.key == CONST_SETTING_APIDB:
          api_db = dataSet.value   
          if api_db != self.env.cr.dbname:
             authorization = False
             holiday_status_id = False 

  return authorization, holiday_status_id, api_db

def get_synchronous_email(self):
    '''
    get synchronous email setting    
    '''
    ret = self.env['ir.config_parameter'].search([('key','=',CONST_SETTING_SYNC_EMAIL)])
    if ret:
        return ret.value 
    else:
        self.env['ir.config_parameter'].create({'key':CONST_SETTING_SYNC_EMAIL,'value':''}) 
        return ""

class weladee_settings(models.TransientModel):
    _name="weladee_attendance.synchronous.setting"
    _description="Weladee settings"

    '''
    purpose : get default holiday_status_id
    remarks :
    2017-09-26 CKA created
    2018-06-07 KPO save data
    '''
    def _get_holiday_status(self):
        __, holiday_status_id, __ = get_api_key(self)

        return holiday_status_id

    def _get_api_key(self):
        api_key, __, __ = get_api_key(self)
        
        return (api_key or [['','']])[0][1]

    def _get_email(self):
        return get_synchronous_email(self)


    holiday_status_id = fields.Many2one("hr.holidays.status", String="Leave Type",required=True,default=_get_holiday_status )
    api_key = fields.Char(string="API Key", required=True,default=_get_api_key )
    email = fields.Text('Email', required=True, default=_get_email )
    api_database = fields.Char('API Database',default=lambda s: s.env.cr.dbname)

    def saveBtn(self):
        '''
        write back to parameter
        '''
        line_ids = self.env['ir.config_parameter'].search([('key','like','weladee-%')])

        if len(line_ids) == 0:
           self.env['ir.config_parameter'].create({'key':CONST_SETTING_APIKEY,
                                                   'value': self.api_key}) 
           self.env['ir.config_parameter'].create({'key':CONST_SETTING_HOLIDAY_STATUS_ID,
                                                   'value': self.holiday_status_id.id}) 
           self.env['ir.config_parameter'].create({'key':CONST_SETTING_SYNC_EMAIL,
                                                   'value': self.email}) 
           self.env['ir.config_parameter'].create({'key':CONST_SETTING_APIDB,
                                                   'value': self.api_database}) 
           return

        for each in line_ids:
            if each.key == CONST_SETTING_APIKEY:
               each.write({'value':self.api_key}) 
            elif each.key == CONST_SETTING_HOLIDAY_STATUS_ID:
               each.write({'value':self.holiday_status_id.id})                
            elif each.key == CONST_SETTING_SYNC_EMAIL:
               each.write({'value':self.email})                

weladee_settings()
