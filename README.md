# local
Set up a local ***test*** enviroment for your website the lazy way. 
Designed for admins to get newbies up and running with wordpress with minimal effort.

## Preparation
- You need to put the 'www.zip' in the same folder as the README.md
- Have your database (its usually a '.sql' or '.sql.zip' file) ready


<details> <summary>Deutsch</summary> 
  
  - Lege dein 'www.zip' archiv in den gleichen ordner wo ua. README.md, setup.bat liegen
  - Halte deine datenbank bereit (typischerweise eine '.sql' oder '.sql.zip' datei)
  
</details>


### Note for admins 
  - strip all irrelevant data (logins, passwords) before giving out the database!
  - adjust the wordpress files to the database login defaults (usually: usr='root' and pwd='root')
  - prepackage this repo with all needed files.

---------------
## Installation
1. Download / clone the whole repo
2. run the appropriate script for your system (windows -> setup.bat; linux, macOS -> setup.sh)
3. Lt it run and dont abort it
4. If it asks you for input (usually with [Y/n]), press enter to continue with the defaults or enter y / n before to select the desired action

<details> <summary>Deutsch</summary>  

1. gesamten Ordner als zip herunterladen (Button "Alle dateien herunterladen") und in einen beliebigen ordner entpacken   
  
2. setup batch skript ausführen (doppelklicken)   
  
3. Laufen lassen, nicht abbrechen.   
  
4. Bei fragen nach user input [Y/n] 'enter' drücken um die groß geschriebene option auszuwählen, sonst einfach 'yes', 'no', 'y' bzw 'n' für die entsprechende option drücken  
   
</details>


## Database
1. go to 'http://localhost/MAMP/myphpadmin' and create the database named wordpress. Import your prepared database into it.
2. If you get errors, note them and ignore them. If it works its usually fine for simple testing.
3. go to http://localhost to view your site. 

<details> <summary>Deutsch</summary> 

1. Bei myphp (url: http://localhost/MAMP/myphpadmin ) eine datenbank "wordpress" anlegen, draufklicken, dann auf "importieren" klicken. wordpress.sql.zip auswählen und hochladen   
  
2. fehler notieren, dann ignorieren   
  
3. gehe auf http://localhost um deine seite zu sehen.
</details>


---------------
## Hilfe
Restarting your system after big changes a good idea and solves a lot of problems. So, do it.
<br>

<details> <summary>Ive got problems</summary> 
  
  Thats unfortunate, but acceptance is always the first step. Moving on then:

  <br>

  ### P: The installation of program __ doesnt continue
  S: Wait for it. In case of windows, try to press enter. Maybe chocolatery needed confirmation.
  
  
  
  ### P: 'www.zip' is missing
  S: You need to provide contents for your www or htdocs folder. The zip should contain the files directly, not inside www folder.
  
  
  
  ### P: MAMP throws some errors
  S: But does the webserver work anyway? If no, restart your system. If its still not working, run the script again.
  
  
  
  ### P: localhost redirect to the live wordpress page
  S: Change the site adress locally and then CLEAR THE BROWSER CACHE.
  
</details>

<br>

Ein Systemneustart is empholen und löst viele Probleme, also mach das bitte.
<details> <summary>Ich habe probleme</summary> 
  
  Das ist schade, aber akzeptanz ist der erste schritt hin zur lösung.
  
  <br>
  
  ### P: Die Installation von Programm _ geht nicht weiter
  L: Braucht ggf mal eine Bestätigung, einmal Enter drücken. Kann aber auch einfach mal lange dauern.



  ### P: 'www.zip' fehlt
  L: schau nach ob du die zipdatei mit heruntergeladen hast; liegt sie im selben ordner wie 'setup.bat' ?
  Wenn du gar keine 'www.zip' datei hast solltest du deinen admin danach fragen.

  

  ### P: MAMP zeigt mir komische fehler an
  L: System neustarten. Wenn immer noch probleme auftreten: skript nochmal laufen lassen.

  

  ### P: Localhost leitet auf die originale website weiter
  L: Browsercache leeren.

  

  ### P: Wie geht xy, Z geht nicht (!) und ähnliches
  L: Googeln, Dokumentation lesen. #giyf \
  Das meiste löst sich so fix. Wenn nicht, einfach Fragen :)
</details>
