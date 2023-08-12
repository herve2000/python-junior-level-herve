# Lorsqu’il y a plus d’un opérateur dans une expression, l’ordre dans lequel les opérations doivent être
# effectuées dépend de règles de priorité. Sous Python, les règles de priorité sont les mêmes que celles qui
# vous ont été enseignées au cours de mathématique. Vous pouvez les mémoriser aisément à l ’aide d’un
# « truc » mnémotechnique, l’acronyme PEMDAS :

# • P pour parenthèses. Ce sont elles qui ont la plus haute priorité.
# Elles vous permettent donc de «  forcer » l’évaluation d’une expression dans l’ordre que vous voulez.
# Ainsi 2*(3-1) = 4, et (1+1)**(5-2) = 8.
# <<Exemple 1>>

# • E pour exposants. Les exposants sont évalués ensuite, avant les autres opérations.
# Ainsi 2**1+1 = 3(et non 4), et 3*1**10 = 3(et non 59049 !).
# <<Exemple 2>>

# • M et D pour multiplication et division, qui ont la même priorité.
# Elles sont évaluées avant  l’addition A et la soustraction S, lesquelles sont donc effectuées en dernier lieu.
# Ainsi 2*3-1 = 5(plutôt que 4), et 2/3-1 = -0.3333...(plutôt que 1.0).
# <<Exemple 3>>

# • Si deux opérateurs ont la même priorité, l’évaluation est effectuée de gauche à droite.
# Ainsi dans l’expression 59*100//60, la multiplication est effectuée en premier, et la machine doit
# donc  ensuite effectuer 5900//60, ce qui donne  98. Si la division était effectuée en premier, le
# résultat serait 59 (rappelez-vous ici que l’opérateur // effectue une division entière, et vérifiez en
# effectuant 59*(100//60))
# <<Exemple 4>>

if __name__ == '__main__':
    # <<Exemple 1>>
    print(f"2*(3-1) est egale a {2 * (3 - 1)}")
    print(f"(1+1)**(5-2) est egale a {(1 + 1) ** (5 - 2)}")  # 2**3

    # <<Exemple 2>>
    # print(f"2**1+1 est egale a {2 ** 1 + 1}")
    # print(f"3*1**10 est egale a {3*1**10}")

    # <<Exemple 3>>
    # print(f"2*3-1 est egale a {2 * 3 - 1}")
    # print(f"2/3-1 est egale a {2/3-1}")

    # <<Exemple 4>>
    # print(100//60)
    # print(f"59*100//60 est egale a {59 * 100 // 60}")
    # print(f"59*(100//60) est egale a {59*(100//60)}")
