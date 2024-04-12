from unittest.mock import patch
import unittest
from EmotionDetection.emotion_detection import emotion_detector  # Replace 'your_module' with the name of your Python module or file


class TestEmotionDetector(unittest.TestCase):

    @patch('requests.post')
    def test_emotion_detector_success(self, mock_post):
        mock_response = {
            'emotion_predictions': [
                {'emotion': {'anger': 0.1, 'disgust': 0.2, 'fear': 0.3, 'joy': 0.4, 'sadness': 0.5}}
            ]
        }
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_response

        result = emotion_detector("This is a test text.")

        expected_result = {
            'anger': 0.1,
            'disgust': 0.2,
            'fear': 0.3,
            'joy': 0.4,
            'sadness': 0.5,
            'dominant_emotion': 'sadness'
        }

        self.assertDictEqual(result, expected_result)

    @patch('requests.post')
    def test_emotion_detector_failure(self, mock_post):
        mock_post.return_value.status_code = 500

        result = emotion_detector("This is a test text.")

        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
