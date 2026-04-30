# PyOrganizer: File Organizer 📁
A simple automation script to keep your Downloads folder organized!

## Functionality
The script scans the Downloads folder and moves files into specific subfolders based on their extensions. If a destination folder does not exist, the operating system handles the flow (it is recommended to ensure the folders exist or use `os.makedirs`).

As categorias atuais são:
- 📄 Documents: .pdf, .docx, .txt
- 🖼️ Images: .jpg, .png, .jpeg
- ⚙️ Installer: .exe, .msi
- 📦 Archives/Compressed: .zip, .rar, .7z

## Requirements

- Python 3.8+

## Automation
## 🪟 Windows: 
To facilitate use and save system resources, this project can be converted into an executable (.exe) using PyInstaller and subsequently scheduled via the Task Scheduler.

#### How to generate the .exe:
1. Clone the repository:
```
git clone https://github.com/GabeNodari/PyOrganizer.git
cd PyOrganizer
```
2. Install PyInstaller:
```
python -m pip install pyinstaller
```
3. Generate the file:
```
pyinstaller --onefile --noconsole app.py
```

The final file will be located in the `dist` folder. Using the `--noconsole` flag allows the script to run invisibly, which is ideal for seamless daily integration.

## 🐧 Linux:
On Linux, automation is handled natively using Cron.

#### How to configure the schedule (Cron):
1. Clone the repository:
```
git clone https://github.com/GabeNodari/PyOrganizer.git
cd PyOrganizer
```
2. Verify the Python location:
```
which python3
```
3. Verify the script location.
4. Open the terminal and access the task editor: 
```
crontab -e
```
5. Add a line at the end of the file to define when the script should run.

Example to run every hour of every day:

```
00 * * * * /usr/bin/python3 /full/path/to/app.py
```
