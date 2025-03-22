# AstroBot: The Solar System Assistant


AstroBot is a simple chatbot designed to answer queries about the solar system. It was developed as part of an Intel Student Bootcamp in 2021. The chatbot uses basic Natural Language Processing (NLP) techniques to understand and respond to user questions about planets, comets, asteroids, and other celestial bodies.

## Features

- **Greetings**: Responds to common greetings like "Hello", "Hi", etc.
- **Solar System Knowledge**: Provides information about planets, comets, asteroids, and more.
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
2. **Install Dependencies**:
Make sure you have Python 3.7+ installed. Then, install the required libraries using pip:
   ```bash
   pip install nltk beautifulsoup4 requests
3. **Download NLTK Data**:
You need to download the necessary NLTK data packages. Run the following commands in a Python shell:
   ```bash
   python
   Copy
   import nltk
   nltk.download('punkt')
   nltk.download('wordnet')
   nltk.download('stopwords')
4. **Run the Chatbot**:
Execute the gui11.py script to start the chatbot:
   ```bash
   python gui11.py

##Usage
1. **Launch the Application**:
After running gui11.py, a window titled "AstroBot: The Solar System Assistant" will appear.

2. **Interact with AstroBot**:
Type your questions or greetings in the input field at the bottom of the window.
Press "Enter" or click the "Send" button to get a response from AstroBot.
To exit, type "Bye" and wait for the application to close automatically.

3. **Customize the Interface**:
Use the "Font" menu to change the font style.
Use the "Color Theme" menu to change the color scheme of the chat interface.


Developer
Vignesh N
