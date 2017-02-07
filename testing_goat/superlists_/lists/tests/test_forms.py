from django.test import TestCase

from lists.forms import ItemForm
from lists.constants import EMPTY_LIST_ERROR_MSG


class ItemFormTest(TestCase):

    def test_form_renders_item_text_input(self):
        form: ItemForm = ItemForm()
        self.assertIn('placeholder="Add a to-do"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())

    def test_form_validation_for_blank_items(self):
        form = ItemForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [EMPTY_LIST_ERROR_MSG])