# -*- coding: utf-8 -*-


from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)


class routeusers(models.Model):
  _name = 'routeusers'
  _rec_name = 'name'
  _description = 'routeusers'
  _parent_store = True

  name = fields.Many2one(comodel_name="res.users", domain="[]", index=True, string="Users", required=True)

  parent_path = fields.Char(string="parent_path", index=True)

  parent_id = fields.Many2one('busroutes', 'Parent Route', ondelete='restrict')

  parent_left = fields.Integer('Parent Left', index=True)
  parent_right = fields.Integer('Parent Right', index=True)

  bus_state = fields.Selection(string='bus_state', store=False, related='parent_id.state')


@api.multi
def write(self, values):
  self.ensure_one()
  x = self.env['routeusers'].search_count([('parent_id.id', '=', self.parent_id.id)])
  raise ValidationError(x)
  # Add code here
  return super(busroutes, self).write(values)


_sql_constraints = [('OneUserOnly', 'UNIQUE (name,parent_id)', 'User already exists'), ]
