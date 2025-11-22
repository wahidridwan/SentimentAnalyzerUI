# 🧠 Sentiment Analyzer (UI Based Mini Project)

![Sentiment Analyzer UI](/mnt/data/986aa596-000c-4d5b-b5fa-93ce0a4efb90.png)

### 📋 Description
This is a mini Python project with a graphical interface (Tkinter) that analyzes the sentiment of text using **TextBlob**.

Each line of input text is analyzed separately, and the app displays:
- Individual line sentiment (Positive / Negative / Neutral)
- Polarity scores for each line
- Overall average polarity and sentiment

### 🚀 How to Run
1. Install required library:
   ```bash
   pip install textblob
   ```

2. Run the app:
   ```bash
   python main.py
   ```

3. Type multiple lines in the text box and click **Analyze Sentiment**.

### 🧩 Features
- Multi-line input support
- Separate line-by-line sentiment results
- Overall polarity and sentiment calculation
- Clean Tkinter-based dark UI

### 🛠 Project Structure (example)
```
SentimentAnalyzerUI/
├─ main.py
├─ requirements.txt
├─ screenshot.png  # or images/screenshot.png
└─ README.md
```

### ✅ Notes & Tips
- If README image does not display on GitHub after you upload, place the screenshot inside an `images/` folder and update the path:
  ```
  ![Sentiment Analyzer UI](images/screenshot.png)
  ```
- Make sure the uploaded screenshot is not 0 bytes (use GitHub web upload or Git push).
- If you're using relative paths, ensure README.md and the image are in the same branch and committed.

---

**Developed by:** Wahid Ridwan  
**Language:** Python 3  
**Library:** TextBlob
