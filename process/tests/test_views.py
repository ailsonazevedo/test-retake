from django.test import TestCase
from django.urls import reverse

class ProcessViewTestcase(TestCase):

    def test_process_return_list(self):
        response = self.client.get(reverse('process'))
        self.assertContains(response, 'Processos')


    def test_process_status_code_200(self):
        response = self.client.get(reverse('process'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'processes.html')

class PartsViewTestcase(TestCase):

    def test_parts_status_code_200(self):
        response = self.client.get(reverse('parts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'parts.html')

class ProcessAddViewTestcase(TestCase):

    def test_process_add_is_used(self):
        response = self.client.get(reverse('add_process'))
        self.assertTemplateUsed(response, 'Process/add_process.html')

class PartsAddViewTestcase(TestCase):

    def test_parts_add_is_used(self):
        response = self.client.get(reverse('add_parts'))
        self.assertTemplateUsed(response, 'Parts/add_parts.html')


    def test_parts_add_status_code_200(self):
        response = self.client.get(reverse('add_parts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Parts/add_parts.html')
