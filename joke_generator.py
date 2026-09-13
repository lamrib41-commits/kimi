import requests
import json
from typing import Dict, Optional
import sys

class JokeGenerator:
    """
    Random Joke Generator using JokeAPI
    Supports multiple categories and joke types
    """
    
    BASE_URL = "https://v2.jokeapi.dev/joke"
    
    CATEGORIES = {
        "any": "Any",
        "general": "General",
        "knock": "Knock-knock",
        "programming": "Programming",
        "misc": "Miscellaneous"
    }
    
    JOKE_TYPES = ["single", "twopart"]
    
    def __init__(self, timeout: int = 5):
        """
        Initialize the JokeGenerator
        
        Args:
            timeout: Request timeout in seconds (default: 5)
        """
        self.timeout = timeout
        self.session = requests.Session()
    
    def get_joke(self, 
                 category: str = "any",
                 joke_type: str = "single",
                 blacklist: Optional[list] = None) -> Optional[Dict]:
        """
        Fetch a random joke from the API
        
        Args:
            category: Joke category (any, general, knock, programming, misc)
            joke_type: Type of joke (single or twopart)
            blacklist: List of flags to blacklist (nsfw, religious, political, racist, sexist, explicit)
        
        Returns:
            Dictionary containing joke data or None if request fails
        """
        # Validate inputs
        if category.lower() not in self.CATEGORIES:
            print(f"❌ Invalid category. Valid options: {list(self.CATEGORIES.keys())}")
            return None
        
        if joke_type.lower() not in self.JOKE_TYPES:
            print(f"❌ Invalid joke type. Valid options: {self.JOKE_TYPES}")
            return None
        
        try:
            # Construct URL
            url = f"{self.BASE_URL}/{category}"
            
            params = {
                "type": joke_type,
                "format": "json"
            }
            
            # Add blacklist if provided
            if blacklist:
                params["blacklist"] = ",".join(blacklist)
            
            # Make request
            response = self.session.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            
            data = response.json()
            
            # Check for error response
            if data.get("error"):
                print(f"❌ API Error: {data.get('message', 'Unknown error')}")
                return None
            
            return data
        
        except requests.exceptions.Timeout:
            print("❌ Request timed out. Please try again.")
            return None
        except requests.exceptions.ConnectionError:
            print("❌ Connection error. Please check your internet connection.")
            return None
        except requests.exceptions.RequestException as e:
            print(f"❌ Request error: {str(e)}")
            return None
        except json.JSONDecodeError:
            print("❌ Failed to parse response.")
            return None
    
    def display_joke(self, joke_data: Dict) -> None:
        """
        Display joke in a formatted way
        
        Args:
            joke_data: Dictionary containing joke data from API
        """
        if not joke_data:
            return
        
        print("\n" + "="*60)
        print(f"📚 Category: {joke_data.get('category', 'Unknown')}")
        print(f"🎭 Type: {joke_data.get('type', 'Unknown')}")
        print("="*60)
        
        if joke_data.get("type") == "single":
            print(f"\n😂 {joke_data.get('joke', 'No joke available')}")
        else:
            print(f"\n🎤 {joke_data.get('setup', 'No setup available')}")
            print(f"\n😂 {joke_data.get('delivery', 'No delivery available')}")
        
        print("\n" + "="*60 + "\n")
    
    def get_multiple_jokes(self, count: int = 3, category: str = "any") -> list:
        """
        Fetch multiple jokes
        
        Args:
            count: Number of jokes to fetch
            category: Joke category
        
        Returns:
            List of joke dictionaries
        """
        jokes = []
        for i in range(count):
            joke = self.get_joke(category=category)
            if joke:
                jokes.append(joke)
        return jokes
    
    def close(self):
        """
        Close the session
        """
        self.session.close()


def main():
    """
    Main function to demonstrate the JokeGenerator
    """
    print("🎭 Welcome to Kimi Joke Generator! 🎭\n")
    
    generator = JokeGenerator()
    
    try:
        while True:
            print("\nOptions:")
            print("1. Get a random joke (any category)")
            print("2. Get a programming joke")
            print("3. Get a knock-knock joke")
            print("4. Get multiple jokes")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == "1":
                joke = generator.get_joke()
                generator.display_joke(joke)
            
            elif choice == "2":
                joke = generator.get_joke(category="programming")
                generator.display_joke(joke)
            
            elif choice == "3":
                joke = generator.get_joke(category="knock")
                generator.display_joke(joke)
            
            elif choice == "4":
                count = input("How many jokes do you want? (default: 3): ").strip()
                count = int(count) if count.isdigit() else 3
                jokes = generator.get_multiple_jokes(count=count)
                for idx, joke in enumerate(jokes, 1):
                    print(f"\n--- Joke {idx} ---")
                    generator.display_joke(joke)
            
            elif choice == "5":
                print("\n👋 Thank you for using Kimi Joke Generator!")
                break
            
            else:
                print("❌ Invalid choice. Please try again.")
    
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted by user.")
    
    finally:
        generator.close()


if __name__ == "__main__":
    main()
