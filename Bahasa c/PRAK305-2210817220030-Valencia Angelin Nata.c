#include <stdio.h>
int main(){
int bd,m,j,d,h;
scanf("%d", &bd);
h= (bd%(86400*30))/86400;
j= (bd%86400)/3600;
m= (bd%3600)/60;
d= (bd%60);
if (h==0){
    printf ("%02d:%02d:%02d\n\n",j,m,d);
    }
else{
    printf("%d hari %02d:%02d:%02d\n\n",h,j,m,d);
    }
}
