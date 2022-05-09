from modeltranslation.translator import translator, TranslationOptions
from .models import Blogs

class BlogTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(Blogs, BlogTranslationOptions)