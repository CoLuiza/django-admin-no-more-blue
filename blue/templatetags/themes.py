from django import template

from nmb import settings

register = template.Library()


class ThemeNode(template.Node):

    def render(self, context):
        context['static_theme'] = settings.STATIC_THEME
        return ''


@register.tag(name='get_theme_context')
def get_theme_context(parser, token):
    return ThemeNode()
