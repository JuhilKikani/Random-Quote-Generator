from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
      "Success की सबसे खास बात है की, वो मेहनत करने वालों पर फ़िदा हो जाती है।",
      "दूसरों के चेहरे हम याद रखें हमारी ऐसी फितरत नहीं लोग हमारा चेहरा देख के अपनी फितरत बदल ले ऐसी हमारी फितरत है।",
      "जिसने भी खुद को खर्च किया है, दुनिया ने उसी को Google पर Search किया है।",
      "या तो आप अपनी Journey में लग जाओ ,नहीं तो लोग आपको अपने Journey में शामिल कर लेंगे।"
]

@app.route('/')
def index():
    random_quote = random.choice(quotes)
    return render_template('index.html', quote=random_quote)

if __name__ == '__main__':
    app.run(debug=True)
