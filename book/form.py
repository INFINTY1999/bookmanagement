from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from book.models import Author, Books

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self ).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            
class CustomUserCreationForm2(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username']
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm2, self ).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
        
class Authorform(ModelForm):
    class Meta:
        model = Author
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super(Authorform, self ).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        
class Booksform(ModelForm):
    class Meta:
        model = Books
        fields = ['title','description','author','rating']
        
    def __init__(self, *args, **kwargs):
        super(Booksform, self ).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})