# 🎵 Spotify Artist Explorer

## 📋 Overview  
The **Spotify Artist Explorer** is an interactive web application built with **Streamlit** that allows users to explore artist information from the Spotify platform.  
With this app, you can:  
- Search for an artist by name.  
- View basic artist data such as popularity, followers, and profile image.  
- Explore top tracks with album covers, clickable links, and even embedded Spotify players.  

The project uses the [Spotify Web API](https://developer.spotify.com/documentation/web-api) to fetch real-time artist and track data.  

---

## 🚀 Project Objectives  
- **Artist exploration**: display relevant data such as popularity and follower count.  
- **Top tracks listing**: show the most popular songs with album cover, album name, and Spotify link.  
- **Modern UI**: leverage HTML + CSS inside Streamlit to create styled cards that resemble a real app experience.  
- **Embedded player**: allow users to listen to tracks via the official Spotify player directly in the app.  

---

## 🗂️ Project Structure  
```bash
📁 api-spotify/
│── 📄 app.py           # Main application code
│── 📄 requirements.txt # Project dependencies
│── 📄 .env.example     # Example environment variables
│── 📄 README.md        # Project documentation
```

## 🛠️ How to Use

To run this project locally, follow the steps below:

### Clone the repository:
```bash
git clone https://github.com/mathreiss04/api-spotify.git your-repository
cd your-repository
```

### Create a virtual environment (optional but recommended):
```bash
python -m venv venv
```

### Activate the virtual environment:
**Windows (Git Bash):**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Install dependencies:
```bash
pip install -r requirements.txt
```

### Set up your spotify credentials:
- **Create an app at [Spotify for Developers](https://developer.spotify.com)**
- **Copy your Client ID and Client Secret**
- **Create a .env file in the project root with the following content:**
```env
SPOTIFY_CLIENT_ID=your_client_id_here
SPOTIFY_CLIENT_SECRET=your_client_secret_here
```

### Run the Streamlit app:
```bash
streamlit run app.py
```

### Access the app:
Open your browser and go to the address shown in the terminal (usually `http://localhost:8501`).

## 🛠️ Technologies Used

- **Streamlit**: To create interactive web interfaces.
- **Python**: Primary programming language.

## 📊 Features and Visualizations

- Display of artist information including name, popularity, followers, and image.
- Styled cards for each top track containing:
    - Album cover
    - Track name (with a clickable link to Spotify)
    - Popularity score

## 🔍 Future Improvements
- Add support for album search in addition to artists
- Include music/artist recommendations
- Implement a search history section

## 📝 License
This project is licensed under the MIT License. See the LICENSE file for details.

## 🤝 Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request.
