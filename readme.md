Dokumentation: Eine Richtlinie 

Projekttitel: Mensch ärgere dich nicht als Konsolenspiel
Teilnehmer: Mike Fröse

Aufbau des Projekts
Das Projekt wurde nach dem „Clean Code“ und „PEP 20“ geschrieben und hält alles so simpel wie nur möglich.

madn_screen.py
Die Datei importiert „time“, das die „sleep“ methode aufgerufen werden kann, die wird benötigt um bestimmte Texte, gewürfelte Zahlen und Computer Züge in einer nachvollziehbaren Geschwindigkeit  zu zeigen. Es wird auch „os“ importiert, um Zugriff auf die „clear“ Funktion der Konsole zu erhalten. Der Import der „sys“ wird benötigt, um den gesamten Speicher auf der Konsole auszugeben, bevor ein „sleep“ aufgerufen wird.
In der „madn_screen.py“ finden Sie alle nötigen Funktionen, die benötigt werden, um das Spiel in der Konsole auszugeben. Zuerst reinigt die Funktion „clear“ die Konsole und ermöglicht es, der „write_pos“ auf dem Konsolenfenster ausgaben gezielt zu überschreiben. Das hat den Vorteil, dass jede zukünftige Funktion nur ihren Teil im Konsolenfenster überschreibt und nicht alles aktualisiert werden muss. Für jeden Bereich, der ausgegeben werden soll, wurde eine eigene Funktion erstellt und erleichtert die zukünftigen Ausgaben der Spiellogik. Es gibt eine Funktion, die Rechtecke in unterschiedlichen Farben zeichnet, eine weitere die Würfel und so weiter.
Für das Spielbrett wurde eine Funktion erstellt, die den Hintergrund malt und eine weitere, die alle Figur-Felder aktualisiert. 

madn_func.py
Die Datei importiert „random“ um eine Zufallszahl für den Würfel zu generieren und importiert „madn_screen.py“ für die direkten Ausgaben in der Konsole und verarbeitet die einzelnen Spielprozesse und Benutzereingaben. Die Benutzereingaben wurden so konzipiert, dass bei einer Falscheingabe der Nutzer darauf hingewiesen wird und die Eingabe wiederholen kann. Für jede Figur des aktiven Spielers wird ermittelt, welche möglichen Züge gültig sind und nur diese werden dem Spieler zur Verfügung gestellt. Es wurde ein Punktesystem entwickelt, an dem sich der Computerspieler orientiert, auf diese Weise nimmt der Computer die bestmögliche Wahl, um das Spiel zu gewinnen.

run_game.py
Die run_game importiert „madn_func.py“, um auf die Spiellogik zuzugreifen und beinhaltet die Game-Klasse. In der wiederum die Spieler und Spielfiguren hinterlegt sind. Die Klasse beinhaltet 3 Methoden:
    •  „draw_game“ zum Initialen Zeichen des Spieles.
    •  „setup_players“ zum Anmelden der Spieler.
    •  „start_game“ zum Initialisieren des Spiels.
Die „start_game“ lädt die ersten beiden Methoden initial und ermöglicht es mit nur einem Aufruf das Spiel zu starten. Es durchläuft eine Spiele-Reihenfolge in einer Schleife, die nach jedem Durchlauf den nächsten Spieler aufruft. Diese Schleife wird unterbrochen, wenn es einen Gewinner gibt. Danach wird die Game-Klasse neu aufgerufen, um ein neues Spiel zu starten.


Die herausforderndste Funktion dieses Projektes war die Berechnung über ein Punktesystem, welche Figur durch den Computer gehen soll.



Funfacts

2  * print  
2  * tuple  
2  * elif  
3  * try  
5  * not  
7  * while  
15 * dict  
15 * list  
16 * Invested Time  
17 * else  
28 * for  
32 * def  
38 * return  
59 * if  
835 * Lines of code  
28702 * chars of code  
64800 * Invested secounds  
2,7339465 chars per secound  

Happy gaming!



