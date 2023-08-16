from django.db.models import Sum
from django.shortcuts import get_object_or_404

from birds.models import BirdModel, AddBirdModel


def _validate_form(form):
    """Проверяем правильность заполнения формы"""
    if form.is_valid():
        form.save()
        return True
    return False


def _birds_list_db():
    """Выводим все поля их BirdModel"""
    return BirdModel.objects.all()


def _delete_bird_db(pk):
    """Позволяет удалить птицу из БД"""
    bird = get_object_or_404(BirdModel, pk=pk)
    bird.delete()


def _get_info_bird_db(pk):
    """Составляем статистику по количеству птиц"""
    bird = BirdModel.objects.get(pk=pk)
    bird_info = AddBirdModel.objects.filter(bird=bird)
    birds_quantity = bird_info.aggregate(Sum('quantity'))['quantity__sum']
    #  должно вывести общее количество обнаруженных птиц
    popular_city = bird_info.values('city').annotate(total_quantity=Sum('quantity')).order_by(
        '-total_quantity').first()  # самый популярный город
    popular_region = bird_info.values('region', 'city').annotate(total_quantity=Sum('quantity')).order_by(
        '-total_quantity').first()  # самый популярный регион И город
    popular_street = bird_info.values('street', 'region', 'city').annotate(total_quantity=Sum('quantity')).order_by(
        '-total_quantity').first()  # самая популярная улица И регион И город

    data = {
        'bird': bird, 'bird_info': bird_info, 'birds_quantity': birds_quantity,
        'popular_region': popular_region, 'popular_city': popular_city, 'popular_street': popular_street
    }

    return data
