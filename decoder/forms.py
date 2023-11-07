from django.core.exceptions import ValidationError
from django.forms import ModelForm, Textarea

from .models import UserMessage


class UserMessageForm(ModelForm):
    """Form for user message."""

    max_msg_length = UserMessage._meta.get_field("message").max_length
    # message = CharField(
    #     max_length=max_length,
    #     label="Message",
    #     widget=Textarea(attrs={"cols": 40, "rows": 10, "placeholder": f"max {max_length} characters"}),
    # )

    class Meta:
        """Metadata for user message."""

        model = UserMessage
        fields = ["message"]
        labels = {"message": "Message"}
        max_length = model._meta.get_field("message").max_length
        widgets = {"message": Textarea(attrs={"cols": 40, "rows": 10, "placeholder": f"max {max_length} characters"})}

    def clean_text(self):
        message = self.cleaned_data.get("message")

        # Split the message into lines and check if any line is non-empty
        lines = message.split("\n")
        for line in lines:
            if line.strip():  # Check if the line contains non-whitespace characters
                continue
            else:
                raise ValidationError("Invalid input. Message should not be blank.")
