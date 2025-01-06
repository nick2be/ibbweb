from django import template

register = template.Library()

@register.filter
def get_translated_field(obj, field):
    """
    Gets a translated field from an object using the field name.
    Usage: {{ object|get_translated_field:'name_en' }}
    """
    return getattr(obj, field, '') 