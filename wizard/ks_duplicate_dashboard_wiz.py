# -*- coding: utf-8 -*-

from odoo import api, fields, models


class KSCreateDashboardWizard(models.TransientModel):
    _name = 'ks.dashboard.duplicate.wizard'
    _description = 'Duplicate Dashboard Wizard'

    ks_top_menu_id = fields.Many2one('ir.ui.menu', domain="[('parent_id','=',False)]", string="Show Under Menu",
                                     required=True,
                                     default=lambda self: self.env['ir.ui.menu'].search(
                                         [('name', '=', 'My Dashboard')]))

    def DuplicateDashBoard(self):
        '''this function returns acion id of ks.dashboard.duplicate.wizard'''
        action = self.env['ir.actions.act_window']._for_xml_id(
            'ks_dashboard_ninja.ks_duplicate_dashboard_wizard')
        action['context'] = {'dashboard_id': self.id}
        return action

    def ks_duplicate_record(self):
        '''this function duplicates record of ks_dashboard_ninja.board and return dashboard action_id'''
        dashboard_id = self._context.get('dashboard_id')
        dup_dash = self.env['ks_dashboard_ninja.board'].browse(dashboard_id).copy(
            {'ks_dashboard_top_menu_id': self.ks_top_menu_id.id})
        if dup_dash.ks_dashboard_menu_id.parent_id.parent_id:
            top_menu_id = dup_dash.ks_dashboard_menu_id.parent_id.parent_id.id
        else:
            top_menu_id = dup_dash.ks_dashboard_menu_id.parent_id.id
        context = {'ks_reload_menu': True, 'ks_top_menu_id': top_menu_id}
        dash_id = self.env['ks_dashboard_ninja.board'].browse(dashboard_id)
        if not dup_dash.ks_dashboard_items_ids:
            for item in dash_id.ks_dashboard_items_ids:
                item.sudo().copy({'ks_dashboard_ninja_board_id': dup_dash.id})
        # if self._context.get('gridstack_config'):
        #     dup_dash.ks_gridstack_config = json.dumps(self._context.get('gridstack_config'))
        return {
            'type': 'ir.actions.client',
            'name': "Dashboard Ninja",
            'res_model': 'ks_deshboard_ninja.board',
            'params': {'ks_dashboard_id': dup_dash.id},
            'tag': 'ks_dashboard_ninja',
            'context': self.with_context(context)._context
        }


class KSDeleteDashboardWizard(models.TransientModel):
    _name = 'ks.dashboard.delete.wizard'
    _description = 'Delete Dashboard Wizard'

    def DeleteDashBoard(self):
        '''this function returns acion id of ks.dashboard.duplicate.wizard'''
        action = self.env['ir.actions.act_window']._for_xml_id(
            'ks_dashboard_ninja.ks_delete_dashboard_wizard')
        action['context'] = {'dashboard_id': self.id}
        return action

    def ks_delete_record(self):
        '''this function creats record of ks_dashboard_ninja.board and return dashboard action_id'''
        dashboard_id = self._context.get('dashboard_id')
        self.env['ks_dashboard_ninja.board'].browse(dashboard_id).unlink()
        context = {'ks_reload_menu': True,
                   'ks_top_menu_id': self.env['ir.ui.menu'].search([('name', '=', 'My Dashboard')], limit=1).id}
        return {
            'type': 'ir.actions.client',
            'name': "Dashboard Ninja",
            'res_model': 'ks_deshboard_ninja.board',
            'params': {'ks_dashboard_id': 1},
            'tag': 'ks_dashboard_ninja',
            'context': self.with_context(context)._context
        }
