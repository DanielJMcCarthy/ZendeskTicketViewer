from django.test import TestCase

"""
class TestHomepage(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    # check if the page contains the subject field and required number of rows.
    def test_content(self):
        self.assertContains(self.response, "Subject")
        self.assertContains(self.response, '<th scope="row">1</th>')
        self.assertContains(self.response, '<th scope="row">25</th>')
        self.assertNotContains(self.response, '<th scope="row">26</th>')

    # check if the page number contains the correct amount of pages.
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

    # check if the 'Previous' and 'Next' buttons do not display on first and last element of pagination bar,
    # if the 'Previous' and 'Next' buttons do display when in between first and last element. i.e when on page two.
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


class TestTicketPage(TestCase):

    def test_template(self):
        response = self.client.get('/ticket')
        self.assertTemplateUsed(response, 'home.html')
        response = self.client.get('/ticket?id=1')
        self.assertTemplateUsed(response, 'ticket.html')

    # Tests the ticket to ensure it contains the data.
    def test_content(self):
        response = self.client.get('/ticket')
        self.assertNotContains(response, "Go Back")
        response = self.client.get('/ticket?id=1')
        self.assertContains(response, "1 - Sample ticket: Meet the ticket")
        self.assertContains(response,
                            "I’m sending an email because I’m having a problem setting up your new product. Can you help me troubleshoot?")
        self.assertContains(response,
                            '<button class="btn btn-primary" onclick="window.history.back()">Go Back</button>')

    # Tests if the page is missing resources i.e ticket_id 10000 does not exist.
    def test_content_404(self):
        response = self.client.get('/ticket?id=10000')
        self.assertNotContains(response, "1 - Sample ticket: Meet the ticket")
        self.assertNotContains(response,
                               "Hi there, I’m sending an email because I’m having a problem setting up your new product. Can you help me troubleshoot? Thanks, The Customer")
        self.assertNotContains(response,
                               '<button class="btn btn-primary" onclick="window.history.back()">Go Back</button>')
        self.assertContains(response, 'RecordNotFound')
"""