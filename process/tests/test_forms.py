from django.test import TestCase

from process.forms import PartsForm, ProcessForm

class ProcessFormTestCase(TestCase):

    def test_process_form_valid(self):
        form = ProcessForm(data={
            'number': '500',
            'judicialClass': 'Danos Materiais',
            'topic': 'Danos',
            'judge': 'João Paulo',
            'parts': ['Pedro'],
            'category': 'Roubo',
        })
        self.assertTrue(form.is_valid())
    
    def test_process_form_invalid(self):
        form = ProcessForm(data={})
        self.assertFalse(form.is_valid())

class PartsFormTestCase(TestCase):

    def test_parts_form_valid(self):
        form = PartsForm(data={
            'name': 'Pedro',
        })
        self.assertTrue(form.is_valid())
    
    def test_parts_form_invalid(self):
        form = PartsForm(data={})
        self.assertFalse(form.is_valid())