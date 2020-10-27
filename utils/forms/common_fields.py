# Django
from django import forms


class TextArea(forms.CharField):
    """Django TextArea with common css attrs."""
    
    icon = ''
    
    def __init__(self, *, placeholder=None, max_length=None, min_length=None, strip=True, empty_value='', **kwargs):
        super().__init__(**kwargs)
        self.widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'})
        if placeholder is not None:
            self.widget.attrs['placeholder'] = placeholder
