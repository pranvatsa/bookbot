# 📚 BookBot

Ever wondered how many times 'e' appears in Frankenstein? **BookBot** knows!  
A fun and simple command-line tool for analyzing the contents of a text file (like a book).  
Created as part of the [Boot.dev curriculum](https://www.boot.dev/courses/build-bookbot-python).

---

## 🚀 Features

- Counts the total number of words in a book.
- Counts the frequency of each character (case-insensitive, alphabetic only).
- Outputs a clean, formatted report.

---

## 🛠️ Usage

1. **Add your books**  
   Place your `.txt` files in the `books/` directory (e.g., `books/frankenstein.txt`, `books/mobydick.txt`).

2. **Run BookBot**  
   Open your terminal and run:

   ```
   python3 main.py <path_to_book>
   ```

   Example:

   ```
   python3 main.py books/frankenstein.txt
   ```

3. **See the magic**  
   The program will print a report showing the word count and character frequencies.

---

## 🐍 Requirements

- Python 3.7 or higher

---

## 📁 Project Structure

```
bookbot/
├── books/
│   ├── frankenstein.txt
│   ├── mobydick.txt
│   └── prideandprejudice.txt
├── main.py
├── stats.py
└── README.md
```

---

## 📝 Example Output

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
...
============= END ===============
```

---

## 📜 License

MIT License

---