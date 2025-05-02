# **Picture Reconnaissance Tool User Manual**  
Author: Stephen Littman  
Date: April 27, 2025  

# **Abstract**  
This document provides comprehensive guidance on the usage and functionality of the **Picture Reconnaissance Tool**, which utilizes **face_recognition** technology to scan and match images. The tool consists of a Tkinter-based GUI (`picture_reconnaissance.py`) and an image-processing module (`collect_all_images.py`). Users can leverage this application to detect faces within an image folder and extract matching images automatically.

# **Introduction**  
The **Picture Reconnaissance Tool** is designed to facilitate face detection and image sorting through an intuitive graphical user interface. It integrates **os**, **sys**, **face_recognition**, **Pillow**, and **Tkinter** to ensure seamless interaction and usability.

# **System Requirements**  
### **Hardware Requirements**  
- Operating System: Windows, macOS, or Linux  
- RAM: Minimum **4GB** (Recommended **8GB+** for optimal performance)  
- Storage: At least **500MB** available disk space  

### **Recommendations**
- **Python Virtual Environment**: 
- It is recommended that before installing the dependencies you build and activate a Python virtual environment Python using the following commands:
- Windows PowerShell
  ```bash
  cd <into_the_directory_of_the_program>

  python -m venv <environment_name>

  <environment_name>/Scripts/activate
  ```
- Linux Terminal
  ```bash
  cd <into_the_directory_of_the_program>

  python -m venv <environment_name>

  source <environment_name>/bin/activate 
  ```

### **Software Requirements**  
- **Python 3.x** (Latest version recommended)

- Dependencies:  
  ```bash
  pip install -r requirements.txt
  ```

# **Installation Steps**  
1. Download and install **Python 3.x** from [python.org](https://www.python.org).  
2. Download the project code.
3. Install the necessary dependencies using the following command:  
   ```bash
   pip install -r requirements.txt
   ```
4. Run the GUI application:  
   ```bash
   python picture_reconnaissance.py
   ```

# **Usage Instructions**  
### **Launching the Application**  
1. **Run the `picture_reconnaissance.py` file** in Python.  
2. The graphical interface will open, allowing the user to interact with the tool.

### **Using the GUI**  
The graphical interface provides **four interactive buttons**:  
- **Select Image:** Choose a reference image.  
- **Select Folder:** Choose the folder containing images to scan.  
- **Select Output Folder:** Select where matching images will be saved.  
- **Detect Faces:** Start the scanning process and retrieve matching images.  

Once processing is complete, a **notification will appear**, confirming that matching images have been copied.

# **Technical Overview**  
### **Functionality of `collect_all_images.py`**  
- Loads a **reference image** and extracts its facial encoding.  
- Iterates through images in a folder and **compares faces** with the reference image.  
- If a match is found, the image is **copied** to the output folder.

### **Functionality of `picture_reconnaissance.py`**  
- Implements a **Tkinter-based GUI** for ease of use.  
- Allows users to **select images and folders interactively**.  
- Calls `collect_all_images.py` to **process and retrieve** matching images.

# **Troubleshooting**  
### **Common Issues & Solutions**  
| Issue | Solution |
|------|---------|
| Python not found | Ensure Python is installed and added to system path |
| Dependencies missing | Run `pip install -r requirements.txt` |


