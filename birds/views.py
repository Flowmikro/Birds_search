from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import BirdModel, AddBirdModel
from .forms import AddBirdForm, BirdForm


@login_required(login_url='/')
def add_new_birds(request):
    error = ''
    if request.method == 'POST':
        form = BirdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('birds_list')
        else:
            error = 'Форма неверна'

    add_form = BirdForm()

    add_data = {
        'add_form': add_form,
        'error': error,
    }
    return render(request, 'birds/add_birds.html', add_data)


@login_required(login_url='/')
def birds_list(request):
    birds = BirdModel.objects.all()
    return render(request, 'birds/birds_list.html', {'birds': birds})


@login_required(login_url='/')
def bird_detail(request, pk):
    bird = BirdModel.objects.get(pk=pk)
    bird_info = AddBirdModel.objects.filter(bird=bird)
    birds_quantity = bird_info.aggregate(Sum('quantity'))['quantity__sum']
    # должно вывести
    # общее количество обнаруженных птиц
    popular_city = bird_info.values('city').annotate(total_quantity=Sum('quantity')).order_by('-total_quantity').first()
    popular_region = bird_info.values('region', 'city').annotate(total_quantity=Sum('quantity')).order_by('-total_quantity').first()
    popular_street = bird_info.values('street', 'region', 'city').annotate(total_quantity=Sum('quantity')).order_by('-total_quantity').first()
    return render(request, 'birds/bird_detail.html', {'bird': bird, 'bird_info': bird_info, 'birds_quantity': birds_quantity, 'popular_region': popular_region, 'popular_city': popular_city, 'popular_street': popular_street})


@login_required(login_url='/')
def bird_post(request):
    error = ''
    if request.method == 'POST':
        form = AddBirdForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('birds_list')
        else:
            error = 'Форма неверна'

    form = AddBirdForm()

    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'birds/bird_post.html', data)


@login_required(login_url='/')
def delete_bird(request, pk):
    bird = get_object_or_404(BirdModel, pk=pk)
    bird.delete()
    return redirect(reverse('birds_list'))