from django.contrib import admin

from .models import Publisher, Categorie, News, Image, Tag, Newslatter, Video, Commentaire, Reponse, SignalComment, SignalReponse


admin.site.register(Publisher)
admin.site.register(Categorie)
admin.site.register(News)
admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(Newslatter)
admin.site.register(Video)
admin.site.register(Commentaire)
admin.site.register(Reponse)
admin.site.register(SignalComment)
admin.site.register(SignalReponse)
