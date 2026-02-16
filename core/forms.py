from django import forms
from .models import Student, Achievement

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'register_number', 'course', 'batch', 'department', 'status']

class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ['title', 'description', 'category', 'proof', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}), # Adds a date picker to the GUI
        }