# Kukulkán: serpente de luz, geometria projetiva e calendário anual

## Estado do documento

```yaml
artifact_id: KUKULKAN-SHADOW-CALENDAR-001
site: Chichen Itza
structure: Estrutura 2D5 / El Castillo / Templo de Kukulkan
culture_context: Maya-Toltec / Posclassico
claim_allowed: false
status: MODEL_FORMULATED
last_reviewed: 2026-07-25
```

Este documento corrige uma confusão de sítios:

- **El Castillo / Templo de Kukulkán** está em **Chichén Itzá** e produz a hierofania luminosa conhecida como o *Descenso de Kukulkán*;
- a **Pirâmide/Templo da Serpente Emplumada, Quetzalcóatl**, em **Teotihuacán**, é outro monumento, de outro contexto urbano e cronológico.

Não se deve transferir automaticamente a geometria luminosa de Chichén Itzá para Teotihuacán.

---

## 1. O fenômeno observado

A manifestação mais conhecida ocorre na **balaustrada noroeste da escadaria norte** de El Castillo, no período da tarde. Conforme o Sol se dirige ao horizonte oeste, as sombras dos corpos escalonados deixam regiões triangulares iluminadas sobre a rampa. A sequência luminosa parece formar o corpo de uma serpente que termina na cabeça pétrea situada na base.

O dado mais recente do INAH descreve um padrão anual, e não apenas dois dias equinociais:

| Âncora anual | Estado luminoso informado |
|---|---|
| 12 de fevereiro | primeira marca breve na parte superior |
| 4 de março | cinco triângulos |
| 15–25 de março | sete triângulos persistentes; equinócio no centro aproximado da janela |
| 26 de março | oitavo triângulo |
| 9 de abril | nove triângulos |
| 24 de maio | balaustrada plenamente iluminada; primeiro passo zenital |
| 21 de junho | iluminação majoritária no solstício |
| 19 de julho | última iluminação plena; segundo passo zenital |
| 2 de setembro | nove triângulos novamente definidos |
| janela do equinócio de setembro | sete triângulos |
| 9 de outubro | cinco triângulos |
| cerca de 29 de outubro | últimos resplandores breves |
| depois de 29 de outubro | rampa em sombra por 52 dias antes e 52 dias depois do solstício de inverno |

Essa sequência permite distinguir duas dinâmicas.

### 1.1 Movimento intradiário

Durante uma tarde observável:

\[
\frac{dh_\odot}{dt}<0,
\]

isto é, a altura solar diminui. Os triângulos aparecem progressivamente em regiões inferiores da balaustrada e a figura parece **descer espacialmente**.

### 1.2 Movimento anual

Ao longo do ano, o número e a largura das regiões iluminadas aumentam, atingem uma zona de saturação e diminuem:

```text
12 fev → aumento de triângulos → iluminação plena → diminuição → 29 out
                                      |
                              janela escura sazonal
```

A linguagem “serpente que sobe e desce” deve, portanto, declarar a escala:

- `DESCIDA_ESPACIAL_INTRADIARIA`: fenômeno visual documentado na tarde;
- `ASCENSAO_ANUAL_DE_ILUMINACAO`: aumento sazonal do número/largura dos triângulos;
- `DESCIDA_ANUAL_DE_ILUMINACAO`: redução sazonal dos triângulos;
- `ASCENSAO_ESPACIAL_INTRADIARIA`: simetria matemática ou hipótese, não promovida a evento histórico sem observação específica.

---

## 2. Geometria de primeira ordem

As dimensões publicadas são aproximadamente:

\[
B=55{,}5\ \mathrm{m}
\]

por lado na base, e:

\[
H_{\mathrm{total}}\approx30\ \mathrm{m},
\]

incluindo os nove corpos e o templo superior. Uma decomposição arquitetônica frequentemente informada usa aproximadamente:

\[
H_{\mathrm{corpo}}\approx24\ \mathrm{m},
\qquad
H_{\mathrm{templo}}\approx6\ \mathrm{m}.
\]

A meia-base é:

\[
R=\frac{B}{2}=27{,}75\ \mathrm{m}.
\]

### 2.1 Pitágoras — perfil idealizado

Tratando o corpo escalonado por seu envelope inclinado:

\[
\ell=\sqrt{R^2+H_{\mathrm{corpo}}^2}.
\]

Com os valores aproximados:

\[
\ell=\sqrt{27{,}75^2+24^2}\approx36{,}6887\ \mathrm{m}.
\]

O ângulo médio do envelope em relação ao plano horizontal é:

\[
\theta=\arctan\left(\frac{H_{\mathrm{corpo}}}{R}\right)
\approx40{,}8554^\circ.
\]

Esses valores descrevem um envelope; não substituem o levantamento dos degraus, rampas, restaurações e irregularidades reais.

---

## 3. Fator autoral da altura do triângulo equilátero

O fator:

\[
q=\frac{\sqrt3}{2}\approx0{,}8660254
\]

é a razão entre a altura e o lado de um triângulo equilátero:

\[
h_{\triangle}=\frac{\sqrt3}{2}a.
\]

Aplicando **somente como teste dimensional** à meia-base de El Castillo:

\[
H_q=qR
=\frac{\sqrt3}{2}(27{,}75)
\approx24{,}0322\ \mathrm{m}.
\]

Comparando com o valor arredondado de 24 m para o corpo escalonado:

\[
\Delta H=H_q-H_{\mathrm{corpo}}
\approx0{,}0322\ \mathrm{m}.
\]

A diferença relativa é:

\[
\varepsilon_q=
\frac{|H_q-H_{\mathrm{corpo}}|}{H_{\mathrm{corpo}}}
\approx0{,}134\%.
\]

O ângulo correspondente ao fator é:

\[
\theta_q=\arctan\left(\frac{\sqrt3}{2}\right)
\approx40{,}8934^\circ,
\]

com diferença aproximada:

\[
\theta_q-\theta\approx0{,}0380^\circ.
\]

### Fronteira epistemológica

Esse ajuste é numericamente próximo, mas **não demonstra intenção construtiva**. As medidas publicadas são arredondadas, o corpo é escalonado, houve consolidação/restauração e a escolha de `24 m` versus `30 m` depende de incluir ou não o templo superior.

```yaml
SQRT3_OVER_2_NUMERICAL_MATCH: OBSERVED_FROM_ROUNDED_DIMENSIONS
DESIGN_INTENT: TOKEN_VAZIO
ARCHAEOLOGICAL_PROOF: TOKEN_VAZIO
```

O teste correto exige nuvem de pontos 3D ou levantamento total-estação, separando corpo escalonado, templo, balaustrada e fases de restauração.

---

## 4. Sol como senoide anual

A declinação solar pode ser aproximada por:

\[
\delta(n)\approx
\varepsilon
\sin\left(\frac{2\pi(n-n_0)}{Y}\right),
\]

onde:

- `n` é o dia;
- `n_0` é uma fase de referência próxima do equinócio;
- `Y` é o ano tropical;
- `\varepsilon\approx23{,}44^\circ` é a obliquidade terrestre.

A polaridade anual é:

\[
p_y(n)=\operatorname{sgn}\left(\frac{d\delta}{dn}\right).
\]

Ela distingue duas passagens por declinações semelhantes:

\[
(\delta,+1)\neq(\delta,-1).
\]

A serpente luminosa não é uma senoide desenhada diretamente na pedra. A senoide modela a variável astronômica que governa a geometria de iluminação ao longo do ano.

---

## 5. Posição solar e vetor de incidência

Para latitude `\varphi`, declinação `\delta` e ângulo horário `\omega`, a altura solar satisfaz:

\[
\sin h_\odot=
\sin\varphi\sin\delta+
\cos\varphi\cos\delta\cos\omega.
\]

O azimute pode ser calculado por:

\[
\cos A_\odot=
\frac{\sin\delta-\sin\varphi\sin h_\odot}
{\cos\varphi\cos h_\odot}.
\]

O vetor unitário que aponta para o Sol é:

\[
\mathbf s(A,h)=
\begin{bmatrix}
\cos h\sin A\\
\cos h\cos A\\
\sin h
\end{bmatrix}.
\]

Em torno do equinócio, usando `\varphi\approx20^\circ40' N` e tempo solar aproximado, obtemos apenas como régua inicial:

| Hora solar | Altura aproximada | Azimute aproximado |
|---:|---:|---:|
| 14:30 | 47,93° | 245,30° |
| 15:00 | 41,42° | 250,56° |
| 15:30 | 34,72° | 254,85° |
| 16:00 | 27,89° | 258,48° |
| 16:30 | 20,98° | 261,68° |
| 17:00 | 14,01° | 264,60° |

Esses números não determinam sozinhos a serpente: é necessário combinar orientação real do edifício, relevo do horizonte, refração, época, geometria 3D e restauração.

---

## 6. Projeção exata da sombra sobre a balaustrada

Considere:

- um ponto `\mathbf x_i` sobre a aresta do corpo `i`;
- o vetor solar `\mathbf s(t)`;
- o plano da balaustrada `\Pi_b`, definido por

\[
\mathbf n_b\cdot\mathbf x=d_b.
\]

O raio de sombra é:

\[
\mathbf r_i(\lambda,t)=
\mathbf x_i-\lambda\mathbf s(t).
\]

A interseção com a balaustrada ocorre em:

\[
\lambda_i(t)=
\frac{\mathbf n_b\cdot\mathbf x_i-d_b}
{\mathbf n_b\cdot\mathbf s(t)},
\]

quando o denominador é diferente de zero.

Logo:

\[
\boxed{
\mathbf p_i(t)=
\mathbf x_i-
\frac{\mathbf n_b\cdot\mathbf x_i-d_b}
{\mathbf n_b\cdot\mathbf s(t)}
\mathbf s(t)
}
\]

é a borda de sombra projetada na rampa.

Os triângulos luminosos não são postulados: eles devem surgir da diferença entre as projeções consecutivas das arestas dos corpos e os limites laterais da balaustrada.

---

## 7. Bhaskara como detector local de entrada e saída da luz

A trajetória solar completa é trigonométrica. Bhaskara não deve substituir a astronomia esférica. Contudo, perto de uma janela curta, a função de contato de uma borda pode ser aproximada por segunda ordem.

Se `u_i(t)` é a coordenada projetada da sombra ao longo da rampa e `u_b` um limite observado, defina:

\[
g_i(t)=u_i(t)-u_b.
\]

Perto de `t_0`, com `\tau=t-t_0`:

\[
g_i(\tau)\approx a_i\tau^2+b_i\tau+c_i.
\]

Os instantes locais de contato são:

\[
\boxed{
\tau_{i,\pm}=
\frac{-b_i\pm\sqrt{b_i^2-4a_ic_i}}{2a_i}
}
\]

O discriminante classifica a observação:

\[
\Delta_i=b_i^2-4a_ic_i.
\]

- `\Delta_i<0`: a borda não cruza o limite na janela;
- `\Delta_i=0`: contato tangencial, candidato a primeiro/último resplendor;
- `\Delta_i>0`: dois cruzamentos locais, entrada e saída da faixa iluminada.

Assim, Bhaskara entra como **aproximação local de eventos de contato**, não como explicação total da serpente.

---

## 8. Estado calendárico da serpente

Defina:

\[
K(n,t)=
\left(
N_\triangle,
W_\triangle,
P_\triangle,
h_\odot,
A_\odot,
p_y,
p_d
\right),
\]

onde:

- `N_\triangle`: número de triângulos visíveis;
- `W_\triangle`: vetor de larguras;
- `P_\triangle`: persistência até o ocaso;
- `p_y`: polaridade anual;
- `p_d=\operatorname{sgn}(dh_\odot/dt)`: polaridade intradiária.

Na tarde do fenômeno:

\[
p_d=-1.
\]

No ramo anual crescente:

\[
p_y=+1,
\]

no ramo decrescente:

\[
p_y=-1.
\]

O mesmo número de triângulos em março e setembro não representa necessariamente o mesmo estado:

\[
(N_\triangle,+1)\neq(N_\triangle,-1).
\]

Esse é o núcleo matemático da conservação de polaridade.

---

## 9. Relações calendáricas

### 9.1 Estrutura arquitetônica tradicionalmente lida como calendário

A leitura arquitetônica mais divulgada registra:

\[
4\times91+1=365
\]

para as quatro escadarias e o patamar/templo superior, e relaciona os nove corpos divididos pelas escadarias a dezoito seções visuais.

Essa associação é relevante, mas sua intenção histórica precisa permanecer vinculada às fontes arqueológicas e ao debate especializado.

### 9.2 Haab'

\[
18\times20+5=365.
\]

A proximidade entre dezoito seções arquitetônicas e dezoito períodos de vinte dias é uma hipótese interpretativa que deve ser testada documentalmente, e não afirmada apenas pela igualdade numérica.

### 9.3 O número 52 em duas escalas

O relatório de 2026 descreve ausência de iluminação da rampa por:

\[
52\ \text{dias antes do solstício de inverno}
\]

e:

\[
52\ \text{dias depois do solstício de inverno}.
\]

A Roda Calendárica mesoamericana fecha em aproximadamente 52 anos Haab'. As duas ocorrências compartilham o número 52, mas possuem unidades e mecanismos diferentes:

\[
52\ \mathrm{dias}\neq52\ \mathrm{anos}.
\]

```yaml
NUMERICAL_RECURRENCE_52: OBSERVED
MECHANISM_IDENTITY: PROHIBITED_WITHOUT_DERIVATION
CULTURAL_INTERPRETATION: HYPOTHESIS
```

### 9.4 Vênus

A literatura arqueoastronômica propõe que a leitura de El Castillo seja comparada também aos períodos sinódicos de Vênus. O fechamento aritmético convencional é:

\[
5\times584=8\times365=2920\ \mathrm{dias}.
\]

A igualdade é aritmética. Demonstrar que a sequência luminosa da balaustrada executa ou marca esse ciclo requer dados observacionais, inscrições, fontes e teste cronológico independente.

---

## 10. Protocolo executável

### Entradas mínimas

```yaml
site_coordinates:
orientation_matrix:
point_cloud_3d:
terrace_edges:
balustrade_plane:
serpent_head_geometry:
horizon_profile:
restoration_mask:
observation_dates:
image_timestamps:
weather_and_refraction:
```

### Pipeline

```text
posição solar
→ vetor de incidência
→ projeção das arestas
→ interseção com a balaustrada
→ polígonos iluminados
→ contagem e largura dos triângulos
→ comparação com fotografias
→ resíduos
→ estado de evidência
```

### Métricas

\[
E_{\mathrm{pixel}}=
\frac{|M_{\mathrm{previsto}}\oplus M_{\mathrm{observado}}|}
{|M_{\mathrm{observado}}|}
\]

\[
E_N=|N_{\mathrm{previsto}}-N_{\mathrm{observado}}|
\]

\[
E_t=|t_{\mathrm{contato,pred}}-t_{\mathrm{contato,obs}}|.
\]

### Controles nulos

1. orientação aleatória preservando dimensões;
2. pirâmide lisa sem corpos escalonados;
3. corpos com alturas embaralhadas;
4. horizonte plano versus horizonte medido;
5. geometria anterior e posterior à restauração;
6. fator `\sqrt3/2` fixo versus inclinação livre estimada.

---

## 11. Falsificadores

A hipótese geométrica específica é enfraquecida ou rejeitada quando:

- o modelo 3D não reproduz a ordem de aparecimento dos triângulos;
- uma orientação aleatória produz ajuste equivalente;
- a inclinação livre supera de forma robusta o fator `\sqrt3/2`;
- a sequência anual prevista diverge das datas observadas;
- o efeito desaparece ao usar a geometria anterior à restauração;
- não existe documentação cultural que sustente a interpretação calendárica proposta.

---

## 12. Estados finais

```yaml
F_ok:
  - sitio e monumento corrigidos
  - descida intradiaria documentada
  - ciclo anual de iluminacao documentado
  - projecao geometrica formalizada
  - Pitagoras aplicado ao perfil
  - Bhaskara delimitada a contatos locais
  - proximidade sqrt3_over_2 calculada
F_gap:
  - nuvem de pontos e medidas sem arredondamento
  - orientacao e plano exato da balaustrada
  - mascara de restauracao
  - serie fotografica com timestamps
  - teste estatistico dos modelos nulos
  - derivacao historica para 18x20, 52 e Venus
F_next:
  - reconstruir a Estrutura 2D5 em 3D
  - executar ray casting solar por minuto e por dia
  - publicar residuos e resultados negativos
claim_allowed: false
```

---

## Referências-base

- Casares Contreras, O. J. (2018). *Los estudios arqueoastronómicos de El Castillo de Chichén Itzá: nuevas propuestas para su interpretación*. Arqueología, 54, 155–166.
- Casares Contreras, O. J. (2021). *Kukulcán, Venus y los ciclos agrícolas en la estructura 2D5 de Chichén Itzá, Yucatán*. TRACE, 79, 37–65. DOI: `10.22134/trace.79.2021.689`.
- Casares Contreras, O. J.; Montero García, A.; Galindo Trejo, J.; Wood Cano, D. (2026). *El Castillo de Chichén Itzá. Evocación de un mensaje majestuoso de trascendencia calendárica*. Arqueología Mexicana, 197.
- Instituto Nacional de Antropología e Historia. *Zona Arqueológica de Chichén Itzá*.
- Instituto Nacional de Antropología e Historia / Secretaría de Cultura (2026). *Aspectos calendáricos y astronómicos de El Castillo de Chichén Itzá*.
