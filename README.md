## ¿Qué pasa con la sucesión al infinito?

Tenmos que la sucesón de Tribonacci está dada como 

$T_n = T_{n-3} +T_{n-2}+ T_{n-1}$

donde $T_n  \geq 0 \ \forall n \in \mathbb{N}$
Así, responder la apregunta es quivalente a  resolver el siguiente límite

$\lim_{n \to \infty} T_n$
 
Por como está definido $T_n$ es fácil ver que está es creciente, de hecho, es exponencialmente creciente pues con un poco de tabulación se ve que los números van en rápido aumento y dado que es la suma de los 3 índices anteriores (naturales), por pura intuición, se ve que no hay un límite a la suma de estos los $T_n$, ie , $\lim_{n \to \infty} T_n= \infty$.

Otra forma de verlo es que (al investigar en internet) $T_n \approx C\lambda^n$  donde $\lambda >1$ asi si $n \to \infty$ se tiene que $T_n \to \infty$

## ¿Diverge?
Por el analisis anterior, sí, la sucesión de Tribonacci diverge normalmente, sin embargo, nosotros tenemos $T_n mod(10^5)$ lo cual cambia las cosas.

Recordemos que para cualquier número entero $a$ tenemos que 

$a \mod (m) =r$

donde $r$ es el resuido de dividir $a$ entre $m$ y siempre se cumple que: 

$0 \leq r < m$

Si $m= 10^5= 100,000$  entonces 

$0 leq T_n \mod (10^5) < 100,000$

Es decir

$T_n \mod (10^5) \in \{0,1,..., 99999\}$

Entonces la función $T_n \mod(10^5)$ es ciclica, por lo que no diverge.


