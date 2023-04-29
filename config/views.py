from django.urls import reverse_lazy
from django.views.generic import RedirectView

class LandingPageRedirectView(RedirectView):
    url = reverse_lazy('plates:index')

redirect_to_landing_page = LandingPageRedirectView.as_view()