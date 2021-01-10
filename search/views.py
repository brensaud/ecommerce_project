from django.shortcuts import render
from django.views.generic import ListView

from products.models import Product
# Create your views here.
#class based generics views
class SearchProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'search/view.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     return context
    
    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q', None)
        if query is not None:
            return Product.objects.filter(title__icontains='hat')
        return Product.objects.featured()
