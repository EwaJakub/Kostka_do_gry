# Kostka_do_gry

Warsztat_1/Zadanie_5

W grach planszowych i papierowych RPG używa się wielu rodzajów kostek do gry, nie tylko tych dobrze znanych, 
sześciennych. Jedną z popularniejszych kości jest np. kostka dziesięciościenna, a nawet stuścienna! 
Ponieważ w grach kośćmi rzuca się często, pisanie za każdym razem np. "rzuć dwiema kostkami dziesięciościennymi, 
a do wyniku dodaj 20" byłoby nudne, trudne i marnowałoby ogromne ilości papieru. 
W takich sytuacjach używa się kodu "rzuć 2D10+20".

Kod takiej kostki wygląda następująco:
`xDy+z`

gdzie:
* `y`– rodzaj kostek, których należy użyć (np. D6, D10), 
* `x` – liczba rzutów kośćmi; jeśli rzucamy raz, ten parametr jest pomijalny, 
* `z` – liczba, którą należy dodać (lub odjąć) do wyniku rzutów (opcjonalnie).

Przykłady:
* `2D10+10`: 2 rzuty D10, do wyniku dodaj 10, 
* `D6`: zwykły rzut kostką sześcienną, 
* `2D3`: rzut dwiema kostkami trójściennymi, 
* `D12-1`: rzut kością D12, od wyniku odejmij 1.

Napisz funkcję, która:
* przyjmie w parametrze taki kod w postaci łańcucha znaków, 
* rozpozna wszystkie dane wejściowe:
  * rodzaj kostki, 
  * liczbę rzutów, 
  * modyfikator,
* jeśli podany ciąg znaków jest niepoprawny, zwróci odpowiedni komunikat, 
* wykona symulację rzutów i zwróci wynik.

Typy kostek występujące w grach: `D3, D4, D6, D8, D10, D12, D20, D100`.