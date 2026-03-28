from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Equipment
from django import forms

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'category', 'purchase_date', 'status']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom de l\'équipement',
                'required': 'required'
            }),
            'category': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Catégorie (ex: Informatique, Électrique)',
                'required': 'required'
            }),
            'purchase_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': 'required'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select',
                'required': 'required'
            })
        }
        labels = {
            'name': 'Nom de l\'équipement',
            'category': 'Catégorie',
            'purchase_date': 'Date d\'achat',
            'status': 'Statut'
        }

def equipment_list(request):
    equipments = Equipment.objects.all()
    return render(request, 'equipment/equipment_list.html', {'equipments': equipments})

def equipment_detail(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    return render(request, 'equipment/equipment_detail.html', {'equipment': equipment})

def equipment_create(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            equipment = form.save()
            messages.success(request, f'✓ Équipement "{equipment.name}" enregistré avec succès!')
            return redirect('equipment_list')
        else:
            messages.error(request, '✗ Erreur lors de l\'enregistrement. Veuillez vérifier les champs.')
    else:
        form = EquipmentForm()
    return render(request, 'equipment/equipment_form.html', {'form': form})
