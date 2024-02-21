from django.template.defaulttags import register

@register.filter
def replace_en(string):
   return string.replace("/en","",1)