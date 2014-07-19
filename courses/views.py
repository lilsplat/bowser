from django.shortcuts import render
from courses.forms import UserForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from courses.models import Student
def index(request):
    return render(request, 'courses/index.html')

def register(request):
    # get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
		# Save the user's form data to the database.
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registered = True
			student = Student.objects.get_or_create(user=user)
		

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render_to_response(
            'courses/register.html',
            {'user_form': user_form, 'registered': registered},
            context)
