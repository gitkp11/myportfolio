from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home/index.html'


class SingleBlogView(TemplateView):
    template_name = 'home/blog-single.html'
