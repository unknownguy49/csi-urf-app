# Unoccupied Room Finder

Welcome to the Unoccupied Room Finder App! This app provides real-time data on unoccupied rooms across different blocks and floors, enabling efficient room management based on specified time slots.

## Features

- **Retrieve Unoccupied Rooms**: Get a list of available rooms for a specific day and time interval.
- **Custom Configuration**: Easily configure time slots and room data.
- **Scalable & Lightweight**: Built with Flask, making it suitable for a range of hosting options.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running Locally](#running-locally)
  - [API Endpoints](#api-endpoints)
- [Configuration](#configuration)

---

## Project Overview

This project provides an API for managing room availability based on a configurable timetable. The main feature is an endpoint that returns a list of unoccupied rooms for a specified day and time interval, facilitating efficient room scheduling.

---

## Getting Started

### Prerequisites

- **Python 3.9+**
- **Flask**: The micro web framework for Python

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt

3. **Set up required files**:
   
   - `time_slot_config.json`: Defines day and time intervals.
   - `occupied_rooms_data.json`: Details rooms currently in use.
   - `all_rooms_list.json`: Contains a complete list of all rooms.

### Usage

#### Running Locally

Run the Flask app in your local environment:

```bash
python app.py
```
Access the app at [http://127.0.0.1:5000](http://127.0.0.1:5000).

### API Endpoints

#### Retrieve Unoccupied Rooms

- **Endpoint**: `/api/rooms/unoccupied`
- **Method**: GET

**Parameters**:
- `day` (required): Specify the day (e.g., "Monday")
- `time_interval` (required): Specify the time interval (e.g., "10:00-11:00")

**Example Request**:

```http
GET /api/rooms/unoccupied?day=Monday&time_interval=10:00-11:00
```

### Configuration

The app configuration requires a few JSON files:

- `time_slot_config.json`: Defines time slots for each day.
- `occupied_rooms_data.json`: Details rooms that are occupied for specified slots.
- `all_rooms_list.json`: Contains a list of all rooms available for scheduling.

Happy coding!