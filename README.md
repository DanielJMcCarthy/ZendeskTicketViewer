## Zendesk Ticket Viewer Installation and usage instructions

#### Zendesk Intern Coding Challenge 2021. Daniel J McCarthy.

<br />

**Note:** Test cases are commented out as the build would fail when uploading using Git Hooks without the secrets file.   
<br />
After completing installation; ensure the response requests tickets from your own subdomain.  
This can be changed in the views.py file in **_both_** the homepage function and ticket function.
<br />
A secrets file must then be added with your email and password used to view your own tickets - seperated by a newline.
<br />
<br />
*If needs be, please do not hesitate to contact me and we can work something out! Thank you!*

<br />

### Using Docker

docker build .  
docker-compose up -d --build  
docker-compose down  

<br />

### In Terminal

python3 -m venv venv  
source venv/bin/active  
pip install -r requirements.txt  
python manage.py runserver  
