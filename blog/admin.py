from django.contrib import admin
from .models import Article, Category

# Admin Header Change
admin.site.site_header = "پنل مدیرت تبریز لینوکس"
# End Admin

def make_published_article(modeladmin, request, queryset):
    rows_updated = queryset.update(status="P")
    if rows_updated == 1 :
        message_bit = "منتشر شد."
    else : 
        message_bit = "منتشر شد."
    modeladmin.message_user(request, "{} مقاله {}".format(rows_updated, message_bit))
make_published_article.short_description = "انتشار مقالات انتخاب شده"

def make_draft_article(modeladmin, request, queryset):
    rows_updated = queryset.update(status="D")
    if rows_updated == 1 :
        message_bit = "پیش‌نویس شد."
    else : 
        message_bit = "پیش‌نویس شد."
    modeladmin.message_user(request, "{} مقاله {}".format(rows_updated, message_bit))
make_draft_article.short_description = "پیش‌نویس شدن مقالات انتخاب شده_"

def make_published_category(modeladmin, request, queryset):
    rows_updated = queryset.update(status=True)
    if rows_updated == 1 :
        message_bit = "نمایش داده شد."
    else : 
        message_bit = "نمایش داده شد."
    modeladmin.message_user(request, "{} دسته‌بندی {}".format(rows_updated, message_bit))
make_published_category.short_description = "نمایش دسته‌بندی های انتخاب شده"

def make_draft_category(modeladmin, request, queryset):
    rows_updated = queryset.update(status=False)
    if rows_updated == 1 :
        message_bit = "پنهان شد."
    else : 
        message_bit = "پنهان شد."
    modeladmin.message_user(request, "{} دسته‌بندی {}".format(rows_updated, message_bit))
make_draft_category.short_description = "پنهان کردن دسته‌بندی های انتخاب شده"

class CategoryAdmin(admin.ModelAdmin):
    list_display        = ('position','title','slug','parent','status')
    list_filter         = (['status'])
    search_fields       = ('title','slug')
    prepopulated_fields = {'slug': ('title',)}
    actions             = [make_published_category, make_draft_category]

admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display        = ('title','thumbnail_tag','slug','author','jpublish','status','category_to_str')
    list_filter         = ('publish','status','author')
    search_fields       = ('title','description','slug')
    ordering            = ('-status','-publish') # Baraye Nozoli Neshan Dadan Az '-publish' Estefade Shode 
    prepopulated_fields = {'slug': ('title',)}
    actions             = [make_published_article, make_draft_article]

admin.site.register(Article, ArticleAdmin)