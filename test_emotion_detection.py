import unittest
from EmotionDetection.emotion_detection import emotion_detector
class TestEmotionDetector(unittest.TestCase):
    def test_joy_detection(self):
        # Test statement: "I am glad this happened" → dominant emotion should be "joy"
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')
    def test_anger_detection(self):
        # Test statement: "I am really mad about this" → dominant emotion should be "anger"
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')
    def test_disgust_detection(self):
        # Test statement: "I feel disgusted just hearing about this" → dominant emotion should be "disgust"
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')
    def test_sadness_detection(self):
        # Test statement: "I am so sad about this" → dominant emotion should be "sadness"
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')
    def test_fear_detection(self):
        # Test statement: "I am really afraid that this will happen" → dominant emotion should be "fear"
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')
if __name__ == '__main__':
    unittest.main()