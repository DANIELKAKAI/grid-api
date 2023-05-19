# Django Grid API

This Django API provides endpoints for calculating closest points on a grid.

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/DANIELKAKAI/grid-api.git
   cd grid-api
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   
3. Install the dependencies:
   ```bash
      pip install -r requirements.txt
   ```

4. Apply the database migrations:
   ```bash
      python manage.py migrate
   ```

5. Run the development server:
   ```bash
      python manage.py runserver
   ```
   
6. Run tests:
   ```bash
      python manage.py test
   ```

## API Endpoints
### POST /calculate-closest-points/
Calculates the closest points on the grid.

Example request:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"points": "2,2;-1,30;20,11;4,5"}' http://localhost:8000/calculate-closest-points/
```

Example response:
```json
{
  "closest_points": "2,2;4,5"
}

```