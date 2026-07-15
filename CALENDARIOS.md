# CALENDARIOS — Floresta Relacional de Tempo, Lugar e Evidência

## Intenção

Este núcleo transforma o repositório de geometria solar Maia/Inca em uma base extensível para calendários de vários lugares, sem afirmar que culturas distintas registraram o mesmo mecanismo.

A unidade mínima de pesquisa é:

```text
lugar + cultura + ciclo + observável + método + incerteza + fonte + estado de prova
```

A relação entre unidades é registrada por uma matriz, não por semelhança narrativa.

## Invariante temporal

Um calendário é tratado como função de estado:

```math
C_n=(P_n,O_n,G_n,S_n,U_n)
```

onde:

- `P`: período declarado;
- `O`: observável — Sol, Lua, Vênus, estação, maré, sombra ou evento celeste;
- `G`: geometria — azimute, altitude, orientação, intervalo ou proporção;
- `S`: fonte e contexto cultural;
- `U`: incerteza, lacuna e condição de revisão.

A comparação entre dois calendários não presume identidade:

```math
R(C_i,C_j)=\langle semelhanças, diferenças, incertezas, fontes, falsificadores\rangle
```

## Camadas de relacionamento

1. **Astronômica:** período, órbita, declinação, precessão e visibilidade.
2. **Geométrica:** azimute, altitude, sombra, eixo, horizonte e orientação arquitetônica.
3. **Ambiental:** estação, chuva, plantio, maré, latitude e relevo.
4. **Material:** erosão, restauração, deslocamento, tolerância e datação.
5. **Cultural:** nome, uso documentado, registro, ritual e transmissão.
6. **Estatística:** erro angular, intervalo, covariância, hipótese nula e comparação.
7. **Topológica:** ciclos locais e globais, grafos de dependência e percurso toroidal.
8. **Epistêmica:** `VERIFIED`, `PARTIAL`, `HYPOTHESIS`, `TOKEN_VAZIO`, `CONTRADICTION`, `PHILOSOPHICAL`.

## Percurso toroidal

O toróide é usado como modelo de navegação em dois ciclos, não como prova de que todos os calendários ou o universo sejam fisicamente toroidais.

```math
x=(R+r\cos\theta)\cos\phi
```

```math
y=(R+r\cos\theta)\sin\phi
```

```math
z=r\sin\theta
```

Interpretação operacional:

- `theta`: ciclo local — observação, medida, erro, correção e repetição;
- `phi`: ciclo longo — ano, série sinódica, precessão, tradição e comparação entre lugares.

Um retorno ao mesmo nó só é válido quando existe nova fonte, nova medida, novo erro ou nova contradição.

## Núcleo atual

O repositório já registra como objetos de trabalho:

- azimute solar;
- altura solar ao meio-dia;
- obliquidade terrestre;
- correção precessional;
- ciclo de Vênus;
- Tzolk'in `13 x 20 = 260`;
- geometria arquitetônica Maia e Inca;
- hipótese de ressonância eletromagnética em Teotihuacán, que permanece separada dos objetos astronômicos estabelecidos.

## Expansão por lugares distintos

A matriz inclui candidatos para ampliar a floresta. Eles começam como `TOKEN_VAZIO` até receberem fonte e medida:

- Mesoamérica além do núcleo atual;
- Andes além do núcleo atual;
- Amazônia;
- Egito;
- Mesopotâmia;
- Polinésia e Pacífico;
- Atlântico Norte e Islândia;
- Mediterrâneo megalítico;
- sul do Brasil e Florianópolis;
- outros lugares adicionados por evidência.

A presença nessa lista é somente escopo de pesquisa. Não é afirmação de alinhamento, contato cultural ou mecanismo comum.

## Pontos latentes, esquecidos ou menos tratados

| Ponto | Estado | Problema operacional | Próximo trabalho |
|---|---|---|---|
| Incerteza angular | `UNDERSERVED` | valores aparecem sem intervalo completo | propagar erro de coordenada, horizonte, época e instrumento |
| Erosão e restauração | `UNDERSERVED` | a geometria atual pode diferir da original | registrar material, intervenção e tolerância |
| Calendários lunares e marés | `LATENT` | foco atual é majoritariamente solar | criar observáveis e períodos separados |
| Comparação com eventos catalogados | `LATENT` | falta ponte executável com catálogo celeste | usar somente eventos com proveniência validada |
| Contradições entre fontes | `FORGOTTEN` | divergências tendem a desaparecer em sínteses | preservar versões e registrar conflito |
| Grafos de influência cultural | `TOKEN_VAZIO` | sem dados suficientes para arestas causais | começar apenas com arestas de citação e coexistência |
| Números primos | `IGNORED` | nenhuma função formal demonstrada no calendário atual | excluir até existir definição e teste |
| Reconstruções vetoriais | `UNDERSERVED` | imagens podem perder escala e origem | registrar coordenadas, escala, licença e transformação |

## Matriz executável

Arquivo canônico:

```text
data/calendar_cycles_matrix.json
```

Validação local:

```bash
python3 scripts/validate_calendar_matrix.py
```

O validador bloqueia:

- IDs duplicados;
- ciclos sem lugar ou observável;
- períodos sem unidade;
- registros científicos sem fonte;
- candidatos promovidos sem evidência;
- relações com nós inexistentes;
- equivalência cultural declarada sem método.

## Ponte com o ecossistema

```text
GEOMETRIA_SOLAR_Maia_Inca
  -> Cosmos: índice e floresta relacional
  -> Catalogo-cosmologico: eventos e objetos com proveniência
  -> relativity-living-light: estatística, covariância e falsificadores
  -> ChipQuantum: execução geométrica e topológica
  -> papers: publicação e revisão
```

Cada repositório permanece responsável pelo seu próprio dado. A ponte carrega referências e estados de prova, não cópias integrais nem validação automática.

## Regra final

```text
sem fonte      -> TOKEN_VAZIO
sem incerteza  -> PARTIAL
sem método     -> não comparar
sem mecanismo  -> não afirmar causalidade
com conflito   -> preservar CONTRADICTION
```

A floresta cresce por relações comprováveis; o que ainda não foi tratado permanece visível como tarefa, não como verdade inventada.