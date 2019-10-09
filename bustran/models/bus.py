# -*- coding: utf-8 -*-


from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class bus(models.Model):

    _name = 'bus'
    _rec_name = 'name'
    _description = 'Buses'

    name = fields.Char(string="Bus Name", required=False, index=True)
    owner = fields.Many2one(comodel_name="res.users", domain="[]", index=True,string="Owner", required=False)
    capacity = fields.Integer(string="Capacity", required=False)
    child_ids  = fields.One2many(comodel_name="busroutes", inverse_name="parent_id", string="routes", required=False)

    members_ids = fields.One2many(comodel_name="busmembers", inverse_name="parent_id", string="Members", required=False)
