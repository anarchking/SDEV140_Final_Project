# 📷 Picture Reconnaissance Tool

## 📝 Overview
This project is a **face recognition tool** that identifies matching faces within a set of images using `face_recognition`. It consists of:
- **`collect_all_images.py`**: Scans images in a folder and finds matches based on a reference image.
- **`picture_reconnaissance.py`**: A **Tkinter-based GUI** that integrates `collect_all_images.py` for an interactive experience.

## ✨ Features
✅ Select a **reference image** for face matching  
✅ Choose a **folder** containing images to scan  
✅ Pick an **output folder** where matching images will be saved  
✅ Detect faces and **copy matching images** to the output folder  
✅ User-friendly **GUI built with Tkinter**  

## 🔧 Installation
### **Prerequisites**
Ensure you have **Python 3.x** installed along with the required dependencies.

To install dependencies, run:
```bash
pip pip install -r requirements.txt
```
Please see user manual.md for more information.
## 🚀 Usage Steps
1️⃣ **Run the GUI application:**  
   ```bash
   python picture_reconnaissance.py
   ```
2️⃣ **Select an image file** as a reference.  
3️⃣ **Choose a folder** of images for scanning.  
4️⃣ **Pick an output folder** for saving results.  
5️⃣ **Click "Detect Faces"** to start processing.  

## 🏗️ Code Structure
### 🔹 `collect_all_images.py`
- Loads a **reference image** and extracts its facial encoding.
- Iterates through images in a folder, detecting faces and comparing them to the **reference encoding**.
- Copies **matching images** into the designated output folder.

### 🔹 `picture_reconnaissance.py`
- Implements a **graphical interface** using **Tkinter**.
- Provides buttons for selecting the **reference image**, **input folder**, and **output folder**.
- Uses `os`, `sys`, and `collect_all_images.py` to process the selected folder and copy matching results.

## ⚖️ License
📜 This program is distributed under the **GNU General Public License v3**.  
See [GNU License](http://www.gnu.org/licenses/) for details.

## 👤 Author
Developed by **Stephen Littman**.