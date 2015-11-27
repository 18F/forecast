from django.contrib import admin

# Register your models here.
from .models import Opportunity, Office, OSBUAdvisor


def make_published(modeladmin, request, queryset):
    queryset.update(published=True)
make_published.short_description = "Publish selected oppotunities"


def make_unpublished(modeladmin, request, queryset):
    queryset.update(published=False)
make_unpublished.short_description = "Unpublish selected oppotunities"


@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):

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


@admin.register(OSBUAdvisor)
class OSBUAdvisor(admin.ModelAdmin):
    pass
