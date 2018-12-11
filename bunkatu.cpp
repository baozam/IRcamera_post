#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include <sys/stat.h>

using namespace std;

int main(){
    char FileName1[200],FileName2[200],outname[200],folder[200];
    int FileName0;
    char para;
    char posi;
    cout<<"run number"<<endl;
    cout<<"RUN:";
    cin>>FileName0;
    cout<<"I or R"<<endl;
    cout<<"IR:";
    cin>>para;
    cout<<"A or B"<<endl;
    cout<<"AB:";
    cin>>posi;
    sprintf(FileName2,"./RAW_data/%d/%c%d%cZM.csv",FileName0,para,FileName0,posi);
    sprintf(FileName1,"%c%d%cZM",para,FileName0,posi);
    cout<<"run num  : "<<FileName0<<endl;
    cout<<"input    : "<<FileName2<<endl;
    cout<<"================================================"<<endl;
    sprintf(folder,"./RAW_data/%d/%cdata",FileName0,para);
    if (mkdir(folder,S_IRWXU|S_IRGRP|S_IXGRP) == 0){
        printf("Success ! create output folder = %s\n", folder);
	}else{
    	printf("Exist or Failure ! cannot create output folder = %s \n", folder);
	}
    cout<<"================================================"<<endl;
    FILE *fin;
    FILE *fout;
    int i=1;
    int a=1;
    char buff[5096]={'\0'};
    fin=fopen(FileName2,"r");
    while(fgets(buff,sizeof(buff),fin)!=NULL){
        if(i==1){
            sprintf(outname,"%s/%sf%dD.csv",folder,FileName1,a);
            cout<<"output   : "<<outname<<endl;
            fout=fopen(outname,"w");
        }
        if(i==240){
            i=0;
            cout<<"file     = "<<a<<endl;
            a++;
            fclose(fout);
        }
        fprintf(fout,"%s",buff);
        i++;
        *buff='\0';
    }
    fclose(fout);
    fclose(fin);
    return 0;
}