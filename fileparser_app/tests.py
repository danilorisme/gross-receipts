from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
import os
from . import views

# Create your tests here.
class TestGrossReceipts(TestCase):
    def setUp(self):
        self.project_dit = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # self.file_parser = views.file_parser()

    def test_file_upload(self):
        url = reverse('file-upload')
        file_test = os.path.join(self.project_dit, "_doc")+"/example_input.tab"
        file_uploaded_test = SimpleUploadedFile(file_test, open(file_test, 'rb').read())
        data = {'file': file_uploaded_test}
        response = self.client.post(url, data, follow=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'grossreceipts/index.html')

    def test_file_parser(self):
        file_test = os.path.join(self.project_dit, "_doc")+"/example_input.tab"
        file_uploaded_test = SimpleUploadedFile(file_test, open(file_test, 'rb').read())

        grossreceipts, file_content_json = views.file_parser(file_uploaded_test)

        self.assertEquals(grossreceipts, 30.0)
        self.assertIs(type(file_content_json), list)


