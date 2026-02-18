import os
from jinja2 import Template
from datetime import datetime
import pytz

def get_flight_data():
    # Simulasi data akurat untuk DJJ (Bisa dikembangkan ke API scraping)
    # Di sini kita buat data dummy yang terlihat profesional
    return [
        {"flight_no": "GA 651", "airline": "Garuda Indonesia", "destination": "Jakarta (CGK)", "time": "08:15", "status": "DEPARTED"},
        {"flight_no": "ID 6181", "airline": "Batik Air", "destination": "Makassar (UPG)", "time": "09:40", "status": "DEPARTED"},
        {"flight_no": "JT 795", "airline": "Lion Air", "destination": "Jayapura (DJJ) - Merauke", "time": "11:00", "status": "SCHEDULED"},
        {"flight_no": "IL 271", "airline": "Trigana Air", "destination": "Wamena (WMX)", "time": "12:30", "status": "SCHEDULED"},
        {"flight_no": "IW 1632", "airline": "Wings Air", "destination": "Dekai (DEX)", "time": "13:15", "status": "SCHEDULED"},
        {"flight_no": "GA 653", "airline": "Garuda Indonesia", "destination": "Jayapura (DJJ) - Timika", "time": "14:45", "status": "SCHEDULED"}
    ]

def main():
    # Pastikan folder output ada
    flights = get_flight_data()
    
    # Set timezone ke WIT (Papua)
    wit = pytz.timezone('Asia/Jayapura')
    now = datetime.now(wit).strftime("%d %b %Y, %H:%M") + " WIT"

    # Load template
    with open("templates/index_template.html", "r") as f:
        template_content = f.read()

    template = Template(template_content)
    rendered_html = template.render(flights=flights, last_update=now)

    # Simpan sebagai index.html
    with open("index.html", "w") as f:
        f.write(rendered_html)
    
    print("Website updated successfully!")

if __name__ == "__main__":
    main()
