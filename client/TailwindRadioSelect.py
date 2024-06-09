from django import forms

class TailwindRadioSelect(forms.RadioSelect):
    template_name = 'client/custom_radio.html'
