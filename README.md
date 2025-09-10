# Create a README.md file for the user's project
readme_content = r"""# buildllm — Agent CLI IA (type **Claude Code**) avec Google **Gemini** (gratuit)

> Un petit agent “dev-copilote” en **ligne de commande** qui lit/écrit des fichiers, exécute du Python, et itère jusqu’à résoudre une tâche de code — en s’appuyant sur l’API **Gemini** (clé gratuite). Idéal pour comprendre **comment fonctionnent vraiment** les outils d’IA “agentiques”.

---

## 🚀 TL;DR
- **Ce que c’est :** un **agent CLI** inspiré de Cursor / Claude Code, propulsé par **Google Gemini**.  
- **Ce que ça fait :**
  - Accepte une **tâche de codage** en texte libre.
  - Choisit des **fonctions/outils** pour lire/écrire/exécuter du code.
  - **Boucle** (plan → action → observation) jusqu’à réussir… ou échouer proprement.
- **Stack :** Python **3.10+**, gestionnaire **uv**, shell Unix (zsh/bash).

---

## 🧠 Contexte & objectifs
Ce dépôt accompagne un projet **Boot.dev** : profiter du momentum autour de l’IA pour **construire un agent from scratch** (sans réinventer un LLM).  
**Objectifs d’apprentissage :**
- S’initier aux projets Python **multi-répertoires** et à la programmation **fonctionnelle**.
- Comprendre **les briques réelles** derrière les éditeurs IA “agentiques” utilisés en entreprise.
- Pratiquer l’intégration d’un **LLM pré-entraîné** (Gemini) pour bâtir un **agent** simple et utile.

> ⚠️ Nous **n’entraînons pas** de LLM : on **orchestra** un LLM existant pour résoudre des tâches de dev.

---

## ✨ Fonctionnalités clés
- **Input libre** : “Fixe ma calculatrice”, “Ajoute des logs”, “Refactorise `utils.py`”…
- **Outils intégrés (fonction-calling)** :
  - `get_files_info` — lister les fichiers d’un répertoire cible
  - `get_file_content` — lire un fichier
  - `write_file` — écraser/écrire un fichier
  - `run_python_file` — exécuter un script Python et récupérer la sortie
- **Boucle d’itération** : planifier → appeler un outil → observer → décider de la suite.
- **Traçabilité** : logs lisibles des actions choisies par l’agent.

---

## 🖥️ Exemple d’utilisation (réel)
```bash
uv run main.py "fix my calculator app, its not starting correctly"
# Calling function: get_files_info
# Calling function: get_file_content
# Calling function: write_file
# Calling function: run_python_file
# Calling function: write_file
# Calling function: run_python_file
# Final response:
# Great! The calculator app now seems to be working correctly. The output shows
# the expression and the result in a formatted way.
