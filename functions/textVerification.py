def modifier_subtitles(texte_reference, subtitles, words_per_second=2.5):
    """
    Ajuste les sous-titres en les remplaçant par le texte de référence, en modifiant les timings si nécessaire.
    
    :param texte_reference: Texte de base (chaîne de caractères).
    :param subtitles: Liste de sous-titres [(texte, start, end)].
    :param words_per_second: Nombre moyen de mots prononcés par seconde.
    :return: Liste de sous-titres modifiés.
    """

    # 🔴 Étape 1 : Charger le texte de référence et le diviser en mots
    texte_reference = texte_reference.strip().split()  # Liste des mots
    index = 0
    nouveaux_sous_titres = []

    # 🔵 Étape 2 : Remplacer les sous-titres en adaptant le timing
    for i, (text, start, end) in enumerate(subtitles):
        mots_detectes = text.split()
        nb_mots_detectes = len(mots_detectes)

        # Récupérer le bon nombre de mots du texte de référence
        mots_a_prendre = texte_reference[index:index + nb_mots_detectes]

        # Si le texte de référence contient plus de mots, ajuster le timing
        if len(mots_a_prendre) > nb_mots_detectes:
            extra_mots = len(mots_a_prendre) - nb_mots_detectes
            extra_time = extra_mots / words_per_second  # Temps additionnel

            # Ajuster la fin du sous-titre
            end += extra_time  

            # Si ce n'est pas le dernier sous-titre, ajuster le suivant pour éviter un chevauchement
            if i < len(subtitles) - 1:
                next_start, next_end = subtitles[i + 1][1], subtitles[i + 1][2]
                shift = end - subtitles[i][2]  # Décalage à appliquer

                # Décaler le sous-titre suivant pour éviter un chevauchement
                subtitles[i + 1] = (subtitles[i + 1][0], next_start + shift, next_end + shift)

        # Création du nouveau sous-titre avec le texte ajusté
        nouveau_texte = " ".join(mots_a_prendre) if mots_a_prendre else text
        nouveaux_sous_titres.append((nouveau_texte, start, end))

        # Mise à jour de l’index
        index += len(mots_a_prendre)

    return nouveaux_sous_titres  # Retourne la liste modifiée
