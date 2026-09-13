import unittest
from joke_generator import JokeGenerator


class TestJokeGenerator(unittest.TestCase):
    """
    Unit tests for JokeGenerator class
    """
    
    def setUp(self):
        """Set up test fixtures"""
        self.generator = JokeGenerator(timeout=10)
    
    def tearDown(self):
        """Clean up after tests"""
        self.generator.close()
    
    def test_get_joke_any_category(self):
        """Test getting a joke from any category"""
        joke = self.generator.get_joke(category="any")
        self.assertIsNotNone(joke)
        self.assertIn("type", joke)
    
    def test_get_joke_programming_category(self):
        """Test getting a programming joke"""
        joke = self.generator.get_joke(category="programming")
        if joke:
            self.assertEqual(joke.get("category"), "Programming")
    
    def test_get_joke_knock_category(self):
        """Test getting a knock-knock joke"""
        joke = self.generator.get_joke(category="knock")
        if joke:
            self.assertEqual(joke.get("category"), "Knock-knock")
    
    def test_invalid_category(self):
        """Test that invalid category returns None"""
        joke = self.generator.get_joke(category="invalid")
        self.assertIsNone(joke)
    
    def test_invalid_joke_type(self):
        """Test that invalid joke type returns None"""
        joke = self.generator.get_joke(joke_type="invalid")
        self.assertIsNone(joke)
    
    def test_get_multiple_jokes(self):
        """Test getting multiple jokes"""
        jokes = self.generator.get_multiple_jokes(count=2)
        self.assertGreaterEqual(len(jokes), 0)
    
    def test_joke_structure_single(self):
        """Test structure of single joke"""
        joke = self.generator.get_joke(joke_type="single")
        if joke and not joke.get("error"):
            self.assertIn("joke", joke)
    
    def test_joke_structure_twopart(self):
        """Test structure of two-part joke"""
        joke = self.generator.get_joke(joke_type="twopart")
        if joke and not joke.get("error"):
            self.assertIn("setup", joke)
            self.assertIn("delivery", joke)


if __name__ == "__main__":
    unittest.main()
