from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from mezzanine.conf import register_setting

# Did you know? If you forget to import settings, above, then,
# well this works...until these settings disappear!
# Also, do not panic if settings disappear when a dev server
# is shut down: they only seem to be persisted when
# in production.

register_setting(
    name="MOLLOM_PUBLIC_KEY",
    label=_("Mollom API Public Key"),
    description=_("API Public Key"),
    editable=True,
    default="",
)

register_setting(
    name="MOLLOM_PRIVATE_KEY",
    label=_("Mollom API Private Key"),
    description=_("API Private Key"),
    editable=True,
    default="",
)

register_setting(
    name="MOLLOM_DEFAULT_SERVER",
    label=_("Mollom Default Server"),
    description=_(
        "Only enter a value if Mollom is unable to talk to its default server."
        "Typically, this default value is 'xmlrpc.mollom.com' "
        "but if that server is unresponsive, you may try, "
        "for instance, 'xmlrpc3.mollom.com'"),
    editable=True,
    default="",
)
