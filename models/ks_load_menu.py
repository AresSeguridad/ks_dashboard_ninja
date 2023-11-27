from odoo import api, fields, models, tools, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    def ks_check_is_enterprise(self):
        ks_temp = False
        if len(self.env['ir.module.module'].sudo().search([('name', '=', 'web_enterprise')]))>0 \
                and self.env['ir.module.module'].sudo().search([('name', '=', 'web_enterprise')],limit=1).state == \
                'installed':
            ks_temp = True
        return ks_temp

