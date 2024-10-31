# Unoccupied Room Finder

Welcome to the Unoccupied Room Finder App! This app provides real-time data on unoccupied rooms across different blocks and floors, enabling efficient room management based on specified time slots.

---
## Table of Contents

- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running Locally](#running-locally)
  - [Running Live](#running-live)

---

## Project Overview

The Unoccupied Room Finder is a web application designed to assist students at VITAP University in locating available classrooms across three blocks (AB1, AB2, and CB). Users can easily select a day and time slot from a user-friendly dropdown interface. Upon selection, the application fetches real-time data to display unoccupied rooms, enhancing the campus experience by minimizing time spent searching for study spaces. The tool aims to foster a productive academic environment by providing quick access to available facilities.

---

## Getting Started

### Prerequisites
---
- **Python**
- **Flask**: The micro web framework for Python

### Installation
---
1. **Clone the repository**:

   ```bash
   git clone https://github.com/unknownguy49/csi-urf-app.git
   cd csi-urf-app
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```
---
## Usage
### Running Locally:
   Run the Flask app in your local environment:
   ```bash
   python app.py
   ```
   Access the app at [http://127.0.0.1:5000](http://127.0.0.1:5000).

### Running Live:
   Access the app at:
   [https://csi-project-urf.vercel.app/](https://csi-project-urf.vercel.app/)
