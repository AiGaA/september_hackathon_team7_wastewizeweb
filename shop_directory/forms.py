from django import forms
from .models import Shop


class ShopForm(forms.ModelForm):
    """
    Shop Form to add shop's details
    """

    class Meta:
        """
        This inner metaclass will define the Model and the fields
        to include
        """

        model = Shop
        # fields = "__all__"
        fields = ['shop_name', 'description', 'company_address', 'eircode', 'image', 'category', 'location']

        widgets = {
            'shop_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'company_address': forms.TextInput(attrs={'class': 'form-control'}),
            'eircode': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        """
        Override the init() method to make changes to some fields
        """
        super().__init__(*args, **kwargs)
