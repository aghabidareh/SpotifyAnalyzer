# 🎵 Spotify Analyzer Dashboard

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Dash](https://img.shields.io/badge/Dash-Plotly-1DB954?style=flat&logo=plotly)](https://dash.plotly.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

<div align="center">
  <img src="https://storage.googleapis.com/pr-newsroom-wp/1/2018/11/Spotify_Logo_RGB_Green.png" alt="Spotify Logo" width="200"/>
</div>

An interactive web-based dashboard for analyzing Spotify music data, built with Python, Dash, and Plotly. Discover insights about your favorite music through beautiful visualizations and powerful analytics.

## ✨ Features

### 🎯 Interactive Analysis
- Interactive data visualization of Spotify tracks
- Filter data by genres and popularity range
- Track details view on click
- Data export functionality

### 🎨 Audio Features Analysis
- **Danceability** - How suitable a track is for dancing
- **Energy** - Measure of intensity and activity
- **Valence** - Musical positiveness conveyed by a track
- **Loudness** - Overall loudness of a track in decibels
- **Tempo** - Overall estimated tempo in BPM
- **Acousticness** - Confidence measure of whether the track is acoustic
- **Speechiness** - Presence of spoken words in a track
- **Instrumentalness** - Predicts whether a track contains no vocals
- **Liveness** - Presence of an audience in the recording

### 📊 Visualization Types
- 📈 Scatter plots
- 📊 Histograms
- 📦 Box plots
- 📑 Bar charts

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Required Python packages:
  ```bash
  pandas
  plotly
  dash
  dash-bootstrap-components
  ```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/aghabidareh/SpotifyAnalyzer.git
cd SpotifyAnalyzer
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## 💻 Usage

1. Ensure you have the `data.csv` file in the project directory
2. Run the application:
```bash
python main.py
```
3. Open your web browser and navigate to `http://127.0.0.1:8050/`

## 📁 Data Structure

The application uses a CSV file (`data.csv`) containing Spotify track data with the following features:
- 🎵 Track name
- 👨‍🎤 Artist name
- 🎼 Genre
- ⭐ Popularity
- 🎹 Audio features (danceability, energy, valence, etc.)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License

This project is licensed under the terms of the license included in the repository.

## 🙏 Acknowledgments

- 🎨 Built with [Dash](https://dash.plotly.com/) and [Plotly](https://plotly.com/)
- 💅 Styled with [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/)
- 🎵 Data provided by Spotify Web API

---

<div align="center">
  Made with ❤️ for music lovers
</div>