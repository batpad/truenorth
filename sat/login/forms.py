class RegisterForm(forms.ModelForm):
    """ a form to create user"""
    password = forms.CharField(
            label="Password",
            widget=forms.PasswordInput()
    )
    password_confirm = forms.CharField(
            label="Password Repeat",
            widget=forms.PasswordInput()
    )
    class Meta:
        model = User
        exclude = ('last_login', 'activation_key')

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Password don't math")
        return password_confirm

    def clean_email(self):
        if User.objects.filter(email__iexact=self.cleaned_data.get("email")):
            raise forms.ValidationError("email already exists")
        return self.cleaned_data['email']

    def save(self):
        user = super(RegisterForm, self).save(commit=False)
        user.password = self.cleaned_data['password']
        user.activation_key = generate_sha1(user.email)
        user.save()

        return user
