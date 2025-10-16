# 🛠️ SVG to PNG Conversion Script

This Python script processes all `.svg` files in the current directory by:
- Replacing a specified color with a new one
- Converting each updated SVG to a `.png` image at 512×512 resolution
- Saving the PNG with a lowercase filename, spaces replaced by underscores, and a custom suffix

---

## ✅ Prerequisites

- **Python 3.7+** installed and added to your system PATH  
  Check with:
  ```bash
  python --version
  ```

- **pip** (Python package manager) installed  
  Check with:
  ```bash
  pip --version
  ```

---

## 📦 Install Required Package

Install the CairoSVG library using pip:

```bash
pip install cairosvg
```

> **Note:** CairoSVG depends on the Cairo graphics engine. If you see an error like  
> `OSError: no library called "cairo-2" was found`, install the GTK runtime:
> - Download from: [GTK for Windows Runtime](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer)
> - Add the `bin` folder (e.g., `C:\Program Files\GTK3-Runtime Win64\bin`) to your system's **PATH** environment variable

---

## 📁 Prepare Your Files

1. Place your `.svg` files in a folder (e.g., `C:\Users\YourName\svg-folder`)
2. Save the Python script as `script.py` in the same folder

---

## 🚀 Run the Script

Open Command Prompt and navigate to the folder:

```bash
cd C:\Users\YourName\svg-folder
```

Run the script:

```bash
python script.py
```

---

## 🧾 Output

- Each `.svg` file will be processed:
  - The specified color will be replaced
  - The result will be saved as a `.png` file
  - The filename will be:
    - Lowercase
    - Spaces replaced by underscores
    - Appended with a suffix (e.g., `logo updated.svg` → `logo_updated.png`)

---

## 🧰 Customization

You can modify the following variables in the script:

```python
old_color = "#ff0000"  # Color to replace
new_color = "#00ff00"  # Replacement color
suffix = "_updated"    # Suffix for output filenames
width = 512            # PNG width
height = 512           # PNG height
```

---
