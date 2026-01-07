import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        expected_results = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear")
        ]
        for statement, expected in expected_results:
            emotion_analysis = emotion_detector(statement)
            dominant_emotion = emotion_analysis["dominant_emotion"]
            print(f"{statement}, {dominant_emotion} (pred), {expected} (exp)")
            self.assertEqual(dominant_emotion, expected)


if __name__ == "__main__":
    unittest.main()