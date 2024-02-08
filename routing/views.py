from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from routing.forms import AddPostForm, AddCatForm, TagForm, OrderForm, ProductForm
from routing.models import Product, Category, Tag, Order
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages


class ProductListView(ListView):
    model = Product
    template_name = 'routing/views/list_of_products.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'routing/views/products_with_details.html'
    context_object_name = 'product'


class ProductCreate(CreateView):
    model = Product
    template_name = 'routing/CRUD_pages/create_Positions.html'
    form_class = ProductForm
    success_url = reverse_lazy('Home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(ProductCreate, self).form_valid(form)


class ProductUpdate(UpdateView):
    model = Product
    template_name = 'routing/views/update_view_products.html'
    form_class = ProductForm
    success_url = reverse_lazy('Home')

    def form_valid(self, form):
        messages.success(self.request, "Продукт был успешно обновлён.")
        return super(ProductUpdate, self).form_valid(form)


class ProductDelete(DeleteView):
    model = Product
    template_name = 'routing/views/delete_view_products.html'
    success_url = reverse_lazy('Home')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_deleted = True
        self.object.save()
        return redirect(self.get_success_url())

    def form_valid(self, form):
        messages.success(self.request, "Продукт был успешно удален.")
        return super(ProductDelete, self).form_valid(form)


class CategoryListView(ListView):
    model = Category
    context_object_name = "categories"
    template_name = 'routing/views/list_of_categories.html'
    paginate_by = 10


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'routing/views/category_detail_view.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category=self.object)
        return context


class TagListView(ListView):
    model = Tag
    context_object_name = "tags"
    template_name = 'routing/views/tags.html'
    paginate_by = 10


class TagDetailView(DetailView):
    model = Tag
    context_object_name = "tag"
    template_name = 'routing/views/tag_detail_view.html'


class TagCreateView(CreateView):
    model = Tag
    template_name = 'routing/CRUD_pages/create_Tag.html'
    form_class = TagForm
    success_url = reverse_lazy('Home')


class OrderListView(ListView):
    model = Order
    context_object_name = "orders"
    template_name = 'routing/views/list_of_orders.html'
    paginate_by = 10


class OrderDetailView(DetailView):
    model = Order
    context_object_name = "order"
    template_name = 'routing/views/order_detail_view.html'


class OrderCreateView(CreateView):
    model = Order
    template_name = 'routing/CRUD_pages/create_Order.html'
    form_class = OrderForm
    success_url = reverse_lazy('Home')


class OrderUpdateView(UpdateView):
    model = Order
    context_object_name = "orders"
    template_name = 'routing/views/order_update_view.html'
    form_class = OrderForm
    success_url = reverse_lazy('Home')


class OrderDeleteView(DeleteView):
    model = Order
    context_object_name = "orders"
    template_name = 'routing/views/order_delete_view.html'
    success_url = reverse_lazy('Home')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_deleted = True
        self.object.save()
        return redirect(self.get_success_url())


def home(request):
    return render(request, 'routing/home.html')  # показывает, какой шаблон необходимо показать при переходе
    # пользователя на данную страницу


def catalogue(request, *args, **kwargs):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'routing/catalogue.html', context)


def tags(request, *args, **kwargs):
    tags = Tag.objects.all()
    context = {'tags': tags}
    return render(request, 'routing/views/tags.html', context)


def all_products(request, *args, **kwargs):
    products = Product.objects.all()
    return render(request, 'routing/views/list_of_products.html', {'products': products})


def product_list_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'routing/product_list.html', {'products': products, 'category': category})


def product_list_by_tag(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    products = Product.objects.filter(tag=tag)
    return render(request, 'routing/products_with_tag_list.html', {'products': products, 'tag': tag})


def my_account(request):
    return render(request, 'routing/my_account.html')


def shopping_cart(request):
    return render(request, 'routing/shopping_cart.html')


def feedback(request):
    return render(request, 'routing/feedback.html')


def API_page(request):
    return render(request, 'routing/API_page.html')


def change_Positions(request):
    return render(request, 'routing/CRUD_pages/change_Positions.html')


def create_Positions(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            new_flower = Product(**form.cleaned_data)
            new_flower.save()
    else:
        form = AddPostForm()

    data = {
        'form': form
    }
    return render(request, 'routing/CRUD_pages/create_Positions.html', data)


def create_Categories(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            new_category = Product(**form.cleaned_data)
            new_category.save()
    else:
        form = AddCatForm()

    data = {
        'form': form
    }
    return render(request, 'routing/CRUD_pages/create_Positions.html', data)


def delete_Positions(request):
    return render(request, 'routing/CRUD_pages/delete_Positions.html')


def read_Positions(request):
    return render(request, 'routing/CRUD_pages/read_Positions.html')


def sign_page(request):
    return render(request, 'routing/sign_page.html')


def agreement_page(request):
    return render(request, 'routing/user_agreement.html')
