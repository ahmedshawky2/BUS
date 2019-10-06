# -*- coding: utf-8 -*-


from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)


class busroutes(models.Model):
  _name = 'busroutes'
  _rec_name = 'name'
  _description = 'routes'
  _parent_store = True

  name = fields.Char(string="Route Name", required=False, index=True)
  startdate = fields.Datetime(string="Start Date", required=False)
  parent_path = fields.Char(string="parent_path", index=True)

  state = fields.Selection(string="Status", selection=[('New', 'New'), ('InProgress', 'InProgress'), ('End', 'End')],
                           required=False)
  parent_id = fields.Many2one('bus', 'Parent Bus', ondelete='restrict')
  capacity = fields.Integer(string='Capacity', store=False, related='parent_id.capacity')

  parent_left = fields.Integer('Parent Left', index=True)
  parent_right = fields.Integer('Parent Right', index=True)
  child_ids = fields.One2many(comodel_name="routeusers", inverse_name="parent_id", string="Users", required=False)
