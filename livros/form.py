from django.forms import ModelForm
from livros.models import Livros



class LivrosForm(ModelForm):
    class Meta:
        model = Livros
        fields = ["liv_codigo", "liv_numerodepaginas","liv_nome","liv_dataleitura","liv_autor","liv_avaliacao","liv_leitura"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['liv_numerodepaginas'].widget.attrs.update(  {'class': 'form-control'})
        self.fields['liv_nome'].widget.attrs.update(  {'class': 'form-control'})
        self.fields['liv_dataleitura'].widget.attrs.update(  {'class': 'form-control'})
        self.fields['liv_autor'].widget.attrs.update(  {'class': 'form-control'})
        self.fields['liv_avaliacao'].widget.attrs.update(  {'class': 'form-control'})
        self.fields['liv_leitura'].widget.attrs.update(  {'class': 'form-control'})
        
        
   