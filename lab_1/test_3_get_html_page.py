from crawler import get_html_page
import unittest


class UrlTests(unittest.TestCase):
    def test_url(self):
        request = get_html_page("https://novayagazeta.ru/stories")
        self.assertEqual(request.status_code, 200)


if __name__ == "__main__":
    unittest.main()
