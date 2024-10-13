from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        has_main = False
        for line in self.forms:
            data = line.cleaned_data
            if data['DELETE']:
                continue
            if data['is_main']:
                if has_main:
                    raise ValidationError('Основным может быть только один раздел')
                has_main = True
        if not has_main:
            raise ValidationError('Укажите основной раздел')
        return super().clean()



class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 0
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass
