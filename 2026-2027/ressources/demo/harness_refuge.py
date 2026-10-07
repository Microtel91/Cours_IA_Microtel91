"""Démo : l'intelligence ne vient pas que du modèle.

Le MÊME modèle répond à la MÊME question, avec un harness de plus en plus complet :

  Niveau 0 : le modèle seul. Il répond de mémoire (il ne connaît pas notre refuge !).
  Niveau 1 : on lui donne un OUTIL (exécuter du Python) et une BOUCLE.
  Niveau 2 : on ajoute du CONTEXTE (où sont les données, à quoi elles ressemblent)
             et des RÈGLES (permissions, nombre d'étapes maximum).

Lancer (dans l'invite Anaconda, depuis ce dossier) :
  python harness_refuge.py                 -> les 3 niveaux, avec l'API Mistral
  python harness_refuge.py --niveau 2      -> un seul niveau
  python harness_refuge.py --demander      -> le harness demande la permission avant chaque outil
  python harness_refuge.py --local         -> modèle local avec Ollama (sans internet)
  python harness_refuge.py --modele mistral-large-latest   -> changer de modèle, garder le harness

Pour l'API Mistral, la clé doit être dans la variable d'environnement MISTRAL_API_KEY :
  Windows : set MISTRAL_API_KEY=ta_cle        Linux/Mac : export MISTRAL_API_KEY=ta_cle
"""

import argparse
import json
import os
import subprocess
import sys

import requests

QUESTION = ("Combien de chats du refuge attendent encore d'être adoptés, "
            "et comment s'appelle le plus âgé d'entre eux ?")
DOSSIER = os.path.dirname(os.path.abspath(__file__))

OUTIL_PYTHON = {
    "type": "function",
    "function": {
        "name": "executer_python",
        "description": "Exécute du code Python et renvoie ce qu'il affiche avec print().",
        "parameters": {
            "type": "object",
            "properties": {"code": {"type": "string", "description": "Le code Python à exécuter."}},
            "required": ["code"],
        },
    },
}


def contexte():
    """Niveau 2 : ce que le modèle ne peut pas deviner tout seul."""
    with open(os.path.join(DOSSIER, "refuge.csv"), encoding="utf-8") as f:
        debut = "".join(f.readlines()[:4])
    return (
        "Tu aides l'équipe d'un refuge pour animaux. Les données du refuge sont dans le fichier "
        "'refuge.csv' (dossier courant). Voici ses premières lignes :\n" + debut +
        "\nLe module pandas n'est peut-être pas installé : utilise le module csv. "
        "Ne réponds jamais de mémoire : calcule avec l'outil, puis réponds en une ou deux phrases."
    )


def executer(code):
    """L'outil : le harness lance le code dans un processus séparé et renvoie la sortie."""
    try:
        r = subprocess.run([sys.executable, "-c", code], cwd=DOSSIER, capture_output=True,
                           text=True, timeout=20, encoding="utf-8")
        return (r.stdout + r.stderr).strip()[-2000:] or "(rien n'a été affiché)"
    except subprocess.TimeoutExpired:
        return "Erreur : le code a mis trop de temps (plus de 20 secondes)."


def appeler(config, messages, outils):
    """Un appel au modèle = une ÉTAPE. Le modèle lit du texte et écrit du texte, c'est tout."""
    corps = {"model": config["modele"], "messages": messages, "temperature": 0.2}
    if outils:
        corps["tools"] = outils
    r = requests.post(config["url"], headers=config["entetes"], json=corps, timeout=600)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]


def repondre(config, niveau, demander, etapes_max=8):
    messages = []
    if niveau == 2:
        messages.append({"role": "system", "content": contexte()})
    messages.append({"role": "user", "content": QUESTION})
    outils = [OUTIL_PYTHON] if niveau >= 1 else None

    for etape in range(1, etapes_max + 1):                              # LA BOUCLE
        message = appeler(config, messages, outils)
        messages.append({"role": "assistant", "content": message.get("content") or "",
                         **({"tool_calls": message["tool_calls"]} if message.get("tool_calls") else {})})

        if not message.get("tool_calls"):                               # ARRÊT : il a répondu
            print(f"\n  [étape {etape}] RÉPONSE : {message.get('content', '').strip()}")
            return

        for appel in message["tool_calls"]:                             # LES OUTILS
            code = json.loads(appel["function"]["arguments"]).get("code", "")
            print(f"\n  [étape {etape}] le modèle DEMANDE d'exécuter :")
            print("    " + code.strip().replace("\n", "\n    "))
            if demander and input("  -> Autoriser ? (o/n) ").strip().lower() != "o":   # PERMISSIONS
                resultat = "Refusé par l'humain."
            else:
                resultat = executer(code)
            print("  [harness] résultat : " + resultat.replace("\n", "\n    ")[:400])
            messages.append({"role": "tool", "name": "executer_python",
                             "tool_call_id": appel["id"], "content": resultat})

    print(f"\n  ARRÊT : limite de {etapes_max} étapes atteinte sans réponse.")


def configurer(args):
    if args.local:
        return {"url": "http://localhost:11434/v1/chat/completions", "entetes": {},
                "modele": args.modele or "qwen3:8b"}
    cle = os.environ.get("MISTRAL_API_KEY")
    if not cle:
        sys.exit("Il manque la clé : définis la variable MISTRAL_API_KEY (voir en haut du fichier).")
    return {"url": "https://api.mistral.ai/v1/chat/completions",
            "entetes": {"Authorization": f"Bearer {cle}"},
            "modele": args.modele or "mistral-small-latest"}


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--niveau", type=int, choices=[0, 1, 2])
    p.add_argument("--modele")
    p.add_argument("--local", action="store_true")
    p.add_argument("--demander", action="store_true")
    args = p.parse_args()
    config = configurer(args)

    noms = ["le modèle seul", "+ un outil et une boucle", "+ du contexte et des règles"]
    print(f"QUESTION : {QUESTION}")
    for n in ([args.niveau] if args.niveau is not None else [0, 1, 2]):
        print(f"\n=== Niveau {n} ({noms[n]}) — modèle : {config['modele']}")
        repondre(config, n, args.demander)
    print("\n(La bonne réponse : 7 chats attendent, le plus âgé est Noisette, 11 ans.)")
