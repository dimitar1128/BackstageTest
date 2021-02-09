from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = 'service/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_id'] = 'home'
        return context
