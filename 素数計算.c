#include <stdio.h>
#include <time.h>
int main(void) {
    clock_t begin, end;
    int num,number[500001],a,b,c,d;
    scanf("%d",&num);
    begin = clock();
    for (c = 2;c<=num;c++){
        number[c] = 1;
    }
    for (a = 2;a<=num;a++){
        for (b = a*2;b<=num;b+=a){
            number[b] = 0;
        }
    }
    end = clock();
    FILE *fp;
    fp = fopen("memo.txt", "w");
    for (d = 0;d<=num;d++){
        if (number[d]==1){
            fprintf(fp, "%d\n", d);
        }
    }
    fclose(fp);
    printf("%lf",(double)(end - begin) / CLOCKS_PER_SEC);
    return 0; 
    }