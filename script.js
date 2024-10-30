async function fetchAndUpdateRooms() {
    // Retrieve selected day and time interval from dropdowns
    const day = document.getElementById('day').value;
    const timeInterval = document.getElementById('slot').value;

    // Check if both fields are selected
    if (day === 'default' || timeInterval === 'default') {
        alert('Please select both day and time interval.');
        return;
    }

    try {
        // Call the API endpoint with the selected parameters
        const response = await fetch(`/api/rooms/unoccupied?day=${day}&time_interval=${timeInterval}`);
        
        // Parse the response JSON
        const data = await response.json();
        
        // Check for errors in the response
        if (!response.ok) {
            console.error('Error:', data.error);
            alert(`Error: ${data.error}`);
            return;
        }

        // Iterate over each block and floor in the response to update the table cells
        Object.keys(data).forEach(block => {
            Object.keys(data[block]).forEach(floor => {
                // Find the table cell based on block and floor
                const cell = document.querySelector(`#room-table td[data-block="${block}"][data-floor="${floor}"]`);

                // Update the cell's content with room numbers or display '-' if none are unoccupied
                if (cell) {
                    const rooms = data[block][floor];
                    cell.textContent = rooms.length ? rooms.join(', ') : '-';
                }
            });
        });
    } catch (error) {
        console.error('Failed to fetch unoccupied rooms:', error);
        alert('An error occurred while fetching room data. Please try again later.');
    }
}
