from modeltranslation.translator import translator, TranslationOptions
from products.models import Category

class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(Category, CategoryTranslationOptions)