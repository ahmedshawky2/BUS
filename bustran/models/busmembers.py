# -*- coding: utf-8 -*-


from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)


class busmembers (models.Model):
  _name = 'busmembers'
  _rec_name = 'name'
  _description = 'busmembers'
  _parent_store = True

  name = fields.Many2one(comodel_name="res.users", domain="[]", index=True, string="Users", required=True)

  parent_path = fields.Char(string="parent_path", index=True)

  parent_id = fields.Many2one('bus', 'Bus', ondelete='restrict',required=True)

  parent_left = fields.Integer('Parent Left', index=True)
  parent_right = fields.Integer('Parent Right', index=True)


  _sql_constraints = [('OneUserOnly', 'UNIQUE (name,parent_id)', 'User already exists'), ]
