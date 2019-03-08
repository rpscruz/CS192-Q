from django.contrib import admin

def save_model(self, request, obj, form, change):
    instance = form.save(commit=False)
    if not hasattr(instance, "poster"):
        instance.poster = request.user
        instance.save()
        form.save_m2m()
        return instance