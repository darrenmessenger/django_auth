{"filter":false,"title":"forms.py","tooltip":"/accounts/forms.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":44,"column":24},"action":"remove","lines":["from django import forms","from django.contrib.auth.models import User","from django.contrib.auth.forms import UserCreationForm","from django.core.exceptions import ValidationError","","","class UserLoginForm(forms.Form):","    \"\"\"Form to be used to log users in\"\"\"","","    username = forms.CharField()","    password = forms.CharField(widget=forms.PasswordInput)","","","class UserRegistrationForm(UserCreationForm):","    \"\"\"Form used to register a new user\"\"\"","","    password1 = forms.CharField(","        label=\"Password\",","        widget=forms.PasswordInput)","    password2 = forms.CharField(","        label=\"Password Confirmation\",","        widget=forms.PasswordInput)","    ","    class Meta:","        model = User","        fields = ['email', 'username', 'password1', 'password2']","    ","    def clean_email(self):","        email = self.cleaned_data.get('email')","        username = self.cleaned_data.get('username')","        if User.objects.filter(email=email).exclude(username=username):","            raise forms.ValidationError(u'Email address must be unique')","        return email","","    def clean_password2(self):","        password1 = self.cleaned_data.get('password1')","        password2 = self.cleaned_data.get('password2')","","        if not password1 or not password2:","            raise ValidationError(\"Please confirm your password\")","        ","        if password1 != password2:","            raise ValidationError(\"Passwords must match\")","        ","        return password2"],"id":1},{"start":{"row":0,"column":0},"end":{"row":44,"column":24},"action":"insert","lines":["from django import forms","from django.contrib.auth.models import User","from django.contrib.auth.forms import UserCreationForm","from django.core.exceptions import ValidationError","","","class UserLoginForm(forms.Form):","    \"\"\"Form to be used to log users in\"\"\"","","    username = forms.CharField()","    password = forms.CharField(widget=forms.PasswordInput)","","","class UserRegistrationForm(UserCreationForm):","    \"\"\"Form used to register a new user\"\"\"","","    password1 = forms.CharField(","        label=\"Password\",","        widget=forms.PasswordInput)","    password2 = forms.CharField(","        label=\"Password Confirmation\",","        widget=forms.PasswordInput)","    ","    class Meta:","        model = User","        fields = ['email', 'username', 'password1', 'password2']","    ","    def clean_email(self):","        email = self.cleaned_data.get('email')","        username = self.cleaned_data.get('username')","        if User.objects.filter(email=email).exclude(username=username):","            raise forms.ValidationError(u'Email address must be unique')","        return email","","    def clean_password2(self):","        password1 = self.cleaned_data.get('password1')","        password2 = self.cleaned_data.get('password2')","","        if not password1 or not password2:","            raise ValidationError(\"Please confirm your password\")","        ","        if password1 != password2:","            raise ValidationError(\"Passwords must match\")","        ","        return password2"]}]]},"ace":{"folds":[],"scrolltop":375.8125,"scrollleft":0,"selection":{"start":{"row":44,"column":24},"end":{"row":44,"column":24},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":0,"state":"start","mode":"ace/mode/python"}},"timestamp":1574787818437,"hash":"33192e9c2c672271a969f7afd93bb2e4bacd99db"}