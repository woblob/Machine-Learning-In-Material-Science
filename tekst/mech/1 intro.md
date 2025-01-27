### Właściwości mechaniczne

Aby zrozumieć, jak materiały reagują na przyłożone siły, należy zacząć od **prawa Hooke'a**, które jest fundamentalne w badaniu właściwości mechanicznych ciał stałych. Prawo Hooke'a stwierdza, że ​​odkształcenie (deformacja) materiału jest wprost proporcjonalne do przyłożonego naprężenia (siła na jednostkę powierzchni) w granicach sprężystości tego materiału. Matematycznie, uproszczoną wersję prawa Hooke'a można to wyrazić jako:

$$
\sigma = E \cdot \epsilon
$$

gdzie:
- $\sigma$ to naprężenie [$Pa$],
- $E$ to moduł sprężystości (moduł Younga) [$Pa$],
- $\epsilon$ to odkształcenie sprężyste [$-$].

Pełną ogólną postać macierzową, które wiąże naprężenie i odkształcenie w ciałach stałych, można wyrazić za pomocą macierzy $6 \times 6$. Ta formuła uwzględnia złożoność materiałów anizotropowych, w których właściwości mechaniczne zmieniają się w zależności od kierunku.

### Uogólnione prawo Hooke'a w postaci macierzowej

W przypadku materiału liniowo sprężystego zależność między naprężeniem $\sigma$ a odkształceniem $\epsilon$ można przedstawić jako:

$$
\begin{bmatrix}
\sigma_1 \\
\sigma_2 \\
\sigma_3 \\
\tau_{23} \\
\tau_{13} \\
\tau_{12}
\end{bmatrix}
=
\begin{bmatrix}
C_{11} & C_{12} & C_{13} & C_{14} & C_{15} & C_{16} \\
C_{12} & C_{22} & C_{23} & C_{24} & C_{25} & C_{26} \\
C_{13} & C_{23} & C_{33} & C_{34} & C_{35} & C_{36} \\
C_{14} & C_{24} & C_{34} & C_{44} & C_{45} & C_{46} \\
C_{15} & C_{25} & C_{35} & C_{45} & C_{55} & C_{56} \\
C_{16} & C_{26} & C_{36} & C_{46} & C_{56} & C_{66}
\end{bmatrix}
\begin{bmatrix}
\epsilon_1 \\
\epsilon_2 \\
\epsilon_3 \\
\gamma_{23} \\
\gamma_{13} \\
\gamma_{12}
\end{bmatrix}
$$

gdzie $\sigma$ odpowiada wektorowi naprężeń, $E$ macierzy sztywności sprężystej a $\epsilon$ wektorowi odkształceń.

- **Wektor naprężeń**: Wektor naprężeń obejmuje naprężenia normalne ($\sigma_1, \sigma_2, \sigma_3$) i naprężenia ścinające ($\tau_{23}, \tau_{13}, \tau_{12}$).
- **Macierz sztywności sprężystej**: Macierz $C$ (lub macierz sztywności) zawiera stałe materiałowe, które definiują, w jaki sposób naprężenie odnosi się do odkształcenia. Każdy $C_{ij}$ reprezentuje związek między składową $i$ naprężenia a składową $j$ odkształcenia.
- **Wektor odkształceń**: Wektor odkształceń składa się z odkształceń normalnych ($\epsilon_1, \epsilon_2, \epsilon_3$) i odkształceń ścinających ($\gamma_{23}, \gamma_{13}, \gamma_{12}$).


Ze względu na symetryczną naturę zarówno tensorów naprężeń, jak i odkształceń w sprężystości liniowej, macierz sztywności jest również symetryczna. Oznacza to, że $C_{ij}=C_{ji}$, co zmniejsza liczbę niezależnych stałych potrzebnych do pełnego opisu zachowania materiału.

Ta uogólniona forma jest kluczowa dla analizy złożonych warunków obciążenia w zastosowaniach inżynieryjnych, szczególnie w materiałach, które nie wykazują jednolitych właściwości we wszystkich kierunkach (materiały **anizotropowe**). Zrozumienie tej zależności pozwala przewidywać, jak materiały będą się zachowywać pod różnymi typami obciążeń.

Uogólnioną forma prawa Hooke'a można zredukować, uwzględniając symetrie materiału. Na przykład w przypadku materiałów izotropowych, które mają jednorodne właściwości we wszystkich kierunkach, liczba niezależnych współczynników w macierzy sztywności może być zmniejszona do nawet tylko dwóch. W takich przypadkach można zastosować uproszczone modele, które uwzględniają tylko kilka kluczowych parametrów materiałowych, co upraszcza analizy i obliczenia związane z zachowaniem materiału pod wpływem obciążeń.

$$
\begin{bmatrix}
C_{11} & C_{12} & C_{12} & 0 & 0 & 0 \\
. & C_{11} & C_{12} & 0 & 0 & 0 \\
. & . & C_{11} & 0 & 0 & 0 \\
. & . & . & \frac{C_{11} - C_{12}}{2} & 0 & 0 \\
. & . & . & . & \frac{C_{11} - C_{12}}{2} & 0 \\
. & . & . & . & . & \frac{C_{11} - C_{12}}{2}
\end{bmatrix}
$$

**Odkształcenie sprężyste** występuje, gdy materiały są poddawane naprężeniom, które nie są zbyt duże, co pozwala im powrócić do pierwotnego kształtu po usunięciu naprężenia. Tego rodzaju deformacja jest istotna w kontekście projektowania i analizy materiałów, ponieważ umożliwia im funkcjonowanie w warunkach zmiennych obciążeń bez ryzyka trwałych uszkodzeń.

Prawo Hooke'a dotyczy zarówno rozciągania, jak i ściskania. Gdy ciało stałe jest wydłużane, jego wymiary zmniejszają się w kierunkach prostopadłych z powodu **efektu Poissona**. To zachowanie można zwizualizować, rozważając pręt cylindryczny: w miarę rozciągania się staje się cieńszy w średnicy.

[zdjęcie z książki]()

**Moduł sprężystości** $E$ określa sztywność materiału i jest definiowany jako stosunek naprężenia do odkształcenia. Metale zazwyczaj posiadają wysokie wartości modułu sprężystości. Zazwyczaj są sztywne i odporne na odkształcenia pod obciążeniem, podczas gdy polimery ma niski moduł sprężystości, co czyni je bardziej elastycznymi.

Zależność opisana przez prawo Hooke'a jest prawdziwa tylko do pewnej granicy znanej jako **granica sprężystości**. Po przekroczeniu tego punktu materiały mogą ulegać odkształceniom plastycznym, w wyniku czego nie powracają do swojego pierwotnego kształtu po usunięciu naprężenia.

Bibliografia:

[1] @book{alma991000386409708832,
author = {Fischer, Traugott E.},
address = {Amsterdam [etc},
booktitle = {Materials science for engineering students},
isbn = {9780123735874},
keywords = {Materiałoznawstwo},
language = {eng},
publisher = {Elsevier},
title = {Materials science for engineering students / Traugott Fischer.},
year = {2009},
}

[2] @book{alma991000389799708832,
author = {Soboyejo, Winston O.},
address = {New York ;},
booktitle = {Mechanical properties of engineered materials},
isbn = {0824789008},
keywords = {Materiały -- właściwości mechaniczne},
language = {eng},
publisher = {Marcel Dekker, Inc.},
series = {Mechanical Engineering : a series of textbooks and reference books ; 152},
title = {Mechanical properties of engineered materials / Wolé Soboyejo.},
year = {2003},
}

[3] @book{alma991001031769708832,
author = {Meyers, Marc André. and Chawla, Krishan K.},
address = {Cambridge [etc},
booktitle = {Mechanical behavior of materials},
edition = {2nd ed.},
isbn = {9780521866750},
keywords = {Wytrzymałość materiałów ; Materiały -- właściwości mechaniczne},
language = {eng},
publisher = {Cambridge University Press},
title = {Mechanical behavior of materials / Marc André Meyers, Krishan Kumar Chawla.},
year = {2009},
}

[4] @book{kittel1976wstęp,
  title={Wst{\k{e}}p do fizyki cia{\l}a sta{\l}ego},
  author={Kittel, C.},
  url={https://books.google.pl/books?id=3IO0AAAAIAAJ},
  year={1976},
  publisher={Pa{\'n}stwowe wydawnictwo naukowe}
}