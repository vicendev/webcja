from django import forms

class ContactForm(forms.Form):

    ## Tipos de trabajos (estaticos) ##
    JOB_1 = 'Construcción'
    JOB_2 = 'Transformación'
    JOB_3 = 'Reparación'
    JOB_4 = 'Demolición'
    JOB_CHOICES = (
        (JOB_1, u"Construcción"),
        (JOB_2, u"Transformación"),
        (JOB_3, u"Reparación"),
        (JOB_4, u"Demolición")
    )

    name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu nombre'}
    ), min_length=3, max_length=100)
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu email'}
    ), min_length=3, max_length=100)
    content =  forms.CharField(label='Contenido', required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows':3, 'placeholder':'Escribe tu mensaje'}
    ), min_length=10, max_length=1000)
    jobs = forms.ChoiceField(choices=JOB_CHOICES, widget=forms.Select(
        attrs={'class':'form-control'}
    ))
    