from enum import Enum

from django.conf import settings


class Themes(Enum):
    BASE = "base"
    PLUM = "plum"
    PEACH = "peach"
    APPLE = "apple"
    BLUEBERRY = "blueberry"
    MELON = "melon"
    GRAPES = "grapes"


class ThemeManager:
    @staticmethod
    def get_theme(request=None):
        is_static_theme = settings.STATIC_THEME
        if is_static_theme:
            return settings.THEME.lower()
        else:
            if not request:
                return Themes.BASE.value
            session = request.session
            if "theme" in session:
                return session["theme"]
            else:
                session["theme"] = Themes.BASE.value
                return Themes.BASE.value
