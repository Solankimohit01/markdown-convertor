# 📝 Markdown to HTML Converter (CLI Tool)

A lightweight and user-friendly Python command-line tool that converts Markdown (`.md`) files into clean HTML files and opens them automatically in your default web browser. This project is also packaged as a standalone `.exe` for easy sharing and use on any Windows system without Python installed.

---

## 📌 Features

- 🔹 Simple and interactive CLI tool
- 🔹 Converts any `.md` file to `.html` using Python
- 🔹 Displays conversion progress and success message
- 🔹 Automatically opens the converted HTML file in the browser
- 🔹 `.exe` version included for Windows users (no Python needed)
- 🔹 Custom icon branding for professional look

---

## 📽️ Demo

```

## Welcome to Markdown to HTML Converter!

📄 Enter the path to your Markdown (.md) file: sample.md
⏳ Converting...
✅ Conversion successful! Opening the HTML file in your browser...

````

---

## 🚀 Getting Started

### 🐍 Option 1: Run with Python

#### 1. **Clone the repository**
```bash
git clone https://github.com/your-username/markdown-html-converter.git
cd markdown-html-converter
````

#### 2. **Install the required package**

```bash
pip install markdown
```

#### 3. **Run the tool**

```bash
python converter.py
```

---

### 🪟 Option 2: Use the `.exe` (no Python required)

If you're using Windows:

1. Go to the [`dist/`](./dist) folder
2. Run `converter.exe` by double-clicking
3. Follow the on-screen instructions

✅ You don’t need to install Python or any dependencies!

---

## 🛠️ How It Works

* Prompts the user to input a `.md` file path
* Uses the `markdown` library to convert content to HTML
* Saves the output as `output.html`
* Opens the HTML file in the default browser

---

## 📂 Project Structure

```
markdown-html-converter/
├── converter.py         # Main Python script
├── icon.ico             # App icon for the .exe
├── README.md            # Project documentation
├── build_converter.bat  # Optional: build script for .exe
├── dist/
│   └── converter.exe    # Compiled Windows executable
└── sample.md            # Example markdown file (optional)
```

---

## 📦 Packaging into `.exe` (Developer Guide)

To convert the Python script into a `.exe`:

### Step 1: Install PyInstaller

```bash
pip install pyinstaller
```

### Step 2: Run PyInstaller with icon

```bash
pyinstaller --onefile --console --icon=icon.ico converter.py
```

### Step 3: Locate the `.exe` file

Check the `dist/` folder for `converter.exe`.

---

## 🧪 Example Markdown Input

```markdown
# Welcome

This is a *markdown* example.

- Item 1
- Item 2

**Bold Text**

[Click me](https://example.com)
```

🡆 Converts to:

```html
<h1>Welcome</h1>
<p>This is a <em>markdown</em> example.</p>
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
</ul>
<p><strong>Bold Text</strong></p>
<a href="https://example.com">Click me</a>
```

---

## 📋 Requirements

* Python 3.6+
* `markdown` library

---

## 👤 Author

**Mohit Solanki**

MCA Student | Python Developer

📧 [solankimohit985@gmail.com](mailto:solankimohit985@gmail.com)

🔗 [LinkedIn](https://www.linkedin.com/in/mohit-solanki-551a2b324)

🔗 [GitHub](https://github.com/Solankimohit01)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 💡 Suggestions or Issues?

Feel free to [open an issue](https://github.com/your-username/markdown-html-converter/issues) or submit a pull request.

---

