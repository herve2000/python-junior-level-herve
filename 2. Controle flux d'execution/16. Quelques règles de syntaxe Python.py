# Tout ce qui précède nous amène à faire le point sur quelques règles de syntaxe :

# 1. Les limites des instructions et des blocs sont définies par la mise en page

# Dans de nombreux langages de programmation, il faut terminer chaque ligne d ’instructions par un
# caractère spécial (souvent le point-virgule). Sous Python, c ’est le caractère de fin de ligne
# qui joue ce rôle. (Nous verrons plus loin comment outre passer cette règle pour étendre une instruction complexe
# sur plusieurs lignes.) On peut également terminer une ligne d ’instructions par un commentaire. Un
# commentaire  Python commence toujours par le caractère spécial  #. Tout ce qui est inclus entre ce
# caractère et le saut à la ligne suivant est complètement ignoré par le compilateur.

# Dans  la  plupart  des  autres  langages,  un  bloc  d’instructions  doit  être  délimité  par  des  symboles
# spécifiques (parfois même par des instructions, telles que begin et end). En C++ et en Java, par exemple,
# un bloc d’instructions doit être délimité par des accolades. Cela permet d ’écrire les blocs d’instructions
# les uns à la suite des autres, sans se préoccuper ni d ’indentation ni de sauts à la ligne, mais cela peut
# conduire à  l’écriture de programmes confus, difficiles à relire pour les pauvres humains que nous
# sommes.
#
# On conseille donc à tous les programmeurs qui utilisent ces langages de se servir  aussi des
# sauts à la ligne et de l’indentation pour bien délimiter visuellement les blocs.

# Avec Python, vous devez utiliser les sauts à la ligne et l’indentation, mais en contrepartie vous n ’avez
# pas à vous préoccuper d’autres symboles délimiteurs de blocs. En définitive, Python vous force donc à
# écrire du code lisible, et à prendre de bonnes habitudes que vous conserverez lorsque vous utiliserez
# d’autres langages.

# 2. Les espaces et les commentaires sont normalement ignorés
# À  part  ceux  qui  servent  à  l’indentation,  en  début  de  ligne,  les  espaces  placés  à  l ’intérieur  des
# instructions et des expressions sont presque toujours ignorés (sauf s ’ils font partie d’une chaîne de
# caractères). Il en va de même pour les commentaires  : ceux-ci commencent toujours par un caractère
# dièse (#) et s’étendent jusqu’à la fin de la ligne courante.
