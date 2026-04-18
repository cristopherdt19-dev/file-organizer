# File Organizer Script

## Description
This Python script automatically organizes files inside a selected folder into subfolders based on their file type.

It is designed as a practical automation tool that improves file management and demonstrates real-world scripting capabilities.

## Features
- Categorizes files by type (Images, Documents, Videos, etc.)
- Automatically creates destination folders
- Handles duplicate file names safely
- Supports multiple file formats (including 3D models and system files)
- Interactive loop for multiple executions
- Generates a log file with timestamps

## Technologies Used
- Python 3
- os (file system handling)
- shutil (file operations)
- datetime (logging timestamps)

## How to Run
1. Clone the repository:
   git clone <your-repo-url>

2. Navigate to the project folder:
   cd file-organizer

3. Run the script:
   python main.py

4. Enter the folder path when prompted

## Example Output
Moved: report.pdf -> PDF  
Moved: image.png -> Images  
Moved: model.stl -> 3D_Models  

Organization completed.  
Total files moved: 15  
Categories created: 6  

## Future Improvements
- Add GUI interface
- Add configuration file for custom categories
- Export logs to structured formats (CSV/JSON)

## Author
Cristopher Delgado Tamariz
