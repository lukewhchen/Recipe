from django.shortcuts import render, redirect
from .models import Ingredient
from .forms import IngredientForm
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('A New Recipe Has Been Established!'))

    all_items = Ingredient.objects.all().order_by('-id')
    return render(request, 'index.html', {'all_items': all_items})


def delete(request, ingredient_id):
    obj = Ingredient.objects.get(pk=ingredient_id)
    name = obj.name
    obj.delete()
    messages.success(request, (name + ' Has Been Deleted!'))
    return redirect('index')

def update(request, ingredient_id):
    obj = Ingredient.objects.get(pk=ingredient_id)
    name = obj.name
    obj.content = request.POST['update']
    obj.save()
    messages.success(request, (name + ' Ingredients Have Been Updated!'))
    return redirect('index')
