:: Batch Script
:: requires mamp, duh
start C:\MAMP\MAMP.exe

echo wait for mamp to start
timeout 10
echo open myphp
start "C:\Programme\Mozilla Firefox\firefox.exe" http://localhost/MAMP/phpmyadmin.php