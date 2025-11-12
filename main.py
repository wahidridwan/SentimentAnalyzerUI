
import tkinter as tk
from textblob import TextBlob

def analyze_sentiment():
    text_input = text_box.get("1.0", tk.END).strip()
    if not text_input:
        result_label.config(text="Please enter some text!")
        return

    lines = text_input.split("\n")
    results = []
    total_polarity = 0

    for i, line in enumerate(lines, 1):
        if line.strip():
            blob = TextBlob(line)
            polarity = blob.sentiment.polarity
            total_polarity += polarity
            if polarity > 0:
                sentiment = "Positive"
            elif polarity < 0:
                sentiment = "Negative"
            else:
                sentiment = "Neutral"
            results.append(f"Line {i}: {sentiment} (Polarity: {polarity:.2f})")

    avg_polarity = total_polarity / len(lines) if lines else 0
    results.append(f"\nOverall Polarity: {avg_polarity:.2f}")
    if avg_polarity > 0:
        overall = "Overall Sentiment: Positive 😊"
    elif avg_polarity < 0:
        overall = "Overall Sentiment: Negative 😔"
    else:
        overall = "Overall Sentiment: Neutral 😐"
    results.append(overall)

    result_label.config(text="\n".join(results))

# --- UI Setup ---
root = tk.Tk()
root.title("Sentiment Analyzer (TextBlob)")
root.geometry("600x500")
root.config(bg="#1e1e1e")

title_label = tk.Label(root, text="🧠 Sentiment Analyzer", font=("Helvetica", 18, "bold"), bg="#1e1e1e", fg="#00ffcc")
title_label.pack(pady=10)

text_box = tk.Text(root, height=10, width=60, font=("Consolas", 12), bg="#2d2d2d", fg="#ffffff", insertbackground="white")
text_box.pack(pady=10)

analyze_button = tk.Button(root, text="Analyze Sentiment", command=analyze_sentiment, bg="#00ffcc", fg="black", font=("Helvetica", 12, "bold"), width=20)
analyze_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Consolas", 11), bg="#1e1e1e", fg="#ffffff", justify="left")
result_label.pack(pady=10)

footer = tk.Label(root, text="Developed by Wahid Ridwan | Using TextBlob", font=("Helvetica", 9), bg="#1e1e1e", fg="#888888")
footer.pack(side="bottom", pady=10)

root.mainloop()
