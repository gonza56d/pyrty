"""PrivateMessage form."""

# Django
from django import forms

# Pyrty
from privatemessages.models import PrivateMessage
from users.models import User


class PrivateMessageForm(forms.ModelForm):
    """Private message creation form."""
    
    def __init__(self, target_user=None, *args, **kwargs):
        super(PrivateMessageForm, self).__init__(*args, **kwargs)
        
        self.fields['message'].widget = forms.Textarea(
			attrs={'class': 'form-control', 'rows': 3}
		)
        
        if target_user is not None:
            self.fields['target_user'] = forms.ModelChoiceField(
                queryset=User.objects.filter(id=target_user.id),
				empty_label=None,
				widget=forms.Select(attrs={'style': 'display:none;'})
            )
    
    class Meta:
        model = PrivateMessage
        fields = ['target_user', 'message']
