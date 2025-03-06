# GlobalNewsBot - Telegram News Bot

**GlobalNewsBot** is a Telegram bot designed to provide users with the latest news from around the world. By simply selecting a country, users can receive top headlines directly in their Telegram chat. This bot leverages the **NewsAPI** to fetch real-time news and delivers it in a clean, easy-to-read format.

---

## Features

- **Country-Specific News**: Users can request news from any country by entering its 2-letter ISO code (e.g., `us` for the United States, `ir` for Iran, `de` for Germany).
- **Top Headlines**: Fetches the top 5 news articles for the selected country.
- **User-Friendly Interaction**: The bot guides users through a simple conversation to select their desired country.
- **Real-Time Updates**: News is fetched in real-time using the **NewsAPI**.
- **Error Handling**: Handles invalid country codes and API errors gracefully.

---

## How It Works

1. The bot starts with the `/start` command, welcoming the user and explaining how to use the bot.
2. When the user sends the `/news` command, the bot asks for the 2-letter country code.
3. The user enters the country code (e.g., `us`, `ir`, `de`).
4. The bot fetches the top 5 news headlines for the specified country using the **NewsAPI**.
5. The bot sends the news titles along with their URLs to the user.

---

## Technologies Used

- **Python**: The core programming language used to build the bot.
- **python-telegram-bot (v20+)**: A modern and asynchronous library for interacting with the Telegram Bot API.
- **NewsAPI**: A free API for fetching real-time news from various sources worldwide.
- **Requests**: A Python library for making HTTP requests to the NewsAPI.

---

## Setup Instructions

### Prerequisites

1. **Telegram Bot Token**:
   - Create a new bot using [BotFather](https://t.me/BotFather) on Telegram.
   - Save the bot token provided by BotFather.

2. **NewsAPI Key**:
   - Sign up for a free API key at [NewsAPI](https://newsapi.org/).
   - Save the API key.

3. **Python Environment**:
   - Ensure Python 3.7 or higher is installed.
   - Install the required libraries using `pip`.

---

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/GlobalNewsBot.git
   cd GlobalNewsBot
   ```

2. Install the required Python libraries:
   ```bash
   pip install python-telegram-bot requests
   ```

3. Replace the placeholders in the script:
   - Replace `YOUR_TELEGRAM_BOT_TOKEN` with your actual Telegram bot token.
   - Replace `YOUR_NEWSAPI_KEY` with your actual NewsAPI key.

4. Run the bot:
   ```bash
   python bot.py
   ```

---

## Usage

1. Start the bot by sending `/start` in Telegram.
2. Use the `/news` command to request news.
3. Enter the 2-letter country code (e.g., `us`, `ir`, `de`) when prompted.
4. The bot will send the top 5 news headlines for the selected country.

---

## Example Interaction

```
User: /start
Bot: Hello! To get the latest news, use the /news command.

User: /news
Bot: Please enter the 2-letter country code (e.g., us, ir, de, fr):

User: us
Bot: Here are the top 5 news headlines for the United States:
📰 Breaking News: Major Event Happens
🔗 https://example.com/news/123

📰 Stock Market Update
🔗 https://example.com/news/456
```

---

## Project Structure

```
GlobalNewsBot/
│
├── bot.py                # Main bot script
├── README.md             # Project documentation
├── requirements.txt      # List of dependencies
```

---

## Contributing

Contributions are welcome! If you'd like to improve this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **NewsAPI** for providing a free and reliable news API.
- **python-telegram-bot** for their excellent library and documentation.
- The open-source community for continuous inspiration and support.

---

## Contact

For questions or feedback, feel free to reach out:

- **Email**: your-email@example.com
- **GitHub**: [your-username](https://github.com/your-username)

---

Enjoy staying updated with **GlobalNewsBot**! 🌍📰
