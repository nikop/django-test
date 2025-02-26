from django import forms

class TodoItemForm(forms.Form):
    template_name = "form.html"

    title = forms.CharField(label="Title", max_length=100)
    description = forms.CharField(label="Description", widget=forms.Textarea)