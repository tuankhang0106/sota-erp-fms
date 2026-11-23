# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Ks_dashboard_ninjaBoard(models.Model):
    _name = 'ks_dashboard_ninja.board'
    _description = 'KS_DASHBOARD_NINJA BOARD'
    _order = 'id desc'

    name = fields.Char(string="Dashboard Name", required=True)
    ks_dashboard_items_ids = fields.One2many(comodel_name="ks_dashboard_ninja.item", inverse_name='parent_id', string="Dashboard Items")
    ks_dashboard_menu_name = fields.Char(string="Menu Name")
    ks_dashboard_top_menu_id = fields.Many2one(comodel_name="ir.ui.menu", string="Show Under Menu")
    ks_dashboard_client_action_id = fields.Many2one(comodel_name="ir.actions.client", string="Ks Dashboard Client Action")
    ks_dashboard_menu_id = fields.Many2one(comodel_name="ir.ui.menu", string="Ks Dashboard Menu")
    ks_dashboard_state = fields.Char(string="Ks Dashboard State")
    ks_dashboard_active = fields.Boolean(string="Active")
    ks_dashboard_group_access = fields.Many2many(comodel_name="res.groups", string="Group Access")
    ks_dashboard_start_date = fields.Datetime(string="Start Date")
    ks_dashboard_end_date = fields.Datetime(string="End Date")
    ks_date_filter_selection = fields.Selection(selection=[["l_none","All Time"],["l_day","Today"],["t_week","This Week"],["t_month","This Month"],["t_quarter","This Quarter"],["t_year","This Year"],["td_week","Week to Date"],["td_month","Month to Date"],["td_quarter","Quarter to Date"],["td_year","Year to Date"],["n_day","Next Day"],["n_week","Next Week"],["n_month","Next Month"],["n_quarter","Next Quarter"],["n_year","Next Year"],["ls_day","Last Day"],["ls_week","Last Week"],["ls_month","Last Month"],["ls_quarter","Last Quarter"],["ls_year","Last Year"],["l_week","Last 7 days"],["l_month","Last 30 days"],["l_quarter","Last 90 days"],["l_year","Last 365 days"],["ls_past_until_now","Past Till Now"],["ls_pastwithout_now"," Past Excluding Today"],["n_future_starting_now","Future Starting Now"],["n_futurestarting_tomorrow","Future Starting Tomorrow"],["l_custom","Custom Filter"]], string="Default Date Filter")
    ks_data_formatting = fields.Selection(selection=[["global","Global"],["indian","Indian"],["exact","Exact"]], string="Format")
    ks_gridstack_config = fields.Char(string="Item Configurations")
    ks_dashboard_default_template = fields.Many2one(comodel_name="ks_dashboard_ninja.board_template", string="Dashboard Template")
    ks_set_interval = fields.Selection(selection=[["15000","15 Seconds"],["30000","30 Seconds"],["45000","45 Seconds"],["60000","1 minute"],["120000","2 minute"],["300000","5 minute"],["600000","10 minute"]], string="Default Update Interval", help="Update Interval for new items only")
    ks_dashboard_menu_sequence = fields.Integer(string="Menu Sequence", help="Smallest sequence give high priority and Highest sequence give low priority")
    ks_child_dashboard_ids = fields.One2many(comodel_name="ks_dashboard_ninja.child_board", inverse_name='parent_id', string="Ks Child Dashboard")
    ks_dashboard_defined_filters_ids = fields.One2many(comodel_name="ks_dashboard_ninja.board_defined_filters", inverse_name='parent_id', string="Dashboard Predefined Filters")
    ks_dashboard_custom_filters_ids = fields.One2many(comodel_name="ks_dashboard_ninja.board_custom_filters", inverse_name='parent_id', string="Dashboard Custom Filters")
    multi_layouts = fields.Boolean(string="Enable Multi-Dashboard Layouts", help="Allow user to have multiple layouts of the same Dashboard")
