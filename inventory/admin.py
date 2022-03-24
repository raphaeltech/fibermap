from django.contrib import admin


from django.contrib import admin
from inventory.models import positionPoles

from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields


class RentalAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }


admin.site.register(positionPoles)