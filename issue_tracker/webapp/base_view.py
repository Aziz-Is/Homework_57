from django.views.generic import  TemplateView

class ListView(TemplateView):
    model = None
    context_key = 'objects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_key] = self.model.objects.all()


