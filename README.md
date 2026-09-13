# 🎭 Kimi Joke Generator

A simple and elegant random joke generator that fetches jokes from the **JokeAPI** external API. Part of the Kimi AI project.

## Features

✨ **Multiple Categories**
- Any (Random)
- General
- Programming
- Knock-knock
- Miscellaneous

🎯 **Joke Types**
- Single-line jokes
- Two-part jokes (setup + delivery)

🛡️ **Content Filtering**
- Blacklist inappropriate content (NSFW, religious, political, racist, sexist, explicit)

📊 **Error Handling**
- Timeout handling
- Connection error handling
- Invalid input validation
- API error responses

🧪 **Unit Tests**
- Comprehensive test suite
- Test for all categories
- Structure validation tests

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/lamrib41-commits/kimi.git
cd kimi
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

## Usage

### Interactive Mode

Run the interactive joke generator:

```bash
python joke_generator.py
```

You'll be presented with options to:
1. Get a random joke (any category)
2. Get a programming joke
3. Get a knock-knock joke
4. Get multiple jokes
5. Exit

### Programmatic Usage

```python
from joke_generator import JokeGenerator

# Initialize the generator
generator = JokeGenerator()

# Get a single joke
joke = generator.get_joke(category="programming")
generator.display_joke(joke)

# Get multiple jokes
jokes = generator.get_multiple_jokes(count=5, category="general")
for joke in jokes:
    generator.display_joke(joke)

# Get a joke with content filtering
blacklist = ["nsfw", "religious", "political"]
joke = generator.get_joke(blacklist=blackklist)

# Close the session
generator.close()
```

## API Details

### JokeAPI (v2)
- **Base URL**: `https://v2.jokeapi.dev/joke`
- **Rate Limit**: 120 requests per minute
- **No Authentication Required**: Free to use
- **Documentation**: [JokeAPI Docs](https://jokeapi.dev/)

## Code Structure

```
kimi/
├── joke_generator.py      # Main JokeGenerator class
├── test_joke_generator.py # Unit tests
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Methods

### `JokeGenerator(timeout=5)`
Initialize the joke generator.

**Parameters:**
- `timeout` (int): Request timeout in seconds (default: 5)

### `get_joke(category="any", joke_type="single", blacklist=None)`
Fetch a single random joke.

**Parameters:**
- `category` (str): Joke category - `any`, `general`, `knock`, `programming`, `misc`
- `joke_type` (str): `single` or `twopart`
- `blacklist` (list): Flags to filter - `nsfw`, `religious`, `political`, `racist`, `sexist`, `explicit`

**Returns:**
- Dictionary with joke data or `None` if error

### `display_joke(joke_data)`
Display joke in formatted output.

**Parameters:**
- `joke_data` (dict): Dictionary from `get_joke()`

### `get_multiple_jokes(count=3, category="any")`
Fetch multiple jokes.

**Parameters:**
- `count` (int): Number of jokes to fetch
- `category` (str): Joke category

**Returns:**
- List of joke dictionaries

## Running Tests

Run the unit tests:

```bash
python -m pytest test_joke_generator.py -v
```

Or using unittest:

```bash
python -m unittest test_joke_generator.py -v
```

## Example Output

```
============================================================
📚 Category: Programming
🎭 Type: single
============================================================

😂 Why do programmers prefer dark mode? Because light attracts bugs!

============================================================
```

## Error Handling

The generator handles various error scenarios:

- ⏱️ **Timeout Error**: If the API takes too long to respond
- 🔌 **Connection Error**: If there's no internet connection
- ❌ **Invalid Input**: Invalid category or joke type
- 📡 **API Error**: When API returns an error response
- 📝 **Parse Error**: If response cannot be parsed as JSON

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Created by **lamrib41-commits** as part of the **Kimi AI** project.

## Acknowledgments

- 🙏 [JokeAPI](https://jokeapi.dev/) - Free API for random jokes
- 🐍 [Python Requests Library](https://requests.readthedocs.io/) - HTTP library

## Support

If you encounter any issues or have suggestions, please:
- Open an [Issue](https://github.com/lamrib41-commits/kimi/issues)
- Create a [Discussion](https://github.com/lamrib41-commits/kimi/discussions)
- Contact the author

---

**Made with ❤️ by Kimi AI Team**
