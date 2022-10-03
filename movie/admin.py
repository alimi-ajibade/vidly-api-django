from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode
from .models import Movie, Genre, MoviePoster

# Register your models here.


class ImagesInline(admin.TabularInline):
    model = MoviePoster
    readonly_fields = ["thumbnail"]

    def thumbnail(self, instance):
        if instance.image.name != "":
            return format_html(f'<img src="{instance.image.url}" class="thumbnail">')
        return ""


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    actions = ["clear_stock"]
    autocomplete_fields = ["genre"]
    inlines = [ImagesInline]
    list_display = ["title", "genre", "imdbRating", "description", "releaseDate"]
    list_editable = ["imdbRating"]
    list_filter = ["genre"]
    list_per_page = 10
    list_select_related = ["genre"]
    ordering = ["title", "releaseDate"]
    search_fields = ["title"]

    class Media:
        css = {"all": ["movie/styles.css"]}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["name", "movie_count"]
    search_fields = ["name"]

    @admin.display(ordering="movie_count")
    def movie_count(self, genre):
        url = f'{reverse("admin:movie_movie_changelist")}?{urlencode({"genre__id": genre._id})}'
        return format_html("<a href={}>{}</a>", url, genre.movie_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(movie_count=Count("movie"))


# @admin.register(Promotion)
# class PromotionAdmin(admin.ModelAdmin):
#     list_display = ["movie", "thumbnail"]
#     autocomplete_fields = ["movie"]

#     def thumbnail(self, instance):
#         if instance.image.name != "":
#             return format_html(f'<img src="{instance.image.url}" class="thumbnail">')
#         return ""

#     class Media:
#         css = {"all": ["movie/styles.css"]}
