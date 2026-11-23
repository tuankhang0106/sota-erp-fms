# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResUsersRole(models.Model):
    _name = 'res.users.role'
    _description = 'RES USERS ROLE'
    _order = 'id desc'

    group_id = fields.Many2one(comodel_name="res.groups", string="Associated group", required=True, readonly=True)
    line_ids = fields.One2many(comodel_name="res.users.role.line", inverse_name='parent_id', string="Role lines")
    user_ids = fields.One2many(comodel_name="res.users", inverse_name='parent_id', string="Users list", readonly=True)
    rule_ids = fields.Many2many(comodel_name="ir.rule", string="Record Rules", readonly=True)
    rules_count = fields.Integer(string="Rules Count", readonly=True)
    model_access_ids = fields.Many2many(comodel_name="ir.model.access", string="Access Rights", readonly=True)
    model_access_count = fields.Integer(string="Model Access Count", readonly=True)
    group_category_id = fields.Many2one(comodel_name="ir.module.category", string="Associated category", help="Associated group's category")
    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name", required=True)
    users = fields.Many2many(comodel_name="res.users", string="Users")
    model_access = fields.One2many(comodel_name="ir.model.access", inverse_name='parent_id', string="Access Controls")
    rule_groups = fields.Many2many(comodel_name="ir.rule", string="Rules")
    menu_access = fields.Many2many(comodel_name="ir.ui.menu", string="Access Menu")
    view_access = fields.Many2many(comodel_name="ir.ui.view", string="Views")
    comment = fields.Text(string="Comment")
    category_id = fields.Many2one(comodel_name="ir.module.category", string="Application")
    color = fields.Integer(string="Color Index")
    full_name = fields.Char(string="Group Name", readonly=True)
    share = fields.Boolean(string="Share Group", help="Group created to set access rights for sharing data with some users.")
    implied_ids = fields.Many2many(comodel_name="res.groups", string="Inherits", help="Users of this group automatically inherit those groups")
    trans_implied_ids = fields.Many2many(comodel_name="res.groups", string="Transitively inherits", readonly=True)
    role_id = fields.One2many(comodel_name="res.users.role", inverse_name='parent_id', string="Role", help="Relation for the groups that represents a role")
    role_ids = fields.Many2many(comodel_name="res.users.role", string="Roles", readonly=True, help="Roles in which the group is involved")
    parent_ids = fields.Many2many(comodel_name="res.groups", string="Parents", help="Inverse relation for the Inherits field. The groups from which this group is inheriting")
    trans_parent_ids = fields.Many2many(comodel_name="res.groups", string="Parent Groups", readonly=True)
    role_count = fields.Integer(string="# Roles", readonly=True)
