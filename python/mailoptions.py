from ipaserver.plugins import user
from ipalib.parameters import Str
from ipalib.text import _

# command line settings for ipa client.
user.user.takes_params = user.user.takes_params + (
    Str(
        "maildeliveroption?",
        cli_name="maildeliveroption",
        label=_("Mail Delivery Option"),
        doc=_(
            "Defines mailDeliveryOption Attribute"
            "Allows mail to be defered, accepted or redirected."
            "See POSTFIX server access table."
        ),
        default="OK",
        autofill=True,
        pattern="^([0-9a-zA-Z\\s]+)$",
        pattern_errmsg="".join(
            'May only contain numbers and letters and spaces'
        ),
    ),
) + (
    Str(
        "mailquota?",
        cli_name="mailquota",
        label=_("Mail Quota Option"),
        doc=_(
            "Defines mailQuota Attribute"
            "Sets the size of the mailbox for the user."
        ),
        default="1G",
        autofill=True,
        pattern="^([0-9]+[MGT])(B?)$",
        pattern_errmsg="".join(
            'May only be possible sizes in the format, [XX..X][M/G/T](B)'
        ),
    ),
)

# add attribute classes to defaults when users are processed
user.user.default_attributes.append("mailDeliveryOption")
user.user.default_attributes.append("mailQuota")


# add structural classes to attributes in cases they are missing. 
def useradd_precallback(self, ldap, dn, entry, attrs_list, *keys, **options):
    entry["objectclass"].append("mailRecipient")
    return dn


user.user_add.register_pre_callback(useradd_precallback)


# add structural classes to attributes in cases they are missing. 
def usermod_precallback(self, ldap, dn, entry, attrs_list, *keys, **options):
    if "objectclass" not in entry.keys():
        old_entry = ldap.get_entry(dn, ["objectclass"])
        entry["objectclass"] = old_entry["objectclass"]
    entry["objectclass"].append("mailRecipient")
    return dn


user.user_mod.register_pre_callback(usermod_precallback)