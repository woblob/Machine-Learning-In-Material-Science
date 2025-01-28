#### Moduł ścinania ($G_{VRH}$)
**Moduł ścinania**, znany również jako moduł sprężystości poprzecznej, określa reakcję materiału na naprężenie ścinające (równolegle do powierzchni).
Definiowany jest jako:

$$
G = \frac{\tau}{\gamma}
$$

gdzie:
- $G$ to moduł ścinania,
- $\tau$ to naprężenie ścinające,
- $\gamma$ to odkształcenie ścinające.

Siła ścinająca przyłożona do ciała stałego, powoduje że ​​sąsiadujące warstwy materiału przesuwają się względem siebie. Moduł ścinania jest stałą określającą tę zależność między zastosowanym naprężeniem ścinającym a wynikającym z niego odkształceniem (odkształceniem ścinającym).

Materiały o wysokim module ścinania są w stanie wytrzymać znaczne odkształcenie bez uginania się, co czyni je idealnymi do zastosowań konstrukcyjnych.

### Związek z innymi właściwościami mechanicznymi

Moduł ścinania jest związany z innymi modułami sprężystości, takimi jak moduł Younga ($E$) lub wcześniej wspomniany, moduł objętościowy ($K$). W przypadku materiałów izotropowych związki te można wyrazić jako:

$$
G = \frac{E}{2(1 + \nu)} = \frac{3(1 − 2ν)K}{2(1 + ν)}
$$

gdzie:
- $\nu$ to współczynnik Poissona
- $K$ to moduł sprężystości objętościowej
- $E$ to moduł Younga

To równanie pokazuje, że moduł ścinania można przedstawiać w różny sposób, w zależności jakie właściwości materiału znamy. 

W części praktycznej moduły sprężystości objętościowej i poprzecznej będą określone jako $K_{VRH}$ i $G_{VRH}$.

$"V R H"$ to skrót od nazwisk Voigt-Reuss-Hill.

Metody Voigt, Reuss i Hill są powszechnie stosowane w mechanice materiałów do określenia efektywnych modułów sprężystości w materiałach kompozytowych oraz wielofazowych.

## Metoda Voigta
Metoda Voigta zakłada, że w całym materiale odkształcenie jest stałe. W efekcie, efektywny moduł sprężystości (np. Younga) oblicza się jako średnią arytmetyczną modułów poszczególnych faz:
$$
  E_V = \sum{E_iV_i}
$$
gdzie $E_i$ i $V_i$ to moduł Younga i udział procentowy dla fazy $i$.

## Metoda Reussa
Metoda Reussa zakłada, że wszystkie fazy materiału są poddawane tym samym odkształceniom. W wyniku tego efektywny moduł sprężystości jest obliczany jako średnia harmoniczna:
  $$
  \frac{1}{E_R} = \sum\frac{V_i}{E_i}
  $$

gdzie $E_i$ i $V_i$ to moduł Younga i udział procentowy dla fazy $i$.
To daje dolną granicę dla efektywnego modułu sprężystości.

## Metoda Hilla
Metoda Hilla łączy podejścia Voigta i Reussa, oferując uśredniony wynik pomiędzy tymi dwiema metodami. 

Efektywny moduł Younga $E_H$ oblicza się jako:
  $$
  E_H = \frac{1}{2}\left(E_V + E_R\right)
  $$
  co umożliwia uzyskanie wartości pośredniej między wartościami uzyskanymi z obu poprzednich metod.
