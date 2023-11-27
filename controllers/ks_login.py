from odoo.http import Controller, request, route
from odoo.addons.web.controllers.main import Home
from odoo import http, tools


class KsHome(Home):

    # this is for handle the color and font at login time
    @http.route('/web/login', type='http', auth="none")
    def web_login(self, redirect=None, **kw):
        res = super(KsHome, self).web_login(redirect, **kw)

        ksis_enterprise = request.env['res.company'].sudo().ks_check_is_enterprise()


        if ksis_enterprise:
            template = request.env.ref("ks_dashboard_ninja.ks_dn_load_assets")
            template.sudo().write({
                'active': False
            })
            active_template = request.env.ref("ks_dashboard_ninja.ks_dn_load_assets_en")
            active_template.sudo().write({
                'active': True
            })
        else:
            template = request.env.ref("ks_dashboard_ninja.ks_dn_load_assets_en")
            template.sudo().write({
                'active': False
            })
            active_template = request.env.ref("ks_dashboard_ninja.ks_dn_load_assets")
            active_template.sudo().write({
                'active': True
            })
        return res



