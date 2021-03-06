from django import forms

from .models import Product 

class ProductForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    email = forms.EmailField()
    description = forms.CharField(required=False, widget=forms.Textarea(
                                            attrs={
                                                "class": "new-class-name two",
                                                "id": "my-id-for-textarea",
                                                "rows":20,
                                                'cols':120
                                            }
                                        )
                                    )
    price = forms.DecimalField()
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
            ]

class RawProductForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(required=False, widget=forms.Textarea(
                                            attrs={
                                                "class": "new-class-name two",
                                                "id": "my-id-for-textarea",
                                                "rows":20,
                                                'cols':120
                                            }
                                        )
                                    )
    price = forms.DecimalField()
    