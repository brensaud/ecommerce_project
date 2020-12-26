from django.http import Http404
from django.views.generic import ListView, DetailView

from django.shortcuts import render,get_object_or_404
from .models import Product

#class based generics views
class ProductFeaturedView(ListView):
    template_name = 'products/product_list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()

class ProductFeaturedDetailView(ListView):
    queryset = Product.objects.featured()
    template_name = 'products/featured-detail.html'

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()


#class based generics views
class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/product_list.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     return context
    
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

# function based views
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list':queryset,
    }
    return render(request, 'products/product_list.html', context)




class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/product_detail.html'

    def get_object(self, *arg, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        instance = get_object_or_404(Product, slug=slug, active=True)
        # if instance is None:
        #     raise Http404('Product does not exist')
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404('Not Found')
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
            return instance
        except:
            raise Http404('Uhmmmmma')

        return instance


#class based generics views
class ProductDetailView(DetailView):
    #queryset = Product.objects.all() # This is not need after we implement our own get_context usin custom ModelManager
    template_name = 'products/product_detail.html'


    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        return context

    def get_object(self, *arg, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk) # using custom model manager
        if instance is None:
            raise Http404('Product does not exist')
        return instance
    

# function based views'
def product_detail_view(request, pk=None, *args, **kwargs):
    # try:
    #     instance = Product.objects.get(pk=pk)
    # except Product.DoesNotExist:
    #     raise Http404('Product does not exist')


    instance = Product.objects.get_by_id(pk) # using custom model manager
    if instance is None:
        raise Http404('Product does not exist')

    # qs = Product.objects.filter(id=pk)
    # # more relevant we it return multiple object like title='biren'
    # # qs = product.object.filter(name='man')
    # if qs.exists() and qs.count() == 1: # len(qs) #but qeryset has method count is more efficent for database
    #     instance = qs.first()
    # else:
    #     raise Http404('Product does\'t exist')


    # hand the execption if object is not found
    #instance = get_object_or_404(Product, pk=pk)
    #print(args)
    #print(kwargs)
    context = {
        'object': instance,
    }
    return render(request, 'products/product_detail.html', context)