import unittest
from EmotionDetection.emotion_detector import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        text_joy = "I am glad this happened"
        result_joy = emotion_detector(text_joy)
        self.assertEqual(result_joy['dominant_emotion'], 'joy')

        # Test case 2: Anger
        text_anger = "I am really mad about this"
        result_anger = emotion_detector(text_anger)
        self.assertEqual(result_anger['dominant_emotion'], 'anger')

        # Test case 3: Disgust
        text_disgust = "I feel disgusted just hearing about this"
        result_disgust = emotion_detector(text_disgust)
        self.assertEqual(result_disgust['dominant_emotion'], 'disgust')

        # Test case 4: Sadness
        text_sadness = "I am so sad about this"
        result_sadness = emotion_detector(text_sadness)
        self.assertEqual(result_sadness['dominant_emotion'], 'sadness')

        # Test case 5: Fear
        text_fear = "I am really afraid that this will happen"
        result_fear = emotion_detector(text_fear)
        self.assertEqual(result_fear['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()