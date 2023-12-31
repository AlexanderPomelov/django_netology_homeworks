from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if len(form.cleaned_data) == 0:
                continue
            if form.cleaned_data['is_main']:
                count += 1
        if count == 0:
            raise ValidationError('Укажите основной раздел')
        elif count > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()

class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    list_filter = ['published_at']



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    inlines = [RelationshipInline]
