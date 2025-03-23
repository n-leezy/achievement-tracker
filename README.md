# Achievement Tracker
The Achievement Tracker is a web and mobile application that enables gamers to track, analyze, and optimize their achievement progress across video game platforms. It provides real-time progress tracking, personalized recommendations, interactive data visualizations, and social comparison features. Initially focused on Steam integration, the platform is designed for future expansion to PlayStation and Xbox.

## Development Setup with Docker

### Prerequisites
- Docker and Docker Compose installed
- Git (for version control)

### Initial Setup
1. Clone the repository
```bash
git clone https://github.com/n-leezy/achievement-tracker.git
cd achievement-tracker
```

2. Create a .env file from the example
```bash
cp .env.example .env
```

3. Edit the .env file to add your API keys and set a secure database password

### Running the Application
```bash
# Build and start all services
docker compose up --build

# Run in background
docker compose up -d

# View logs
docker compose logs -f

# Stop services
docker compose down
```
### Accessing the Application
- Frontend: http://localhost:3000
- Backend: http://localhost:8000

### Working Across Different Machines
1. Commit your changes before switching machines
```bash
git add .
git commit -m "your commit message"
git push
```

2. On your other machine
```bash
git pull
# create .env file if not exists
docker compose up
```

## Project Structure
- `frontend`: React web application
- `backend`: Python FastAPI backend
- `docker-compose.yml`: Docker services configuration

## Notes

