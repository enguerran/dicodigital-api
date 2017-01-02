import django_filters as filters
from random import randint
from . import models


class WordFilter(filters.FilterSet):

    creator = filters.CharFilter(name='creator__username')
    first = filters.ModelChoiceFilter(method='search_by_first_letter')
    def_like = filters.ModelChoiceFilter(method='search_by_word_in_definition')
    empty = filters.ModelChoiceFilter(method='search_without_definition')
    random = filters.ModelChoiceFilter(method='get_random_word')

    class Meta:
        model = models.Word
        fields = ['label', 'creator', 'first', 'def_like']

    def search_by_first_letter(self, queryset, value):
        return queryset.filter(label__istartswith=value)

    def search_by_word_in_definition(self, queryset, value):
        return queryset.filter(definitions__text__icontains=value)

    def search_without_definition(self, queryset, value):
        empty = True if value == 'true' else False
        return queryset.filter(definitions__isnull=empty)

    def get_random_word(self, queryset, value):
        ids = [word.id for word in queryset.all()]
        if len(ids) > 1:
            return queryset.filter(id=randint(ids[0], ids[-1]))
        return queryset
