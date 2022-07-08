import unittest

class TestForumApp(unittest.TestCase):

    def test_app_is_not_none(self):
        from forum_app import app
        self.assertIsNotNone(app)
