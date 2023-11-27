odoo.define('ks_dashboard_ninja.ks_form_renderer', function (require) {
    "use strict";

    var FormView = require('web.FormRenderer');
    var FormController = require('web.FormController');

    FormView.include({
        updateState: function (state, params) {
            var ks_form_view =this._super.apply(this, arguments);
            if(state.model == 'ks_dashboard_ninja.board'){
                if(odoo.session_info.server_version == "14.0+e"){
                    this.trigger_up('ks_reload_menu_data_enterprise');
                }
                else if(odoo.session_info.server_version == "14.0"){
                        this.trigger_up('ks_reload_menu_data');
                    }
            }

            return ks_form_view
    },

    });

    FormController.include({

       createRecord: async function (parentID, additionalContext) {
          var self= this;
          if(self.modelName == 'ks_dashboard_ninja.board'){
            this._rpc({
              model: 'ks.dashboard.wizard',
              method: "CreateDashBoard",
              args: [''],
              }).then((result)=>{
                 self.do_action(result)
              });
          }
          else{
            this._super.apply(this, arguments);
          }

        },

    });


    return FormView,FormController;
});