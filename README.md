# SaccoZote (WORK IN PROGRESS)

SaccoZote is an API designed to provide a comprehensive list of Saccos in Kenya based on region. It's built with Flask and utilizes Africa’s Talking USSD API and Postgres for efficient data management.

## Features

- **Sacco Listing**: Provides a detailed list of Saccos in Kenya, categorized by region.
- **Region-Based Search**: Users can easily search for Saccos based on their geographical location.
- **Integration with USSD API**: Seamless integration with Africa’s Talking USSD API for enhanced user experience.
- **Secure Data Management**: Utilizes Postgres for robust and secure data storage and retrieval.

## Technologies Used

- Flask: Backend framework for building the API.
- Africa’s Talking USSD API: Integration for providing Sacco information via USSD.
- Postgres: Database management system for storing Sacco data.

## Usage

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Configure environment variables, if necessary.
4. Run the application using `python app.py`.
5. Access the API endpoints as per the documentation.

## API Endpoints

- `/saccos`: Retrieves a list of all Saccos.
- `/saccos/{region}`: Retrieves Saccos based on the specified region.

## Contributing

Contributions are welcome! Fork the repository and submit a pull request for enhancements or bug fixes.

## License

This project is licensed under the MIT License.
