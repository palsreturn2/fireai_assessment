# Fireai Assessment

This is the django app for the assignment which was shared to me. This repo also includes Summarization.ipynb which has the model training code. 

Installation instructions for the django app.

1) Clone the git repo.

2) Download the model file https://drive.google.com/file/d/1FD3FJ6_DepuImIKpR0w_nR4R2Yq7ikNz/view?usp=drive_link

3) Unzip the model tar file into the folder ./summarize/. 

4) Run pip install -r requirements.txt

5) Run the server using python manage.py runserver.


Instructions to query the server (Say localhost) in Windows Powershell

# Request
### Define the headers
$headers = @{
    "Content-Type" = "application/x-www-form-urlencoded"
}

### Define the body (data to send)
$body = @{
    "prompt" = "The full cost of damage in Newton Stewart, one of the areas worst affected, is still being assessed.\nRepair work is ongoing in Hawick and many roads in Peeblesshire remain badly affected by standing water.\nTrains on the west coast mainline face disruption due to damage at the Lamington Viaduct.\nMany businesses and householders were affected by flooding in Newton Stewart after the River Cree overflowed into the town.\nFirst Minister Nicola Sturgeon visited the area to inspect the damage."
}

### Make the POST request
Invoke-WebRequest -Uri "http://127.0.0.1:8000/summarise/" -Method POST -Headers $headers -Body $body

# Response

StatusCode        : 200
StatusDescription : OK
Content           : The full cost of damage in Newton Stewart, one of the areas worst affected, is still being assessed.nRepair work is ongoing in Hawick and many
                    roads in Peeblesshire remain badly affected by flooding.
RawContent        : HTTP/1.1 200 OK
                    X-Frame-Options: DENY
                    X-Content-Type-Options: nosniff
                    Referrer-Policy: same-origin
                    Cross-Origin-Opener-Policy: same-origin
                    Content-Length: 199
                    Content-Type: text/html; charset=ut...
Forms             : {}
Headers           : {[X-Frame-Options, DENY], [X-Content-Type-Options, nosniff], [Referrer-Policy, same-origin], [Cross-Origin-Opener-Policy, same-origin]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 199
