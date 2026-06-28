from django import forms


class EventRegistrationForm(forms.Form):

    full_name = forms.CharField(
        label="Full Name",
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Full Name"
        })
    )

    student_id = forms.CharField(
        label="Student ID",
        max_length=30,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Student ID"
        })
    )

    email = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Email Address"
        })
    )

    mobile = forms.CharField(
        label="Mobile Number",
        max_length=15,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Mobile Number"
        })
    )

    department = forms.CharField(
        label="Department",
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Department"
        })
    )

    semester = forms.CharField(
        label="Year / Semester",
        max_length=50,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Year / Semester"
        })
    )

    declaration = forms.BooleanField(
        label="I confirm that the above information is correct."
    )