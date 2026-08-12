import java.util.Random;

public class Cine {
    public static void main(String[] args) {
        int TAM = 10;

        int arreglo[] = new int[TAM];

        Random rand = new Random();
        for(int i = 0; i < TAM; i++){
            arreglo[i]=rand.nextInt(2);
        }
        imprimpirValores(arreglo);

        for (int i=0; i < arreglo.length; i++) {
            if (arreglo[i] ==0 ) {
                System.out.println("El primer asiento vacio es: " + (i + 1));

                arreglo[i] = 1;

                break;
            }
        }
    }

    public static void imprimpirValores( int arreglo[]){
        for(int i=0; i < arreglo.length; i++)
            System.out.print(arreglo[i]+",");
        System.out.println();
    }
}
