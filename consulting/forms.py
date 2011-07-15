from django import forms
from models import Question
from django.utils.translation import ugettext, ugettext_lazy as _


class AskQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['username', 'email', 'text', 'comment', 'topic']

    honeypot = forms.CharField(required=False,
        label=_('If you enter anything in this field '\
                'your comment will be treated as spam'))


    def __init__(self, *args, **kwargs):
        super(AskQuestionForm, self).__init__(*args, **kwargs)
        self.fields['comment'].widget = forms.Textarea(attrs={'rows': 3, 'cols': 30})
        self.fields['text'].widget = forms.Textarea(attrs={'rows': 3, 'cols': 30})
        self.fields['topic'].widget = forms.HiddenInput()

    def clean_honeypot(self):
        """Check that nothing's been entered into the honeypot."""
        value = self.cleaned_data["honeypot"]
        if value:
            raise forms.ValidationError(self.fields["honeypot"].label)
        return value

