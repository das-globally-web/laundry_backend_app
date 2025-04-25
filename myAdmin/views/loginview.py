from django import forms

from myAdmin.views.decorators import session_login_required

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    # Optional: Prevent access if already logged in
    if request.session.get('user'):
        return redirect('dashboard')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Hardcoded Credentials
            if email == "admin@admin.com" and password == "admin@123":
                request.session['user'] = email
                messages.success(request, "Login successful!")
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid email or password.")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
@session_login_required
def dashboard_view(request):
    if 'user' not in request.session:
        return redirect('login')  # Agar login nahi kiya, to redirect ho jaye
    
    return render(request, 'dashboard.html', {'user': request.session['user']})
@session_login_required
def logout_view(request):
    request.session.flush()  # Clear all session data
    messages.success(request, "Logged out successfully.")
    return redirect('login')
