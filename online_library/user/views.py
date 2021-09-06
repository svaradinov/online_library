from django.shortcuts import render, redirect

from online_library.user.forms import UserForm



def create_user(req):
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            form.save()

            return redirect('home')

    else:
        form = UserForm()

    context = {
        'form': form
        }

    return render(req, 'home-no-profile.html', context)


def user_details(req):
    pass

def edit_user(req):
    pass

def delete_user(req):
    pass