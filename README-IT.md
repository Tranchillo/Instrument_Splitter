# Instrument Splitter

## Descrizione
Instrument Splitter è uno script Python progettato per separare la traccia vocale dagli strumenti in un file audio. Utilizza modelli di machine learning per eseguire questa separazione in modo accurato, salvando le tracce risultanti in cartelle distinte.

## Funzionamento
Dopo l'esecuzione dello script, i file audio vengono processati e suddivisi in due categorie:
- **no_vocals/**: Contiene la traccia senza voce.
- **vocals/**: Contiene solo la voce.

Struttura risultante:
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

### 1. Creazione della cartella di lavoro
Creare una cartella dedicata in cui posizionare lo script. Ad esempio: Instrument_Splitter

### 2. Installazione
1. Posizionarsi all'interno della cartella appena creata e aprire il prompt dei comandi.
2. Scaricare il repository
Clonare il repository GitHub eseguendo:
```sh
git clone https://github.com/Tranchillo/Instrument_Splitter.git
```

### 3. Creazione dell'ambiente virtuale e installazione delle dipendenze
#### **Windows**
```sh
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

#### **Linux/macOS** *(non testato su questi sistemi)*
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Installazione di Torch
A seconda della configurazione del sistema, è necessario installare manualmente la versione corretta di Torch:

#### **Per GPU NVIDIA**
```sh
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

#### **Per CPU**
```sh
pip install torch torchvision torchaudio
```

## Utilizzo
Assicurarsi che l'ambiente virtuale sia attivo, posizionarsi nella directory principale ed eseguire:

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

## Licenza
Questo progetto è open-source e deve rimanere gratuito per tutti gli utenti. Contributi e miglioramenti sono ben accetti!

