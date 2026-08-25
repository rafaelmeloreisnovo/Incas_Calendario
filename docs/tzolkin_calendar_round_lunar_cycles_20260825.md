# Tzolk’in × Haab × Calendar Round × Lua — extensão observacional 2026-08-25

**Estado:** `APPEND_ONLY | CLAIM_ALLOWED=false`  
**Parent:** `data/calendar_cycles_matrix.json`  
**Regra:** `contagem calendárica ≠ forçante física ≠ correlação ≠ causalidade`.

## 1. Reconstrução aritmética

O Tzolk’in combina 13 números e 20 nomes de dia:

```text
13 × 20 = 260 dias
```

O Haab possui 365 dias. A recorrência da mesma combinação Tzolk’in/Haab é:

```text
lcm(260,365) = 18.980 dias
18.980 / 260 = 73 Tzolk'in
18.980 / 365 = 52 Haab
```

Em ano tropical médio de 365,2422 dias:

```text
18.980 / 365,2422 = 51,9655177 anos tropicais
52 × 365,2422 - 18.980 = 12,5944 dias
```

Assim, `52 Haab` e `51,9655 anos tropicais` descrevem o mesmo intervalo em duas unidades distintas. Isso é uma identidade de contagem, não uma prova de periodicidade solar, lunar ou auroral.

## 2. Relógios independentes para comparação

### Calendáricos

- Tzolk’in: 260 d;
- Haab: 365 d;
- Calendar Round: 18.980 d.

### Astronômicos/físicos

- lunação sinódica: ~29,53059 d;
- envelope spring-neap: ~14,7653 d;
- ciclo nodal lunar: ~18,61 anos;
- recorrência aproximada da rotação solar: ~27 d;
- harmônico de meia rotação: ~13,5 d;
- geometria semi-anual/equinocial: ~182,62 d;
- ano tropical: ~365,2422 d.

Cada relógio deve ocupar uma coluna própria. Nenhum período deve ser arredondado para outro somente por proximidade numérica.

## 3. Codificação de fase

Para período `P` e época explícita `t0`:

```text
φP(t) = 2π × (((t - t0) mod P) / P)
XP(t) = [sin φP(t), cos φP(t)]
```

O par seno/cosseno evita a descontinuidade artificial entre o último e o primeiro dia de um ciclo.

O `t0` precisa ser registrado e testado por sensibilidade. Um resultado que apareça somente após escolher retrospectivamente um `t0` favorável não fecha evidência.

## 4. Lua: por que entra como eixo físico

A Lua entra porque há mecanismos físicos próprios — gravitação/marés, geometria de iluminação e marés atmosféricas. NASA ICON/GOLD já observou assinatura de maré lunar na termosfera-ionosfera através de ventos neutros, deriva de plasma e emissão O 135,6 nm.

Logo:

```text
LUA → maré oceânica/atmosférica = mecanismo físico
LUA → aurora diretamente         = TOKEN_VAZIO até evidência
```

Há literatura regional em que ciclos de maré/lunação modulam mistura e comunidades planctônicas, mas isso não autoriza lei biológica global.

## 5. Calendar Round como hipótese estatística

O Calendar Round pode entrar em uma regressão como feature exploratória de fase, porém depois dos drivers físicos conhecidos:

```text
Y(t) = baseline_sazonal
     + vento_solar/IMF
     + dipole_tilt/Kp/AE/Dst
     + lua/maré
     + Tzolk'in/Haab/CalendarRound
     + ε
```

Se a feature de 260 d ou 18.980 d não aumentar desempenho fora da amostra, ela permanece descrição calendárica e não preditor físico.

## 6. Relação com o teste auroral de ~52 anos

O arquivo DMSP de 1973–1974 permite comparar a extensão equatorward da atividade auroral com dados modernos de 2025–2026. A distância temporal próxima de 52 anos torna essa comparação interessante para o Calendar Round, mas duas épocas não bastam para identificar periodicidade.

Para testar periodicidade de ~18.980 d é necessário recuperar épocas intermediárias e normalizar instrumentos/coordenadas/atividade solar. Sem isso:

`CALENDAR_ROUND_AURORA_52Y_PERIODICITY = TOKEN_VAZIO_IDENTIFIABILITY`.

## 7. Fontes de autoridade

- Smithsonian National Museum of the American Indian, Living Maya Time — Tzolk’in, Haab e Calendar Round.
- NASA Moon/Tides — fases e mecanismos de maré.
- NASA ICON/GOLD — observação de maré lunar na termo-ionosfera.
- NASA/NTRS — recorrências 27/13,5 d e variação semi-anual geomagnética/Russell–McPherron.

## 8. F_ok / F_gap / F_next

`F_ok`: 260/365/18.980 reconstruídos sem numerologia; 51,9655↔52 Haab explicitado; Lua e ciclos heliogeomagnéticos separados por mecanismo.

`F_gap`: nenhuma causalidade Tzolk’in→aurora foi demonstrada; série auroral de ~52 anos ainda não é identificável com apenas duas épocas.

`F_next`: ligar esta extensão ao cubo histórico auroral do Mapa e testar os ciclos somente após baseline físico.

`DELTA`: extensão append-only; `data/calendar_cycles_matrix.json` original permanece intacto.
