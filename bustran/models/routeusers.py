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

  parent_id = fields.Many2one('busroutes', 'Parent Route', ondelete='restrict',required=True)

  parent_left = fields.Integer('Parent Left', index=True)
  parent_right = fields.Integer('Parent Right', index=True)

  bus_state = fields.Selection(string='Route Status', store=False, related='parent_id.state')
  bus_name =  fields.Char(string='Bus name', store=False, related='parent_id.parent_id.name')
  Route_name = fields.Char(string='Route Name', store=False, related='parent_id.name')

  @api.model
  def create(self,values):
    pid= values['parent_id']
    n =  values['name']
    #raise ValidationError(str(n))
    ishaveanotherres = self.env['routeusers'].search_count([('name', '=', n),("bus_state","=","InProgress")])

    if ishaveanotherres >0:
      raise ValidationError("You Have another Reservation")
    routestat = self.env['busroutes'].search([('id', '=', pid)], limit=1).state
    if(routestat != "InProgress"):
      raise ValidationError("This Route is not available for reservation ")


    current = self.env['routeusers'].search_count([('parent_id', '=', pid)])
    capacity = self.env['busroutes'].search([('id', '=', pid)], limit=1).capacity

    if(current>=capacity):
      raise ValidationError("Max Reached : " + str(current)  )
    #raise ValidationError()
    if(self.parent_id.parent_id.capacity>len(self.parent_id.child_ids)):
      raise ValidationError("Max Reached")

    return super(routeusers,self).create(values)

  @api.multi
  def write(self, values):
    #raise ValidationError("hi")


    # Add code here
    return super(routeusers, self).write(values)


  _sql_constraints = [('OneUserOnly', 'UNIQUE (name,parent_id)', 'User already exists'), ]
