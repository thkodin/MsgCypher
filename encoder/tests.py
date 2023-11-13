from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.test import TestCase

from .constants import MAX_MESSAGE_LENGTH
from .forms import UserMessageForm
from .models import UserMessage

print("Beginnning tests for encoder app...")


# Create your tests here.
class UserMessageModelTest(TestCase):
    def createAndRetrieveMessage(self):
        msg = "This is a test message."
        user_msg = UserMessage.objects.create(message=msg)
        retrieved_msg = UserMessage.objects.get(pk=user_msg.pk)
        self.assertEqual(retrieved_msg, msg)

    def testUserMessageLength(self):
        # Is it saved as metadata properly?
        meta_msg_length = UserMessage._meta.get_field("message").max_length
        self.assertEqual(meta_msg_length, MAX_MESSAGE_LENGTH)

        # Input not blank, but less than max length
        msg_in_limits = UserMessage.objects.create(message="a" * (MAX_MESSAGE_LENGTH - 1))
        msg_length = len(msg_in_limits.message)
        self.assertLess(msg_length, MAX_MESSAGE_LENGTH)

        # Input exactly equal to max length
        msg_maxlength = UserMessage.objects.create(message="a" * MAX_MESSAGE_LENGTH)
        msg_length = len(msg_maxlength.message)
        self.assertEqual(msg_length, MAX_MESSAGE_LENGTH)

        # Input larger than max length (should raise exception)
        with self.assertRaises(ValidationError):
            msg_exceed_maxlength = UserMessage.objects.create(message="a" * (MAX_MESSAGE_LENGTH + 1))
            msg_exceed_maxlength.full_clean()

    def testBlankInput(self):
        with self.assertRaises(ValidationError):
            msg_blank = UserMessage.objects.create(message="")
            msg_blank.full_clean()

    def testNullInput(self):
        with self.assertRaises(IntegrityError):
            msg_null = UserMessage.objects.create(message=None)
            msg_null.full_clean()


class UserMessageFormTests(TestCase):
    def test_blank_message(self):
        form = UserMessageForm(data={"message": ""})
        self.assertFalse(form.is_valid())

    def test_null_message(self):
        form = UserMessageForm(data={"message": None})
        self.assertFalse(form.is_valid())

    def test_message_too_long(self):
        form = UserMessageForm(data={"message": "a" * (MAX_MESSAGE_LENGTH + 1)})
        self.assertFalse(form.is_valid())

    def testSymbolsInMessage(self):
        typical_symbols = [
            "!",
            "@",
            "#",
            "$",
            "%",
            "^",
            "&",
            "*",
            "(",
            ")",
            "-",
            "_",
            "+",
            "=",
            "[",
            "]",
            "{",
            "}",
            "|",
            "\\",
            ";",
            ":",
            "'",
            '"',
            ",",
            ".",
            "<",
            ">",
            "/",
            "?",
            "`",
            "~",
        ]
        for symbol in typical_symbols:
            form = UserMessageForm(data={"message": symbol})
            self.assertTrue(form.is_valid())

    def testCorrectMessage(self):
        form = UserMessageForm(data={"message": "The quick brown fox jumps over the lazy dog."})
