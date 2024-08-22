from django.contrib import admin
from .models import Movie,Director,Actor,DressingRoom
from django.db.models import QuerySet
# Register your models here.
admin.site.register(Director)
admin.site.register(Actor)
# admin.site.register(DressingRoom)
@admin.register(DressingRoom)
class DressingRoomAdmin(admin.ModelAdmin):
    list_display = ['floor','number','actor']
class RatingFilter(admin.SimpleListFilter):
    title = 'Фильмы по рейтингу'
    parameter_name = 'qwerty'
    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низкий'),
            ('от 40 до 59', 'Средний'),
            ('от 60 до 79', 'Высокий'),
            ('>=80', 'Максимальный'),
        ]
    def queryset(self, request, queryset: QuerySet):
        if self.value()=='<40':
            return queryset.filter(ratings__lt=40)
        if self.value()=='от 40 до 59':
            return queryset.filter(ratings__gte=40).filter(ratings__lt=60)
        if self.value()=='от 60 до 79':
            return queryset.filter(ratings__gte=60).filter(ratings__lt=80)
        if self.value()=='>=80':
            return queryset.filter(ratings__gte=80)


        return queryset





@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields=['name','ratings']
    prepopulated_fields = {'slug':('name',)}
    list_display=['name','ratings', 'currency', 'director','budget','rating_status']
    list_editable=['ratings','currency','budget','director']
    actions = ['set_dollar','set_euro']
    filter_horizontal = ['actors']
    search_fields = ['name__istartswith']
    list_filter = ['name','ratings','currency',RatingFilter]
    def rating_status(self, movie):
        if movie.ratings < 50:
            return 'It sucks'
        if movie.ratings < 70:
            return "That's fine"
        if movie.ratings <= 85:
            return "Good"
        return "Top"
    @admin.action(description='Ставим доллар')
    def set_dollar(self,request,q:QuerySet):
        q.update(currency=Movie.USD)

    @admin.action(description='Ставим евро')
    def set_euro(self,request,q:QuerySet):
        count_updated=q.update(currency=Movie.EUR)
        self.message_user(
            request,
            f'Было обновлено {count_updated} записей'
                          )






# admin.site.register(Movie,MovieAdmin)