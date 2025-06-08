# ❤️‍🔥 EKG App – Analyse & Visualisierung von Trainingsdaten

## 🧾 Übersicht

Die **EKG App** dient der intuitiven Visualisierung und Analyse von Trainingsdaten (Leistung & Herzfrequenz) einer Versuchsperson. Sie ermöglicht:

- die Auswahl einer Testperson,
- das Festlegen der maximalen Herzfrequenz,
- sowie die grafische Darstellung von Leistungsdaten und Herzfrequenzzonen (HR-Zonen).

Dabei werden automatisch folgende Kennwerte berechnet:

- 🏋️‍♂️ Durchschnittliche und maximale Leistung  
- ⏱️ Verweildauer in den einzelnen HR-Zonen  
- 📊 Durchschnittliche Leistung je Herzfrequenzzone  

---

## 🚀 App starten

### 🔧 Voraussetzungen

- 🐍 Python ≥ 3.8  
- 📦 Paketmanager [PDM](https://pdm.fming.dev/)  
- 📄 Abhängigkeiten laut `pyproject.toml`

### ▶️ Schritt-für-Schritt-Anleitung

1. Repository klonen:
   ```bash
   git clone https://github.com/KRSI58/programmieruebung_2-5.git
   ```

2. Projekt initialisieren:
   ```bash
   pdm init
   ```

3. App starten:
   ```bash
   streamlit run main.py
   ```
---
## 🖼️APP Screenshot
![alt text](screenshot.png)

---
## 🖼️APP Screenshot (Aufgabe 5)
![image](https://github.com/user-attachments/assets/eb3698f2-8a48-46fa-ba6e-9d5ae2505a35)

---
## 🗂️Projektstruktur

|📁Datei/Ordner          | 📝Beschreibung                                                   |
| --------------------- | -------------------------------------------------------------- |
| `data/`               | Übergeordneter Ordner für alle Daten                           |
| `data/activities/`    | Aktivitätsdaten der Testpersonen                               |
| `data/ekg_data/`      | EKG-Rohdaten der Trainingssessions                             |
| `data/pictures/`      | Profilbilder der Versuchspersonen                              |
| `data/person_db.json` | JSON-Datei mit Stammdaten und EKG-Testverweisen der Personen   |
| `main.py`             | Einstiegspunkt der App                                         |
| `person.py`           | Enthält die Klasse Person zum Laden und Auslesen von Stammdaten|
| `ekg_data.py`         | Enthält die Klasse EKG_data zum Laden, Verarbeiten und Plotten von EKGs|
| `read_pandas.py`      | Funktionen zur Darstellung mit Pandas + Erstellen und Darstellen Powercurve                      |
| `pyproject.toml`      | Definition der Abhängigkeiten und Projektkonfiguration für PDM |
| `pdm.lock`            | Lock-Datei mit exakt aufgelösten Abhängigkeiten                |
| `.gitignore`          | Dateien und Ordner, die von Git ignoriert werden               |
| `README.md`           | Projektbeschreibung und Anleitung zur Nutzung                  |

---

## 🔄Ablaufdiagramm

```mermaid
flowchart TD
    Start[Start] --> LoadData[Lade JSON]
    LoadData --> SelectPerson[Waehle Person]
    SelectPerson --> ShowPicture[Zeige Bild]
    ShowPicture --> SelectEKG[Waehle EKG]
    SelectEKG --> LoadEKG[Lade EKG CSV]
    LoadEKG --> NormalizeTime[Normiere Zeit ab 0]
    NormalizeTime --> FilterWindow[Filtere 15 Sekunden]
    FilterWindow --> DetectPeaks[Finde Peaks]
    DetectPeaks --> CalculateHR[Berechne Herzfrequenz]
    CalculateHR --> Visualize[Zeige Plot]
    Visualize --> End[Ende]


```

---

# ⚡ Aufgabe 4 – Power Curve Analyse

Diese Aufgabe generiert eine **Power Curve** aus Leistungsdaten (in Watt), z. B. aus Radfahr-Aktivitäten.  
Die Power Curve zeigt die **maximal erreichbare Durchschnittsleistung** über verschiedene Zeitintervalle  
(z. B. 5 s, 1 min, 5 min, …) und gibt damit einen schnellen Überblick über die Belastbarkeit der Testperson  
in verschiedenen Phasen der Belastung.

---

## 🖼️ Screenshot

![Power Curve](power_curve.png)

---

## 🔄Ablaufdiagramm Aufgabe 4

```mermaid
flowchart TD
    Start --> LoadData
    LoadData --> FindBestEffort
    FindBestEffort --> GeneratePowerCurve
    GeneratePowerCurve --> PlotPowerCurve
    PlotPowerCurve --> Show_and_Save
    Show_and_Save --> End
```
