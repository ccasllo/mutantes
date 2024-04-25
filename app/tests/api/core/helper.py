def isMutant(dna):
    n = len(dna)

    # Verificar secuencias horizontales y verticales
    for i in range(n):
        # Verificar filas
        if any(dna[i][j] == dna[i][j+1] == dna[i][j+2] == dna[i][j+3] for j in range(n-3)):
            return True

        # Verificar columnas
        if any(dna[j][i] == dna[j+1][i] == dna[j+2][i] == dna[j+3][i] for j in range(n-3)):
            return True

    # Verificar secuencias diagonales (de izquierda a derecha y de derecha a izquierda)
    for i in range(n-3):
        for j in range(n-3):
            # Diagonal de izquierda a derecha (\)
            if dna[i][j] == dna[i+1][j+1] == dna[i+2][j+2] == dna[i+3][j+3]:
                return True
            # Diagonal de derecha a izquierda (/)
            if dna[i][j+3] == dna[i+1][j+2] == dna[i+2][j+1] == dna[i+3][j]:
                return True

    # Si no se encontraron secuencias mutantes
    return False
