odoo.define('ks_dashboard_ninja.ks_list_renderer', function (require) {
    "use strict";

    var ListView = require('web.ListRenderer');
    var ListController = require('web.ListController');
    var ajax = require('web.ajax');

     ListView.include({
        updateState: function (state, params) {
            var ks_list_view =this._super.apply(this, arguments);
            if (state.model == 'ks_dashboard_ninja.board'){
                if(odoo.session_info.server_version == "14.0+e"){
                        this.trigger_up('ks_reload_menu_data_enterprise');
                    }
                else if(odoo.session_info.server_version == "14.0"){
                        this.trigger_up('ks_reload_menu_data');
                    }
            }
            return ks_list_view
    },

    });

    ListController.include({

       _onCreateRecord: function (ev) {
          var self= this;
          if ($(ev.currentTarget).hasClass('o_list_button_add') && self.modelName == 'ks_dashboard_ninja.board'){
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


    return ListView,ListController;

});