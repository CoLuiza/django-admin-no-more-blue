from django.views.generic import TemplateView, RedirectView

from blue.themes.manager import Themes


class ThemeSelectorView(TemplateView):
    template_name = "blue/themeselector.html"

    def get_context_data(self, **kwargs):
        current_context = super().get_context_data(**kwargs)
        current_context["title"] = "Themes"
        return current_context


class SelectThemeView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        theme = self.request.GET.get("theme")
        possible_themes = [theme.value for theme in list(Themes)]
        if theme in possible_themes:
            self.request.session["theme"] = theme
        return "/admin/"
