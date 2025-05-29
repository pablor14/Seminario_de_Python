

 [O jogador está visível?]
├── Não
│   └── [Está patrulhando?]
│       ├── Sim → Continuar patrulha
│       └── Não → Voltar à posição inicial
└── Sim
    └── [Distância até o jogador < 5 metros?]
        ├── Não
        │   └── [Tem cobertura próxima?]
        │       ├── Sim → Perseguir com cautela
        │       └── Não → Perseguir correndo
        └── Sim
            └── [Vida do NPC > 40%?]
                ├── Sim → Atacar
                └── Não → Fugir / Procurar abrigo





def decidir_comportamento(jogador_visivel, distancia_jogador,vida_npc, tem_cobertura,patrulhando):
    if not jogador_visivel:
        if patrulhando:
            return "Continuar patrulha"
        else:
            return "Voltar à posição inicial"
    else:
        if distancia_jogador >= 5:
            if tem_cobertura:
                return "Perseguir com cautela"
            else:
                return "Perseguir correndo"
           else:
            if vida_npc > 40:
                return "Atacar"
            else:
                return "Fugir / Procurar abrigo"

# uso:
npc_acao = decidir_comportamento(
    jogador_visivel= True,
    distancia jogador =3,
    vida_npc = 35,
    tem_cobertura=False,
    patrulhando=False
)

print("Decisão do NPC:" npc_acao)
