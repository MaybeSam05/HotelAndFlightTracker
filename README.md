Travel Booker - README

Overview
Travel Booker is a Python-based command-line tool that allows users to search for and book flights and hotels for their travel needs. The tool utilizes the SerpAPI to fetch flight and hotel data based on user preferences, including destination, departure dates, number of travelers, and accommodation preferences. This application provides a step-by-step booking process, allowing users to make informed decisions about their travel options.

The program uses the requests library to interact with the SerpAPI for real-time data and the tabulate library to display travel destination options in a neatly formatted table.

Features:

- Destination Selection: Users can choose from a predefined list of 15 travel destinations.
- Flight Booking: The tool fetches and presents multiple flight options based on the user’s preferences, including departure and return dates, airport codes, and cabin class.
- Hotel Booking: Users can search for hotel accommodations in their selected destination, filter options based on price and rating, and pick from several hotel options.
- Customizable Options: The application allows users to define their travel party (number of adults, children, and infants), the class of flight, and other details like check-in and check-out dates for hotels.

Requirements:
The following Python packages are required to run the application:

- requests
- tabulate
- airportsdata

How It Works:

- Welcome Screen: The program starts with a welcome message and displays a list of travel destinations using tabulate.
- Destination Selection: The user is prompted to select a destination from the list (1-15).
- Airport and Flight Details: The user provides the IATA code of their home airport, along with departure and return dates. The program then fetches available flight options using the SerpAPI and displays the best options.
- Hotel Search: After selecting a flight, the user enters their preferences for hotels, including check-out dates, minimum and maximum prices, and sorting options (e.g., by price, rating, or reviews). The SerpAPI fetches relevant hotel options, which are displayed for selection.
- Final Confirmation: After making selections, the program summarizes the chosen flight and hotel details and prints them for confirmation.

Example Output:

Hello and Welcome to Travel Booker!

╔════╤═══════════════════╤═════════════════╗
║ No │ Destination │ Country ║
╟────┼───────────────────┼─────────────────╢
║ 1 │ New York │ USA ║
║ 2 │ London │ UK ║
║ 3 │ Paris │ France ║
...
╚════╧═══════════════════╧═════════════════╝

Where would you like to travel to? (Pick a number 1-15)
You've selected **London, UK**

Please enter the IATA code of your home airport:
You've selected **JFK - John F. Kennedy International Airport** as your starting airport.
...

API Integration:

- The tool utilizes the SerpAPI to fetch live flight and hotel data, ensuring that users receive up-to-date travel options. API keys must be configured within the dest.py file.

Customization:

- The tool is designed to be easily extended with additional functionality, such as adding more travel destinations, enhancing flight or hotel search criteria, or improving user interactions through a GUI interface.
