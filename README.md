# Instrument Splitter
## Description
Instrument Splitter is a Python script designed to separate vocal tracks from instruments in an audio file. It uses machine learning models to perform this separation accurately, saving the resulting tracks in distinct folders.

## Operation
After running the script, audio files are processed and divided into two categories:
- **no_vocals/**: Contains the track without vocals.
- **vocals/**: Contains only the vocals.

Resulting structure:
```
|-- Instrument_Splitter.py
|-- requirements.txt
|-- separated_audio/
    |-- no_vocals/
        |-- Dany Tranchillo - Onlyjob (Djent)_no_vocals.mp3
        |-- Flapjackers - Pick Up The Pieces_no_vocals.mp3
        |-- Ion Chi - Town Shuffle (Jason Hodges remix)_no_vocals.mp3
        |-- Marc Fairfield - That Funk_no_vocals.mp3
        |-- Massive Attack - Paradise Circus_no_vocals.mp3
        |-- Phonique - Casualities_no_vocals.mp3
    |-- vocals/
        |-- Dany Tranchillo - Onlyjob (Djent)_vocals.mp3
        |-- Flapjackers - Pick Up The Pieces_vocals.mp3
        |-- Ion Chi - Town Shuffle (Jason Hodges remix)_vocals.mp3
        |-- Marc Fairfield - That Funk_vocals.mp3
        |-- Massive Attack - Paradise Circus_vocals.mp3
        |-- Phonique - Casualities_vocals.mp3
|-- venv/
```

### 1. Creating the Working Directory
Create a dedicated folder to place the script. For example: Instrument_Splitter

### 2. Installation
1. Navigate to the newly created folder and open the command prompt.
2. Download the repository
Clone the GitHub repository by executing:
```sh
git clone https://github.com/Tranchillo/Instrument_Splitter.git
```

### 3. Creating the Virtual Environment and Installing Dependencies
#### **Windows**
```sh
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

#### **Linux/macOS** *(not tested on these systems)*
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Installing Torch
Depending on your system configuration, you need to manually install the correct version of Torch:

#### **For NVIDIA GPU**
```sh
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

#### **For CPU**
```sh
pip install torch torchvision torchaudio
```

## Usage
Make sure the virtual environment is active, navigate to the main directory and run:

#### **Windows**
```sh
venv\Scripts\activate
python Instrument_Splitter.py
```

#### **Linux/macOS**
```sh
source venv/bin/activate
python3 Instrument_Splitter.py
```

## License
This project is open-source and must remain free for all users. Contributions and improvements are welcome!
