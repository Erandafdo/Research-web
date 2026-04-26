import os

file_path = 'static/js/main.941d00c7.js'
with open(file_path, 'r') as f:
    content = f.read()

replacements = {
    "PlanetPulse": "ElephantPulse",
    "Planet Pulse": "Elephant Pulse",
    "PlanetPulse An Application For Community Collaboration In Climate Resilience And Disaster Preparedness": "ElephantPulse An Application For Intelligent Elephant Care & Visitor Insight system",
    "In an ever-changing world, where the impacts of climate change and natural disasters are becoming increasingly prevalent, it\\'s crucial that communities come together to build resilience and preparedness. That\\'s where PlanetPulse comes in.PlanetPulse is not just another app; it\\'s a powerful tool designed to foster collaboration, share vital information, and empower communities to face the challenges of our time head-on. With the collective strength of individuals, local organizations, and governments, we can take a proactive approach towards building a more resilient future.": "ElephantPulse is an AI-driven platform designed to improve elephant welfare and visitor education. This project consolidates multiple care functionalities into one unified architecture. It features Health Prediction, Stress Detection, and Visitor Analytics to ensure the well-being of elephants and a great experience for visitors.",
    "Motivates users to actively engage in tree planting and contribute to a greener planet. It rewards them with points that can be donated to worthy causes. ": "Monitors elephant vitals to predict health trends using AI and analyzes behavior to detect stress levels. "
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open(file_path, 'w') as f:
    f.write(content)

print("Replacements done in js.")
