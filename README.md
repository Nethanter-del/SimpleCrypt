# SimpleCrypt
# EXE Cryptor - Morphing and Mutating EXE Files

This project provides a tool to obfuscate and modify executable files by:  
- Morphing with functionality from other applications.  
- Copying digital certificates to maintain legitimacy.  
- Adding junk functions to increase complexity.  
- Mutating the EXE to avoid detection by static analysis tools.  

## Features
- **EXE Morphing:** Combine features of different applications into a single executable.  
- **Certificate Cloning:** Duplicate and embed digital certificates from trusted executables.  
- **Junk Function Injection:** Adds random, unused code to increase file complexity.  
- **Mutation Engine:** Modifies the EXE structure to evade static analysis and signature-based detection.  

![Original EXE](1.png)
![Obfuscated EXE](2.png)

## Requirements
- Python 3.8 or later  
- [PyInstaller](https://pyinstaller.org)  

Install dependencies using pip:  
```bash
pip install pyinstaller
