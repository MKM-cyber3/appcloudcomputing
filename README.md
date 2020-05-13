# Aplicație de tip tovarăș de călătorie  :earth_americas:

## Introducere
<br>Aplicația **MARINA APP** își propune să fie un așa-zis travel companion digital al celor care se află într-o călătorie la momentul accesării ei și nu numai. Aplicația **de căutare** a fost realizată în Python cu Flask și a utilizat **două API-uri**. În ceea ce privește cloud-ul, a fost publicată pe **două platforme**, pe **Heroku** (https://appcloudcomputingmarina.herokuapp.com/), dar și pe **Azure** (https://appmarina.azurewebsites.net/). De curiozitate, am publicat și pe platforma pythonanywhere (http://marinacloudcomputing.pythonanywhere.com/). Am utilizat biblioteca Python Requests pentru a apela API-ul și Flask pentru a afișa rezultatele căutării. Flask este un micro web framework scris în Python. 

## Descriere problemă
<br>Problema pe care această aplicație web o poate rezolva este faptul că cei care călătoresc au nevoia de a căuta cu ușurință starea vremii din prezent în orașul în care se află la acel moment, iar apoi pot căuta rapid video-uri pe YouTube cu referire la ceea ce pot vizita în locația respectivă. Este o aplicație foarte utilă spre exemplu pentru cei ce călătoresc în interes de serviciu și pot astfel accesa mai facil cele două informații necesare: starea vremii și idei de călătorie. Aplicația oferă top 9 rezultate din căutarea pe YouTube, lucru care este un time-saver pentru călători, întrucât nu mai este nevoie să "filtreze" ei înșiși informația. De asemenea, este afișată și durata fiecărui videoclip, utilizatorul putând alege și pe baza acestui criteriu ce videoclip să vizioneze. Astfel, **MARINA APP** devine o aplicație utilă în vederea accesării rapide a informațiilor necesare călătorilor. 

## Descriere API
În vederea realizării aplicației, am utilizat două API-uri, **YouTube Data API** de la Google și **Open Weather Map API** de la RapidAPI.

###### YouTube Data API 
https://developers.google.com/youtube/v3
<br>**YouTube Data API** permite utilizatorilor să includă funcții executate în mod normal pe site-ul YouTube în propriul site sau în propria aplicație. Există diferite tipuri de resurse care se pot regăsi folosind API-ul. API-ul suportă, de asemenea, metode pentru a insera, actualiza sau șterge multe dintre aceste resurse. O resursă reprezintă un tip de element care cuprinde o parte din experiența YouTube, cum ar fi un videoclip, o listă de redare sau un abonament. Pentru fiecare tip de resursă, există una sau mai multe reprezentări de date, iar resursele sunt reprezentate ca obiecte JSON. În cadrul ghidului de utilizare YouTube Data API se listează, de asemenea, una sau mai multe metode acceptate (LIST, POST, DELETE, etc.) pentru fiecare tip de resursă și se explică modul de utilizare a acestor metode în aplicație.

###### Open Weather Map API 
https://rapidapi.com/community/api/open-weather-map/details
https://openweathermap.org/api
<br>Cei de la RapidAPI oferă acest **Open Weather Map API**, prin care se pot accesa datele meteo curente pentru orice locație, inclusiv peste 200.000 de orașe, vremea actuală fiind actualizată frecvent pe baza modelelor globale și a datelor de la peste 40.000 de stații meteo. Datele sunt disponibile în format JSON, XML sau HTML, iar ca și pricing, acest API este disponibil atât pentru abonamente gratuite, cât și pentru plată, pentru cele gratuite existând un număr exact de request-uri pe care le poți face pentru accesarea vremii. Nu am ales să mă conectez la o bază de date pentru a implementa acest API, întrucât nu am utilizat metode de tip UPDATE, DELETE etc. 
  
## Flux de date
  
1. Exemple de request/response
    
    Ca și flux de date, prin metoda POST se trimite către server request-ul reprezentat de termenul căutat în bara de search, atât pentru API-ul de YouTube, cât și pentru cel de vreme. După accesarea API-urilor, response-ul va fi întors la aplicație prin metoda GET, sub formă de JSON. De asemenea, este importantă de menționat librăria Requests din Python. Spre **exemplu**, atunci căutăm cum este vremea în București, termenul *Bucharest* este transmis prin POST către server, iar apoi se primește răspunsul sub formă de JSON prin metoda GET.

2. Metode HTTP
    
    Metodele utilizate au fost GET și POST.
    <br>Metoda **POST** este utilizată pentru a trimite date către server, cu scopul de a căuta ceea ce utilizatorul își dorește și a aduce ulterior rezultatele. Metoda **GET** indică faptul că am încercat să obțin datele din resursa specificată, API-ul. Pentru a face solicitarea GET, am utilizat requests.get ().
    
    <br>Exemple:
    ```
    @main.route('/weather',methods=['GET','POST'])
    
    GET /static/album.css HTTP/1.1
    POST /youtube HTTP/1.1
    GET /weather HTTP/1.1
    POST /weather HTTP/1.1
    
3. Autentificare și autorizare servicii utilizate

    <br>La acest punct, voi detalia metoda doar pentru API-ul de YouTube, întrucât doar la acesta a fost necesar. Pentru a utiliza metodele HTTP de tip GET și POST, a fost necesară doar o cheie API pe care am inclus-o în fișierul .env din proiect, cheie care a trebuit ulterior inclusă separat la momentul deployment-ului, pe Heroku și Azure. 
    
    ```
    YOUTUBE_API_KEY=AIzaSyA-T2pMN9WOlA7z_eB7NfjmVMN447N_dX0
    
## Capturi ecran aplicație
      
![](images/homepage.JPG) 
![](images/weather1.JPG) 
![](images/weather2.JPG)
![](images/youtube1.JPG) 
![](images/youtube2.JPG) 
![](images/youtube3.JPG) 
      
## Referințe    
  - Seminarii Video Eduard Budacu
  - https://developers.google.com/youtube/v3/docs
  - https://rapidapi.com/community/api/open-weather-map/details
  - https://openweathermap.org/api
  - https://www.youtube.com/channel/UC-QDfvrRIDB6F0bIO4I4HkQ/videos
  - https://www.w3schools.com/
  - https://docs.microsoft.com/en-gb/
  - https://developers.google.com/apis-explorer
    
