define([ 'freeipa/phases', 'freeipa/user'], function(phases, user_mod) {

// helper function
function get_item(array, attr, value) {
        for (var i=0,l=array.length; i<l; i++) {
                if (array[i][attr] === value)
                        return array[i];
                }
                return null;
}

var mail_options_plugin = {};

// adds nextcloud quota field into user account facet
mail_options_plugin.add_mailoptions = function() {
        var facet = get_item(user_mod.entity_spec.facets, '$type', 'details');
        var section = get_item(facet.sections, 'name', 'identity');
        section.fields.push({
            name: 'maildeliveryoption',
            label: 'Mail Delivery Option',
            flags: ['w_if_no_aci']
        },
        {
            name: 'mailquota',
            label: 'Mail Quota',
            flags: ['w_if_no_aci']
        });
        return true;
};

phases.on('customization', mail_options_plugin.add_mailoptions);

return mail_options_plugin;
});