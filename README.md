# ℹ️ Information

This project aims to automate textual data analysis using Natural Language Processing (NLP) on `.txt` files.  
For each file added to the `input/` folder, a corresponding image will be generated in the `output/` folder.  
The image contains sentiment analysis and descriptive statistics extracted from the text.

![sentiment_analysis](https://github.com/user-attachments/assets/89c3a0cd-6e2e-43c3-a36f-dd999329e55b)

## ⚙️ How It Works

Each text is processed into a vector of alphanumeric words. Punctuation and stop words are removed during preprocessing. The core analysis is performed by a C++ algorithm called **Stringler**, which is compiled and executed via Python using `pybind11`. Python handles the input/output flow, feeds the text to the C++ module, and inserts the results into a visual template per file.

The sentiment analysis is based on word classification into **positive**, **neutral**, and **negative** categories.

## ✨ Features

- **reaction**: sentiment score based on word classification
- **emotion**: count of emotional words
- **tokens**: total number of words
- **fashion**: most frequent word
- **largest**: longest word
- **unigrams**: number of unique single words
- **bigrams**: number of unique two-word sequences
- **trigrams**: number of unique three-word sequences
- **mean**: average word length
- **std**: standard deviation of word lengths
- **ttr**: type-token ratio (lexical diversity)
- **skew**: skewness of word length distribution
- **kurtosis**: kurtosis of word length distribution
- **jb**: Jarque-Bera test for normality

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/aryelsoares/stringler.git
cd stringler
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Compile the C++ module

Make sure you have the following installed:

- A C++ compiler (e.g. `g++`)
- `pybind11`
- `make`

```bash
make all
```

### 4. Update font directory

Replace font directories from `fonts.json` to one compatible with your OS for text injection.

- **fnt1**: /usr/share/fonts/TTF/Arialbd.TTF.
- **fnt2**: /usr/share/fonts/TTF/Arial.TTF.

## 🛠️ Usage

Add your `.txt` files to the `input/` directory. Then run:

```bash
python generate_reports.py
```

The resulting images will be saved in the `output/` folder.

## 📝 Notes

This project is intended as a learning example that combines software engineering with data science workflows. For real-world sentiment analysis, you may consider using pre-trained NLP models such as **BERT**, **XLNet**, or similar transformers for improved performance and context awareness.
