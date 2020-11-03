public class Counting {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String [] entrada = sc.nextLine().split(" ");

        int [] sequencia = new int[entrada.length];
        for (int i = 0; i < entrada.length; i++){
            sequencia[i] = Integer.parseInt(entrada[i]);
        }
        int maior = sc.nextInt();

        countingSort(sequencia,maior);
    }

    private static void countingSort(int[] sequencia, int maior) {
        int[] contagem = new int[maior + 1];


        for (int i = 0; i < sequencia.length; i++){
            contagem[sequencia[i]] += 1;
            System.out.println(imprimeArray(contagem));
        }

        for (int j = 1; j < contagem.length; j++){
            contagem[j] += contagem[j-1];
        }
        System.out.println("Cumulativa do vetor de contagem - " + imprimeArray(contagem));

        int [] aux = new int[sequencia.length];
        for (int k = sequencia.length-1; k >= 0; k--){
            aux[contagem[sequencia[k]] - 1] = sequencia[k];
            contagem[sequencia[k]] -= 1;
        }

        System.out.println(imprimeArray(contagem));
        System.out.println(imprimeArray(aux));
    }

    private static String imprimeArray(int[] array) {
        String result = "";
        for (int i = 0; i < array.length; i++){
            result += array[i] + " ";
        }
        return result.substring(0, result.length()-1);
    }


}
