#include <stdio.h>

int main() {
    int numero;

    printf("Introduce un numero: ");
    scanf("%d", &numero);

    if (numero > 0) {
        printf("El numero es positivo.\n");
    } else if (numero < 0) {
        printf("El numero es negativo.\n");
    } else {
        printf("El numero es cero.\n");
    }

    return 0;
}
##En c estas llamando una libreria, declaras el numero como variable 
## e indicas que que cierre el programa y en Phyton no tienes que hhacer nada de eso 