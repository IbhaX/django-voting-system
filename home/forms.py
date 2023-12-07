from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Voters, PoliticalParty


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        fields_to_style = ["username", "email", "password1", "password2"]

        for field_name in fields_to_style:
            self.fields[field_name].widget.attrs["class"] = "form-control"
            self.fields[field_name].widget.attrs[
                "placeholder"
            ] = f"{field_name.capitalize()}"
            self.fields[field_name].label = ""
            self.fields[field_name].help_text = ""
        
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password1"].help_text = ""
        self.fields["password1"].label = ""

        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["placeholder"] = "Retype Password"
        self.fields["password2"].help_text = ""
        self.fields["password2"].label = ""
        

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=255)
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        fields_to_style = ["username", "password"]

        for field_name in fields_to_style:
            self.fields[field_name].widget.attrs["class"] = "form-control"
            self.fields[field_name].widget.attrs[
                "placeholder"
            ] = f"{field_name.capitalize()}"
            self.fields[field_name].label = ""
    
    
class VoterForm(forms.ModelForm):
    class Meta:
        model = Voters
        fields = ("uuid", "name", "dob", "pincode", "region", "email")

    def __init__(self, *args, **kwargs):
        super(VoterForm, self).__init__(*args, **kwargs)

        fields_to_style = ["uuid", "name", "dob", "email", "pincode", "region"]

        for field_name in fields_to_style:
            self.fields[field_name].widget.attrs["class"] = "form-control"
            self.fields[field_name].widget.attrs[
                "placeholder"
            ] = f"{field_name.capitalize()}"
            self.fields[field_name].label = ""

        self.fields["uuid"].widget.attrs["placeholder"] = "AADHAAR"


class PartyForm(forms.ModelForm):
    class Meta:
        model = PoliticalParty
        fields = (
            "party_id",
            "party_name",
            "party_logo",
            "candidate_name",
            "candidate_profile_pic",
        )

    def __init__(self, *args, **kwargs):
        super(PartyForm, self).__init__(*args, **kwargs)

        fields_to_style = [
            "party_id",
            "party_name",
            "party_logo",
            "candidate_name",
            "candidate_profile_pic",
        ]

        for field_name in fields_to_style:
            self.fields[field_name].widget.attrs["class"] = "form-control"
            self.fields[field_name].widget.attrs[
                "placeholder"
            ] = f"{' '.join(field_name.split("_")).title()}"
            self.fields[field_name].label = ""
