
# Flight Deal Finder

A program that searches for flight deals based on data stored in a Google Sheet and sends notifications via SMS using the Twilio API.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Important Parts of the Code](#important-parts-of-the-code)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/your-username/Flight-deal-finder.git
   ```

2. Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

3. Set up a Google Sheet with the following columns:

   - `city` (string): the name of the city to search for flight deals
   - `iataCode` (string): the [IATA code](https://www.iata.org/en/publications/directories/code-search/) for the city
   - `lowestPrice` (integer): the maximum price you are willing to pay for a flight

   Share the sheet with an account that has [Google Sheets API access](https://developers.google.com/sheets/api/guides/authorizing).

4. Set up a [Twilio account](https://www.twilio.com/try-twilio) and obtain your account SID, auth token, and Twilio phone number.

5. Set up a [Kiwi.com account](https://tequila.kiwi.com/portal/signin) and obtain your API key.

6. Create a `.env` file in the root directory of the project with the following variables:

   ```
   SHEETY_ENDPOINT=your Google Sheets API endpoint
   SHEETY_TOKEN=your Google Sheets API token
   TWILIO_ACCOUNT_SID=your Twilio account SID
   TWILIO_AUTH_TOKEN=your Twilio auth token
   TWILIO_PHONE_NUMBER=your Twilio phone number
   KIWI_API_KEY=your Kiwi.com API key
   ```

## Usage

Run the program with the following command:

```
python main.py
```

The program will first check if the `iataCode` column is populated in the Google Sheet. If not, it will use the Kiwi.com API to search for the IATA code of each city and populate the sheet accordingly.

Then, the program will search for flight deals based on the data in the sheet using the Kiwi.com API. If a flight deal is found that is cheaper than the maximum price specified in the sheet, the program will send an SMS notification via the Twilio API.

## File Structure

```
flight-deal-finder/
├── data/
│   ├── cities.csv
│   ├── sheety_endpoint.json
│   └── sheety_token.json
├── helpers/
│   ├── flight_search.py
│   ├── google_sheet.py
│   ├── notification_manager.py
│   └── sheety.py
├── main.py
├── README.md
└── requirements.txt
```

- `data/`: Contains data files needed for the program to run.
    - `cities.csv`: A CSV file containing a list of cities to search for flight deals.
    - `sheety_endpoint.json`: A JSON file containing the endpoint for the Google Sheets API.
    - `sheety_token.json`: A JSON file containing the authorization token for the Google Sheets API.
- `helpers/`: Contains helper classes for the program.
please also include  the important coding parts
## Contributing
Contributions to this project are welcome. To contribute, follow these steps:
1. Fork this repository
2. Create a new branch (`git checkout -b feature/new-feature`)
3. Make and commit your changes (`git commit -am "Add new feature"`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a new Pull Request
## Find me on
[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-Profile-informational?style=flat&logo=linkedin&logoColor=white&color=0D76A8)](https://www.linkedin.com/in/gokul-bakkiyarasu-531535251)
