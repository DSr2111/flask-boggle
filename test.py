from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):
    def setUp(self):
        """Setup prior to executing tests"""

        self.client = app.test_client()
        app.config['TESTING'] = True
    def test_homepage(self):
        """Ensure information in session and HTML displaying properly"""

        with self.client:
            response = self.client.get('/')
            self.assertIn('board', session)
            self.assertIsNone(session.get('highscore'))
            self.assertIsNone(session.get('nplays'))
            self.assertIn(b'<p>High Score:', response.data)
            self.assertIn(b'Score:', response.data)
            self.assertIn(b'Seconds Left:', response.data)

    
