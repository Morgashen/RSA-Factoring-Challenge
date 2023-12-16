#include <stdio.h>  
#include <math.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {


  if(argc < 2) {
    printf("Usage: factorize number\n"); 
    return 1;
  }


  long long num = atoll(argv[1]);  


  if(num <= 0) {
    printf("Error: Please enter a positive number\n");
    return 1;
  }

  long long limit = sqrt(num);


  long factor1;
  for(factor1 = 2; factor1 <= limit; factor1++) { 
    if(num % factor1 == 0)
      break;
  }
  

  if (factor1 > limit) {
    printf("%lld is a prime number\n", num);  
  }
  else {
    long long factor2 = num / factor1;
    FILE *fp = fopen("factors.txt","w");
    fprintf(fp, "%lld = %lld * %ld\n", num, factor2, factor1);  
    printf("Factors written to factors.txt\n");
    fclose(fp);
  }

  return 0;
}
