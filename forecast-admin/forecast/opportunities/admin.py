from django.contrib import admin

# Register your models here.
from .models import Opportunity, Office, OSBUAdvisor


@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):

    def make_published(self, request, queryset):
        for obj in queryset:
            obj.published = True
            obj.save()
    make_published.short_description = "Publish selected oppotunities"

    def make_unpublished(self, request, queryset):
        queryset.update(published=False)
    make_unpublished.short_description = "Unpublish selected oppotunities"

    list_display = ['__str__', 'office', 'published']
    ordering = ['office']
    actions = [make_published, make_unpublished]

    def get_queryset(self, request):
        """Limit Pages to those that belong to the request's user."""
        qs = super(OpportunityAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            # It is mine, all mine. Just return everything.
            return qs
        # Now we just add an extra filter on the queryset and
        # we're done. Assumption: Page.owner is a foreignkey
        # to a User.
        return qs.filter(owner=request.user)


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        """Limit Pages to those that belong to the request's user."""
        qs = super(OfficeAdmin, self).get_queryset(request)
        return qs

admin.site.register(OSBUAdvisor)
