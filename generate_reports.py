import sys
sys.path.append("build")

from Stringler import Stringler # type: ignore
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import json
import os
import io

# Load Data
def load_all() -> None:
    input_dir = 'input'
    files = [f for f in os.listdir(input_dir) if f.endswith('.txt')]
    total = len(files)

    for i, filename in enumerate(files, start=1):
        filepath = os.path.join(input_dir, filename)
        img = Image.open("template/info.png").convert("RGBA")
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()
            data = Stringler(text)
            graph(data, img)
            stats(data, img, filename)
        
        # Progress bar
        progress = int((i / total) * 100)
        bar = ('#' * (progress // 2)).ljust(50)
        sys.stdout.write(f'\rProcessing files: [{bar}] {progress}%')
        sys.stdout.flush()

    print("\nAll files processed.")

# Graphics
def graph(data: Stringler, img: Image) -> None:
    # === PIE CHART ===
    reaction = data.reaction()
    keys = list(reaction.keys())
    values = list(reaction.values())
    colors = ['red', 'cyan', 'green']

    fig1, ax1 = plt.subplots()
    if sum(values) != 0:
        idx = 0
        while idx < len(values): # remove missing categories
            if values[idx] == 0:
                del keys[idx], values[idx], colors[idx]
            else:
                idx += 1
        ax1.pie(values, labels=keys, colors=colors,
        autopct='%.1f%%', shadow=True, startangle=45)
    else: # no reaction
        ax1.pie([1], labels=['No reaction'], colors=['lightgray'])
    ax1.axis('equal')
    plt.tight_layout()

    pie_buf = io.BytesIO()
    plt.savefig(pie_buf, format='PNG', transparent=True)
    plt.close(fig1)
    pie_buf.seek(0)

    pie_img = Image.open(pie_buf).resize((500, 400))
    img.paste(pie_img, (75, 200), pie_img)

    # === BARH CHART ===
    positiveList = ["adequate", "attached", "attracted", "ecstatic", "esteemed", "fearless",
                    "focused", "free", "happy", "independent", "loved", "safe"]
    neutralList = ["average", "entitled", "justful", "surprise"]

    emotion = data.emotion()
    keys = list(emotion.keys())
    values = list(emotion.values())

    barLabel, barColor = [], []
    seen = {"Positive": False, "Neutral": False, "Negative": False}

    for word in keys: # color legend
        if word in positiveList:
            label = "Positive" if not seen["Positive"] else "_Positive"
            barColor.append('tab:green')
            seen["Positive"] = True
        elif word in neutralList:
            label = "Neutral" if not seen["Neutral"] else "_Neutral"
            barColor.append('tab:cyan')
            seen["Neutral"] = True
        else:
            label = "Negative" if not seen["Negative"] else "_Negative"
            barColor.append('tab:red')
            seen["Negative"] = True
        barLabel.append(label)
    
    fig2, ax2 = plt.subplots()
    if barLabel:
        ax2.barh(keys, values, label=barLabel, color=barColor)
    else: # no emotion
        ax2.barh(['No emotion'], [0], label=['Empty'], color='lightgray')
    
    ax2.set_xlabel('Frequency')
    ax2.set_ylabel('Emotions')
    ax2.legend(title='Category')
    plt.tight_layout()

    bar_buf = io.BytesIO()
    plt.savefig(bar_buf, format='PNG', transparent=True)
    plt.close(fig2)
    bar_buf.seek(0)

    bar_img = Image.open(bar_buf).resize((450, 400))
    img.paste(bar_img, (600, 200), bar_img)

# Statistics
def stats(data: Stringler, img: Image, filename: str) -> None:
    draw = ImageDraw.Draw(img)
    fnt_dir1, fnt_dir2 = "", ""

    with open('fonts.json') as f:
        file = json.load(f)
        fnt_dir1 = file["fnt1"]
        fnt_dir2 = file["fnt2"]

    fnt = ImageFont.truetype(fnt_dir1, 14)
    # Filename
    draw.text((120, 29), filename, font=fnt, fill="black", anchor="la")
    # Tokens
    tokens = str(data.getSize())
    draw.text((350, 686), tokens, font=fnt, fill="black", anchor="mm")
    # Fashion
    fashion = data.fashion()
    draw.text((350, 716), fashion, font=fnt, fill="black", anchor="mm")
    # Largest
    largest = data.largest()
    draw.text((350, 746), largest, font=fnt, fill="black", anchor="mm")
    # Unigrams
    unigrams = str(len(data.polygrams()))
    draw.text((550, 686), unigrams, font=fnt, fill="black", anchor="mm")
    # Bigrams
    bigrams = str(len(data.polygrams(2)))
    draw.text((550, 716), bigrams, font=fnt, fill="black", anchor="mm")
    # Trigrams
    trigrams = str(len(data.polygrams(3)))
    draw.text((550, 746), trigrams, font=fnt, fill="black", anchor="mm")
    # Mean
    mean = str(round(data.mean(), 2))
    draw.text((700, 686), mean, font=fnt, fill="black", anchor="mm")
    # Std
    std = str(round(data.std(), 2))
    draw.text((700, 716), std, font=fnt, fill="black", anchor="mm")
    # TypeTokenRatio
    ttr = str(round(data.typeTokenRatio() * 100, 2)) + "%"
    draw.text((700, 746), ttr, font=fnt, fill="black", anchor="mm")
    # Skew
    skew = str(round(data.skew(), 2))
    draw.text((865, 686), skew, font=fnt, fill="black", anchor="mm")
    # Kurtosis
    kurtosis = str(round(data.kurtosis(), 2))
    draw.text((865, 716), kurtosis, font=fnt, fill="black", anchor="mm")
    # Jarque-Bera
    jarqueBera = str(round(data.jarqueBera(), 2))
    draw.text((865, 746), jarqueBera, font=fnt, fill="black", anchor="mm")
    # Copyright
    fnt2 = ImageFont.truetype(fnt_dir2, 10)
    copyright = "Copyright © 2025, by aryelsoares"
    draw.text((1052, 800), copyright, font=fnt2, fill="black", anchor="mm")
    # save image
    os.makedirs("output", exist_ok=True)
    base = os.path.splitext(filename)[0]
    img.save("output/" + base + ".png")

# Main
def main():
    print("-" * 40 + "\n🚀 Starting analysis with Stringler" + "\n" + "-" * 40)
    load_all()
    print("\n✅ Process completed successfully!\n")

if __name__ == '__main__':
    main()
