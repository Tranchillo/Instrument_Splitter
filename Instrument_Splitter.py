import os
import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
import subprocess
import torch
import shutil

def select_audio_file():
    """Apre una finestra per selezionare il file audio."""
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Seleziona il file audio",
        initialdir="music_input",  # Parte dalla cartella music_input
        filetypes=[("Audio Files", "*.mp3 *.wav *.flac")]
    )
    return file_path

def save_as_mp3(input_file, output_path):
    """Salva il file audio separato come MP3 usando pydub."""
    audio_segment = AudioSegment.from_file(input_file)
    audio_segment.export(output_path, format="mp3")

def choose_model():
    """Permette all'utente di selezionare un modello numericamente."""
    models = {"1": "htdemucs", "2": "mdx_extra", "3": "light"}
    print("Scegli il modello Demucs:")
    print("1 - htdemucs (Alta qualità, più lento)")
    print("2 - mdx_extra (Buon equilibrio tra qualità e velocità)")
    print("3 - light (Più veloce, qualità inferiore)")
    
    while True:
        choice = input("Inserisci il numero del modello (default: 1): ")
        if choice == "" or choice in models:
            return models.get(choice, "htdemucs")
        else:
            print("Scelta non valida. Riprova.")

def separate_audio(input_file, base_output_folder="separated_audio"):
    """
    Separa gli strumenti da un file audio utilizzando Demucs e salva le tracce separate in cartelle dedicate.
    """
    if not os.path.exists(base_output_folder):
        os.makedirs(base_output_folder)
    
    vocals_folder = os.path.join(base_output_folder, "vocals")
    no_vocals_folder = os.path.join(base_output_folder, "no_vocals")
    
    # Crea le cartelle se non esistono
    os.makedirs(vocals_folder, exist_ok=True)
    os.makedirs(no_vocals_folder, exist_ok=True)
    
    model = choose_model()
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    print(f"Separazione in corso con il modello {model} su {device}...")
    
    try:
        subprocess.run([
            "demucs", "-n", model, "--two-stems", "vocals", "--out", base_output_folder, "--device", device, input_file
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Errore durante l'esecuzione di Demucs: {e}")
        return
    
    # Nome del file senza estensione
    track_name = os.path.splitext(os.path.basename(input_file))[0]
    demucs_output_folder = os.path.join(base_output_folder, model, track_name)
    
    # Verifica l'esistenza della cartella generata
    if not os.path.exists(demucs_output_folder):
        print(f"Errore: la cartella '{demucs_output_folder}' non è stata trovata.")
        return
    
    # Percorsi dei file separati
    vocals_path = os.path.join(demucs_output_folder, "vocals.wav")
    no_vocals_path = os.path.join(demucs_output_folder, "no_vocals.wav")
    
    # Controlla l'esistenza dei file separati
    if os.path.exists(vocals_path) and os.path.exists(no_vocals_path):
        # Crea i nomi dei file di output
        vocals_output_path = os.path.join(vocals_folder, f"{track_name}_vocals.mp3")
        no_vocals_output_path = os.path.join(no_vocals_folder, f"{track_name}_no_vocals.mp3")
        
        # Converti e salva i file separati come MP3
        save_as_mp3(vocals_path, vocals_output_path)
        save_as_mp3(no_vocals_path, no_vocals_output_path)
        
        print(f"File MP3 salvati:")
        print(f"- Vocals: {vocals_output_path}")
        print(f"- No Vocals: {no_vocals_output_path}")
        
        # Rimuovi i file intermedi (.wav)
        os.remove(vocals_path)
        os.remove(no_vocals_path)
        
        # Rimuovi la cartella temporanea generata da Demucs
        shutil.rmtree(os.path.join(base_output_folder, model), ignore_errors=True)
        print("Cartella temporanea rimossa.")
    else:
        print("Errore: i file separati non sono stati trovati.")

if __name__ == "__main__":
    print("Seleziona il file audio da separare")
    input_audio = select_audio_file()
    
    if not input_audio:
        print("Nessun file selezionato. Uscita.")
    else:
        separate_audio(input_audio)