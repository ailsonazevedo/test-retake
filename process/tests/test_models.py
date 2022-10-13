from django.test import TestCase
from process.models import Process, Parts
class ProcessTestCase(TestCase):
    def setUp(self):
        Process.objects.create(
            number='500',
            judicialClass='Danos Materiais',
            topic = 'Danos',
            judge = 'João Paulo',
        )
        Parts.objects.create(
            name='Pedro',
        )
    def test_return_str_process(self):
        process = Process.objects.get(number='500')
        self.assertEqual(str(process), '500')

    def test_return_str_parts(self):
        parts = Parts.objects.get(name='Pedro')
        self.assertEqual(str(parts), 'Pedro')
