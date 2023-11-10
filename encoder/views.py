from django.shortcuts import render

from .forms import UserMessageForm

# To keep track of the user's most recent input and its output.
# This makes the result invalid-input safe in that it is preserved even if the
# user enters invalid input (e.g., a blank message), which would normally
# refresh the page and the variables within the view function. Describing them
# in this global scope preserves them.
previous_input = {"user_message": "", "encoded_message": ""}


# Create your views here.
def encodeUserMessage(request):
    if request.method == "POST":
        # Prcoess the user's input.
        form = UserMessageForm(request.POST)

        if form.is_valid():
            # Grab the data and apply encoding (reverse) to it.
            user_input = form.cleaned_data
            user_message = user_input["message"]
            encoded_message = user_message[::-1]

            # Update previous input dictionary.
            previous_input["user_message"] = user_message
            previous_input["encoded_message"] = encoded_message
            return render(
                request,
                "encoder.html",
                {"form": UserMessageForm(), "user_message": user_message, "encoded_message": encoded_message},
            )
        else:
            # Keep previous input and display error message.
            user_message = previous_input["user_message"]
            encoded_message = previous_input["encoded_message"]
            return render(
                request,
                "encoder.html",
                {"form": form, "user_message": user_message, "encoded_message": encoded_message},
            )

    else:
        # Get the base form for user input, and do not add history elements.
        form = UserMessageForm()
        return render(request, "encoder.html", {"form": form})
