from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, ListView, TemplateView
from rest_framework import viewsets

from app.forms import OrderForm
from app.models import Order
from app.serializers import OrderSerializer


class OrderAPIViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class IndexView(TemplateView):
    template_name = 'app/index.html'


class OrderListView(ListView):
    model = Order
    template_name = 'app/order_list.html'
    context_object_name = 'orders'


class OrderDetailView(DetailView):
    model = Order
    template_name = 'app/order_detail.html'
    context_object_name = 'order'


class OrderAddFormView(FormView):
    form_class = OrderForm
    template_name = 'app/order_form.html'
    success_url = reverse_lazy('order-list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
