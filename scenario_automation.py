import os

# Start Docker containers
os.system('docker-compose up -d')

# Run attack scenario
os.system('python basic_attack_scenario.py')

# Teardown environment
os.system('docker-compose down')
