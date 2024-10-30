from flask import Flask, render_template_string, send_from_directory, request, jsonify, abort
import os
import json
import logging

app = Flask(__name__)

with open("index.html", "r", encoding="utf-8") as f:
    index_html = f.read()

@app.route("/")
def home():
    # Render the HTML content directly
    return render_template_string(index_html)

@app.route("/<filename>")
def static_files(filename):
    # Serve static files like CSS and JS
    return send_from_directory(os.getcwd(), filename)


# Load configuration at startup to avoid reloading on each request
try:
    with open('time_slot_config.json', 'r') as file:
        tome_slot_config = json.load(file)
except Exception as e:
    app.logger.error("Error loading 'tome_slot_config.json': %s", e)
    tome_slot_config = {}

# Configure logging for production
logging.basicConfig(level=logging.INFO)

def get_slots(day, time_interval):
    """Retrieve slots for a given day and time interval."""
    if day in tome_slot_config:
        day_schedule = tome_slot_config[day]
        if time_interval in day_schedule:
            return day_schedule[time_interval]
        elif 'LAB' in day_schedule and time_interval in day_schedule['LAB']:
            return day_schedule['LAB'][time_interval]
    return None

def find_rooms_by_slot(json_file, search_slot):
    """Find rooms occupied during a specific slot."""
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
    except Exception as e:
        app.logger.error("Error loading '%s': %s", json_file, e)
        return {}

    rooms_found = {}
    for slot, block_data in data.items():
        if search_slot == slot or search_slot in slot.split('+'):
            for block, rooms in block_data.items():
                if block not in rooms_found:
                    rooms_found[block] = set()
                rooms_found[block].update(rooms)
    return rooms_found

def load_all_rooms(filename):
    """Load a list of all rooms from the provided file."""
    try:
        with open(filename, 'r') as file:
            all_rooms = json.load(file)
        return all_rooms
    except Exception as e:
        app.logger.error("Error loading '%s': %s", filename, e)
        return {}

def find_unoccupied_rooms(all_rooms, occupied_rooms):
    """Calculate unoccupied rooms based on all rooms and occupied rooms."""
    unoccupied_rooms = {}

    for block, floors in all_rooms.items():
        unoccupied_rooms[block] = {}
        for floor, data in floors.items():
            floor_rooms = set(data['rooms'])
            occupied_floor_rooms = occupied_rooms.get(block, set())
            unoccupied = floor_rooms - occupied_floor_rooms
            if unoccupied:
                unoccupied_rooms[block][floor] = list(unoccupied)

        # Filter out empty floors
        unoccupied_rooms[block] = {k: v for k, v in unoccupied_rooms[block].items() if v}

    return {k: v for k, v in unoccupied_rooms.items() if v}

@app.route('/api/rooms/unoccupied', methods=['GET'])
def get_unoccupied_rooms():
    """API endpoint to get unoccupied rooms for a specific day and time interval."""
    day = request.args.get('day')
    time_interval = request.args.get('time_interval')
    
    if not day or not time_interval:
        return jsonify({"error": "Parameters 'day' and 'time_interval' are required."}), 400

    slot = get_slots(day, time_interval)
    if not slot:
        app.logger.info("No slot found for day: %s, time interval: %s", day, time_interval)
        return jsonify({"error": f"No slot found for day: {day}, time interval: {time_interval}"}), 404

    # Find occupied rooms based on the slot
    occupied_rooms = find_rooms_by_slot("occupied_rooms_data.json", slot[0])
    all_rooms = load_all_rooms("all_rooms_list.json")

    # Check for empty room list to handle errors
    if not all_rooms:
        app.logger.error("All rooms list could not be loaded.")
        return jsonify({"error": "Internal error loading room data"}), 500

    # Calculate unoccupied rooms
    unoccupied_rooms = find_unoccupied_rooms(all_rooms, occupied_rooms)
    return jsonify(unoccupied_rooms), 200

# For production, set debug=False and enable logging to file if needed
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
