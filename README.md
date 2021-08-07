# Design-patterns


## Overview

Wzorce projektowe to dobre i sprawdzone rozwiązania, które należy dostosować do swojego projektu. Pozwalają na uniknięcie tworzenia koła od nowa, są odpowiedzią na zmiany, które czekają na nas w projekcie. Ogólnie mówiąc wzorce projektowe są konwencją, ideą. Ważne jest to, że wzorce projektowe nie rozwiązują wszystkich problemów programistycznych. 

Wyodrębniamy trzy główne typy wzorców projektowych:
- <strong> Kreacyjne </strong> (Fabryka, Budowniczy, Singleton, Prototyp, Pula Obiektów) - Służą do organizowania procesu tworzenia obiektów
- <strong> Struktoralne </strong>  (Adapter, Proxy, Dekorator, Kompozycja, Fasada, Mostek) - Służą do łączenia różnych obiektów w celu uzyskania rozbudowanej funkcjonalności
- <strong> Czynnościowe / Operacyjne </strong> (Strategia, Łańcuch zobowiązań, Obserwator, Odwiedzający) - Służą do komunikacji między obiektami, do przepływu pracy

Poza tym wyróżniamy także:
- <strong> Architektoniczne </strong> (MVC, MVT, MVVM)
- <strong> Współbieżne / Wielowątkowe </strong>

## Singleton 

Wzorzec projektowy zapewniający istnienie co najwyżej jednej instancji danej klasy. Instancja ta musi być dostępna zewsząd. Sytuacje w których warto użyć wzorca Singleton to min.: Logger, Dziennik, Bufor, Obiekt ustawień, Obiekt łączenia z bazą danych. 
