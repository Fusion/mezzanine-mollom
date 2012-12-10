An anti spam module for Mezzanine.

To install:

Open <mezzanine home>/settings.py

Add or edit:

    SPAM_FILTERS = (
        "mezzanine.utils.views.is_spam_akismet",
        "mollom.filters.is_spam_mollom",
    )

To configure:

Edit Mollom settings in admin control panel.
