import requests

class RentalBot:
    API_URL = "http://localhost:8000"  # Change if you deploy this API elsewhere

    def respond(self, query: str, tenant_id: int):
        # Check if the user is asking about rent due date
        if "rent due" in query.lower():
            # Make a GET request to the FastAPI endpoint
            response = requests.get(f"{self.API_URL}/rent-due/{tenant_id}")
            data = response.json()
            if "rent_due_date" in data:
                return f"Your rent is due on {data['rent_due_date']}."
            return "I couldn't find your rent due date."

        # Add responses for other queries, like repair requests, etc.
        elif "repair" in query.lower():
            return "For repairs, please contact maintenance at support@rentalservice.com."

        # Default response
        return "I can assist with rent and maintenance inquiries!"
