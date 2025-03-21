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
