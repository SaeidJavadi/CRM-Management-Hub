from django import template

register = template.Library()


@register.simple_tag
def to_class_name(object):
    return str(object.__class__.__name__)


@register.filter
def checkpaid(objs):
    return objs.filter(status=True).count()


@register.filter
def checkunpaid(objs):
    return objs.filter(status=False).count()
