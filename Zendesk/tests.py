from django.test import TestCase

"""
class TestHomepage(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_content(self):
        self.assertContains(self.response, "Subject")
        self.assertContains(self.response, '<th scope="row">1</th>')
        self.assertContains(self.response, '<th scope="row">25</th>')
        self.assertNotContains(self.response, '<th scope="row">26</th>')

    # check if the page number contains the correct amount of pages
    def test_pagination_content(self):
        response = self.client.get('/?page=1')
        self.assertContains(response, '<th scope="row">1</th>')
        self.assertContains(response, '<th scope="row">25</th>')
        response = self.client.get('/?page=2')
        self.assertContains(response, '<th scope="row">26</th>')
        self.assertContains(response, '<th scope="row">50</th>')
        response = self.client.get('/?page=3')
        self.assertContains(response, '<th scope="row">51</th>')
        self.assertContains(response, '<th scope="row">75</th>')
        response = self.client.get('/?page=4')
        self.assertContains(response, '<th scope="row">76</th>')
        self.assertContains(response, '<th scope="row">100</th>')

    # check if the 'Previous' and 'Next' buttons do not display on first and last element of pagination bar
        # if the 'Previous' and 'Next' buttons do display when in between first and last element.
    def test_pagination_buttons(self):
        response = self.client.get('/?page=1')
        self.assertNotContains(response, 'Previous')
        self.assertContains(response, '<li class="page-item"><a class="page-link" href="/?page=1">1</a></li>')
        self.assertContains(response, '<li class="page-item"><a class="page-link" href="/?page=2">2</a></li>')
        self.assertContains(response, '<li class="page-item"><a class="page-link" href="/?page=3">3</a></li>')
        self.assertContains(response, '<li class="page-item"><a class="page-link" href="/?page=4">4</a></li>')
        self.assertContains(response, 'Next')
        response = self.client.get('/?page=3')
        self.assertContains(response, 'Previous')
        self.assertContains(response, '<li class="page-item"><a class="page-link" href="/?page=1">1</a></li>')
        self.assertContains(response, '<li class="page-item"><a class="page-link" href="/?page=2">2</a></li>')
        self.assertContains(response, '<li class="page-item"><a class="page-link" href="/?page=3">3</a></li>')
        self.assertContains(response, '<li class="page-item"><a class="page-link" href="/?page=4">4</a></li>')
        self.assertContains(response, 'Next')
        response = self.client.get('/?page=4')
        self.assertContains(response, 'Previous')
        self.assertContains(response, '<li class="page-item"><a class="page-link" href="/?page=1">1</a></li>')
        self.assertContains(response, '<li class="page-item"><a class="page-link" href="/?page=2">2</a></li>')
        self.assertContains(response, '<li class="page-item"><a class="page-link" href="/?page=3">3</a></li>')
        self.assertContains(response, '<li class="page-item"><a class="page-link" href="/?page=4">4</a></li>')
        self.assertNotContains(response, 'Next')
        
"""
