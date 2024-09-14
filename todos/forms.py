from django import forms

from todos.models import Task

class TaskForm(forms.ModelForm):
   class Meta:
      model = Task
      fields = ["name", "description", "status"]

   def clean_name(self, *args, **kwargs):
      query_name = self.cleaned_data.get("name")
      if '@' in query_name or '-' in query_name or '|' in query_name:
        raise forms.ValidationError('Task name cannot have special characters.') #Validation example filtering special characters
      return query_name