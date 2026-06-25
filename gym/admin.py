from django.contrib import admin
from .models import Trainer, MembershipPlan, Member, Gallery, Contact, BlogPost

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'experience')
    search_fields = ('name', 'specialty')

@admin.register(MembershipPlan)
class MembershipPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration')
    search_fields = ('name',)

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'join_date', 'expiry_date', 'plan')
    list_filter = ('plan', 'join_date', 'expiry_date')
    search_fields = ('name', 'email', 'phone')

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('category', 'author', 'created_at')
    search_fields = ('title', 'content')
