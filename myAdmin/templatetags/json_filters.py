import json
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def jsonify(value):
    """
    Convert a Python object to a JSON string, marked as safe for use in HTML attributes.
    """
    return json.dumps(value)