import logging
from mezzanine.utils import views
from mezzanine.conf import settings
from django.forms import Textarea
from Mollom import MollomAPI
from Mollom import MollomFault


def is_spam_mollom(request, form, url):
    def logit(msg):
        if settings.DEBUG:
            logger = logging.getLogger(__name__)
            logger.info(msg)

    settings.use_editable()  # Re-eval setting every time
    if not settings.MOLLOM_PUBLIC_KEY or not settings.MOLLOM_PRIVATE_KEY:
        return False
    else:
        comment = None
        for name, field in form.fields.items():
            if isinstance(field.widget, Textarea):
                comment = form.cleaned_data.get(name)
                break
        if comment is None:
            return False
        else:
            if not settings.MOLLOM_DEFAULT_SERVER:
                mollom_api = MollomAPI(
                    publicKey=str(settings.MOLLOM_PUBLIC_KEY),
                    privateKey=str(settings.MOLLOM_PRIVATE_KEY))
            else:
                mollom_api = MollomAPI(
                    publicKey=str(settings.MOLLOM_PUBLIC_KEY),
                    privateKey=str(settings.MOLLOM_PRIVATE_KEY),
                    defaultServer="http://%s" % settings.MOLLOM_DEFAULT_SERVER)
            if not mollom_api.verifyKey():
                raise MollomFault('Your MOLLOM credentials are invalid.')
            cc = mollom_api.checkContent(postBody=comment)
            if cc['spam'] == 2:
                logit("MOLLOM::SPAM: %s" % comment)
                return True
            elif cc['spam'] == 3:
                logit("MOLLOM::not sure: %s" % comment)
                return False
            else:
                logit("MOLLOM::ham: %s" % comment)
                return False
