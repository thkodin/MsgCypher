from django.shortcuts import render

from .forms import UserMessageForm

previous_input = {"user_message": "", "decoded_message": ""}


# Create your views here.
def decodeUserMessage(request):
    if request.method == "POST":
        # Prcoess the user's input.
        form = UserMessageForm(request.POST)

        if form.is_valid():
            # Grab the data and apply encoding (reverse) to it.
            user_input = form.cleaned_data
            user_message = user_input["message"]
            decoded_message = user_message[::-1]

            # Update previous input dictionary.
            previous_input["user_message"] = user_message
            previous_input["decoded_message"] = decoded_message
            return render(
                request,
                "decoder.html",
                {"form": UserMessageForm(), "user_message": user_message, "decoded_message": decoded_message},
            )
        else:
            # Keep previous input and display error message.
            user_message = previous_input["user_message"]
            decoded_message = previous_input["decoded_message"]
            return render(
                request,
                "decoder.html",
                {"form": form, "user_message": user_message, "decoded_message": decoded_message},
            )

    else:
        # Get the base form for user input, and do not add history elements.
        form = UserMessageForm()
        return render(request, "decoder.html", {"form": form})
