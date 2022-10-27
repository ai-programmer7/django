from django import forms
from .models import Message


class ClientForm(forms.ModelForm):
    class Meta:
        STYLE_CLASS_NAME = "form-control rounded-0 border-top-0 border-right-0 border-left-0"
        model = Message
        fields = '__all__'
        labels = {
            'name': 'Имя',
            'mail': 'Электронная почта',
            'phone': 'Телефон',
            'message': 'Сообщение'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': STYLE_CLASS_NAME}),
            'mail': forms.EmailInput(attrs={'class': STYLE_CLASS_NAME}),
            'phone': forms.TextInput(attrs={'class': STYLE_CLASS_NAME}),
            'message': forms.Textarea(attrs={'class': STYLE_CLASS_NAME,
                                             'rows': 1})
        }

        error_messages = {
            'name': {
                'required': 'Укажите Ваше имя',
                'invalid': 'Укажите имя используя только буквы'
            },
            'mail': {
                'invalid': 'Адрес электронной почты указан неправильно'
            },
            'phone': {
                'requred': 'Укажите номер телефона',
                'min_length': 'Номер телефона не может содержать менее 12 символов',
                'max_length': 'Номер телефона не может содержать более 12 символов',
                'invalid': 'Номер телефона указан неправильно'
            },
            'message': {
                'required': 'Укажите Ваше сообщение'
            }
        }
