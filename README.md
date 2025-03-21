# AstroBot: The Solar System Assistant

![AstroBot Logo](https://via.placeholder.com/150) <!-- Add a logo if you have one -->

AstroBot is a simple chatbot designed to answer queries about the solar system. It was developed as part of an Intel Student Bootcamp in 2021. The chatbot uses basic Natural Language Processing (NLP) techniques to understand and respond to user questions about planets, comets, asteroids, and other celestial bodies.

## Features

- **Greetings**: Responds to common greetings like "Hello", "Hi", etc.
- **Solar System Knowledge**: Provides information about planets, comets, asteroids, and more.
- **Text-to-Speech**: Converts responses to speech using the `pyttsx3` library.
- **GUI**: Built with `Tkinter` for a user-friendly interface.
- **Customizable Themes**: Allows users to change the font and color theme of the chat interface.

## Technologies Used

- **Python**: The core programming language used for development.
- **NLTK (Natural Language Toolkit)**: For tokenization, lemmatization, and stopword removal.
- **TfidfVectorizer**: For text vectorization and cosine similarity calculations.
- **BeautifulSoup**: For web scraping Wikipedia to gather information about celestial bodies.
- **Tkinter**: For building the graphical user interface (GUI).
- **pyttsx3**: For text-to-speech functionality.

## Installation

To run AstroBot on your local machine, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/AstroBot.git
   cd AstroBot
Install Dependencies:
Make sure you have Python 3.x installed. Then, install the required libraries using pip:

bash
Copy
pip install nltk beautifulsoup4 requests pyttsx3
Download NLTK Data:
You need to download the necessary NLTK data packages. Run the following commands in a Python shell:

python
Copy
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
Run the Chatbot:
Execute the gui11.py script to start the chatbot:

bash
Copy
python gui11.py
Usage
Launch the Application:
After running gui11.py, a window titled "AstroBot: The Solar System Assistant" will appear.

Interact with AstroBot:

Type your questions or greetings in the input field at the bottom of the window.

Press "Enter" or click the "Send" button to get a response from AstroBot.

To exit, type "Bye" and wait for the application to close automatically.

Customize the Interface:

Use the "Font" menu to change the font style.

Use the "Color Theme" menu to change the color scheme of the chat interface.

Screenshots
AstroBot Screenshot <!-- Add a screenshot if you have one -->

Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Intel Student Bootcamp: For providing the opportunity to work on this project.

NLTK and BeautifulSoup: For making NLP and web scraping easier.

Tkinter and pyttsx3: For enabling the creation of a user-friendly interface with text-to-speech capabilities.

Developer
Vignesh N: Primary developer of AstroBot.

Feel free to explore the code and improve upon it. Happy coding! 🚀

Copy

### Notes:
- Replace `your-username` in the clone command with your actual GitHub username.
- Add a logo and screenshot if you have them.
- Customize the acknowledgments and developer sections as needed.

This README should give users a clear understanding of your project and how to get started with it.
