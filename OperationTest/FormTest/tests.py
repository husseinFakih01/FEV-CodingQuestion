from django.test import SimpleTestCase, TestCase
from .forms import ItemForm


# Create your tests here.
class TestForm(SimpleTestCase):

  #check the form with valid data
    def test_Form_valid_data(self):
      form=ItemForm(data={
        'name':'Car',
        'price':'10000',
        'description':'Very Nice Car',
        'quantity':'1'
        })
      self.assertTrue(form.is_valid())

      #check the form without data
    def test_Form_no_data(self):
        form=ItemForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),3)