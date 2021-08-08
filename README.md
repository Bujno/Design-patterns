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

Wzorzec projektowy zapewniający istnienie co najwyżej ustalonej z góry liczby instancji danej klasy. Instancja ta musi być dostępna zewsząd. Sytuacje w których warto użyć wzorca Singleton to min.: Logger, Dziennik, Bufor, Obiekt ustawień, Obiekt łączenia z bazą danych. 

Plusy:
- Łatowść implementacji
- Brak zmian po stronie projektu
- Stan singletonów jest globalny
- Leniwe tworzenie instancji 

Minusy:
- Komplikacje przy wielowątkowości
- Klasa singleton robi to musi ale dodatkowo też kontroluje swoje instancje
- Może być trudny w testowaniu, a właściwie debugowaniu 


## Abstract Factory

Najpierw powtórzmy sobie definicję <strong>klasy abstrakcyjnej</strong>. Jest to uogulnienie innych klas z której te będą dziedziczyć, czyli taka klasa bazowa. Z klasy abstrakcyjnej możemy jedynie dziedziczyć - nie możemy tworzyć z niej obiektów w sposób bezpośredni. 

<strong>WAŻNE!</strong> Fabryka abstrakcyjna może, ale wcale nie musi być klasą abstrakcyjną

<strong>Farbyka abstrakcyjna</strong> - wzorzec projektowy dostarczający mechanizm tworzenia instancji różnych klas należących do pewnej rodziny. Czyli:
- Posiadamy rodzinę niemal całkiem innych klas
- Każda klasa posiada zainicjalizowane te same metody
- Celem fabryki abstrakcyjnej będzie dostarczenie nam odpowiedniej klasy
My programniści, użytkownicy fabryki abstrakcyjnej, nie będziemy nawet wiedzieć jaka klasa została zwrócona - nie potrzebujemy tej wiedzy, o ile zostanie dobrana dobra klasa końcowa. Aby zrealizować wzorzec fabryki abstrakcyjnej należy wydzielić logikę wyboru klasy do osobnej klasy, której celem będzie jedynie zwrócenie odpowiedniego typu.