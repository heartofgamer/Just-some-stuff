#include<iostream>
#include<conio.h>
#include<iomanip>
#include<string.h>
#include<stdio.h>
#include<ctype.h>
#include<stdlib.h>
using namespace std;
char name[31],city[16],date[10];
int lcounter=0,lcount=2,qcounter=10,amt=0;
char *ques(int,int);
char *queans(int);
char *amount(int);
void pinfo();
void rules();
void lifelines(char,int);
int *order();
void victory();
void lose(int);
void kbcgame();
void quitgame(char,int);
void winmoney();
void kbc()
{   cout<<"\n"<<setw(51)<<"KAUN BANEGA CROREPATI\n\n";
}
char *amount(int at)
{	switch(at)
	{    case 0: return "0";
	     case 1: return "20,000";
	     case 2: return "40,000";
	     case 3: return "80,000";
	     case 4: return "1,60,000";
	     case 5: return "3,20,000";
	     case 6: return "6,40,000";
	     case 7: return "12,50,000";
	     case 8: return "25,00,000";
	     case 9: return "50,00,000";
	     case 10: return "1 Crore";
	     default: return NULL;
	}
}
char *queans(int quesno)
{       switch(quesno)
	{    case 1:return "3:2";
	     case 2:return "Crust";
	     case 3:return "Pandit Nehru";
	     case 4:return "Bachendri Pal";
	     case 5:return "World War 2";
	     case 6:return "China";
	     case 7:return "Chikan Garments";
	     case 8:return "Aurangzeb";
	     case 9:return "Stonehenge";
	     case 10:return "Koala";
	     case 11:return "Samudragupta";
	     case 12:return "Nicole Faria";
	     case 13:return "Sarojini Naidu";
	     case 14:return "Saffron";
	    case 15:return "John Adams";
	    case 16:return "Stroma";
	    default: return NULL;
	 }
}
char *ques(int qno,int pos)
{   switch(qno)
   {	case 1:
	char *q1[]={"The Ratio of dimensions of Indian Flag is","3:2","3:1","5:1","4:3"};
	return *(q1+pos);
	case 2:
	char *q2[]={"Which is the thinnest layer on earth","Crust","Stratosphere","Atmosphere","Lithosphere","Exosphere"};
	return *(q2+pos);
	case 3:
	char *q3[]={"Who wrote the book 'The Discovery of India","Pandit Nehru","Mahatma Gandhi","Saradar Vallabhai Patel","Netaji Bose"};
	return *(q3+pos);
	case 4:
	char *q4[]={"Who was the first Indian Woman to scale Mount Everst","Bachendri Pal","Arunima Sinha","Nahida Fazoor","PT Usha"};
	return *(q4+pos);
	case 5:
	char *q5[]={"Which war took place during 1939-1946","7 Years War","World War 2","World War 1","Cold War"};
	return *(q5+pos);
	case 6:
	char *q6[]={"Where was paper money first introduced","USA","India","China","England"};
	return *(q6+pos);
	case 7:
	char *q7[]={"Lucknow is famous for what all over the World","Chikan Garments","Glass","Animals","Nature"};
	return *(q7+pos);
	case 8:
	char *q8[]={"Who was the last Mughal ruler","Aurangzeb","Shah Jahan","Babur","Khilji"};
	return *(q8+pos);
	case 9:
	char *q9[]={"What is the name of the famous group of huge standing stones on a plain in   England","Stonehenge","Carnac Stones","Rollright Stones","Callanish Stones"};
	return *(q9+pos);
	case 10:
	char *q10[]={"Which animal is the teddy bear","Polar Bear","Dog","Koala","Bear"};
	return *(q10+pos);
	case 11:
	char *q11[]={"Who is known as Napolean of India","Samudragupta","Akhbar","Chandragupta","Maharana Pratap"};
	return *(q11+pos);
	case 12:
	char *q12[]={"Who is the first Indian woman to recieve Miss World","Nicole Faria","Vanessa Vonce","Manushi Chhillar","Stephanie Valle"};
	return *(q12+pos);
	case 13:
	char *q13[]={"Who was the First woman Governer of Indian","Sarojini Naidu","Lata Maheshkar","Pritabha Patel","PT Usha"};
	return *(q13+pos);
	case 14:
	char *q14[]={"Which is the world's most expensive spice","Saffron","Indigo","Tumeric","Cinnomon"};
	return *(q14+pos);
	case 15:
	char *q15[]={"Who was the first US president to stay at White House","John Adams","Abraham Lincoln","Barack Obama","George Washington"};
	return *(q15+pos);
	case 16:
	char *q16[]={"What the pore of a plant leaf called which opens and closes to let gases in   or out","Grana","Stroma","Stomata","Xylem"};
	return *(q16+pos);
	default: return NULL;
   }
}
void pinfo()
{	kbc();
	cout<<"Name:";
	gets(name);
	cout<<"\nCity Name:";
	gets(city);
	cout<<"\nToday's Date(dd/mm/yyyy):";
	gets(date);
}
void rules()
{	pinfo();
	system("cls");
	kbc();
	cout<<"So today on hot seat we have "<<name<<" who is from "<<city;
	getche();
	cout<<"\n\nNow "<<name<<" I make you known to the rules of the game--\n\n";
	cout<<setw(3)<<"1- There will be 10 questions worth of which will";
	cout<<"\n start from Rs "<<amount(1)<<" to Rs "<<amount(10)<<".\n\n";
	cout<<"\t>"<<amount(1)<<setw(17)<<"|\t>"<<amount(6);
	cout<<"\n\t>"<<amount(2)<<setw(17)<<"|\t>"<<amount(7);
	cout<<"\n\t>"<<amount(3)<<setw(17)<<"|\t>"<<amount(8);
	cout<<"\n\t>"<<amount(4)<<setw(15)<<"|\t>"<<amount(9);
	cout<<"\n\t>"<<amount(5)<<setw(15)<<"|\t>"<<amount(10)<<"\n\n";
	cout<<setw(3)<<"2- After you give right answer of the "<<qcounter/2
	<<" question"<<"\n you will surely be taking home Rs 3,20,000.\n\n";
	cout<<setw(3)<<"3- There are two life lines - DOUBLE DIP &"
	<<" FLIP THE QUESTION"<<"\n if you stuck on any question.\n\n";
	cout<<setw(3)<<"4- You can quit the game any moment you wish to.";
	getche();
}
void lifelines(char rtans,int rno)
{   char optans;
    if(lcounter==1)
    {	cout<<"you have Flip The question Life line only\n";
	goto l2;
    }
    else
	if(lcounter==2)
       {	cout<<"you have Double Dip Life line only\n";
		goto l1;
       }
    char lopt;
reenter:    cout<<"Press U for Double Dip / V for Flip the Question:";
    cin>>lopt;
    if(islower(lopt))
	lopt=toupper(lopt);
    switch(lopt)
    {	case'U':
	{     lcounter=1;
	l1:   --lcount;
	      cout<<"Input First Choice:";
 againtemp:   cin>>optans;
	      if(islower(optans))
		    optans=toupper(optans);
	      switch(optans)
	      {       case 'A':      case 'B':
		      case 'C':      case 'D':
			 if(optans==rtans)
			 {	victory();
				goto end;
			 }
			 break;
		      default:cout<<"Invalid Enter Again:";
			      goto againtemp;
	      }
	      cout<<"this is the wrong answer enter again"
		  <<"\nif you want to quit press Q, L for second lifeline"
		  <<"\nelse input second choice:";
  againtemp2: cin>>optans;
	      if(islower(optans))
		     optans=toupper(optans);
	      switch(optans)
	      {       case 'A':	      case 'B':
		      case 'C':	      case 'D':
			  if(optans==rtans)
			       victory();
			  else
			       lose(rno);
			break;
		      case 'Q': quitgame(rtans,rno);
		      case 'L': goto l2;
		      default:cout<<"Invalid Enter Again;";
			      goto againtemp2;
	      }
	}
end:	break;
	case'V':
	{    lcounter=2;
	l2:  --lcount;
	     cout<<"So Now this question will be removed"
	     <<" and a new question will be displayed."
	     <<"\nBut before changing the question we have "
	     <<"to tell our audience the correct answer,"
	     <<"\nSo if you have played which option you would have selected:";
     fret:   cin>>optans;
	     if(islower(optans))
		  optans=toupper(optans);
	     switch(optans)
	     {    case 'A':     case 'B':
		  case 'C':     case 'D':
		     if(optans==rtans)
		     {   cout<<"Oh this would have been the"
			 <<" right answer if you would have played "
			 <<"this question.\n But no regrets.";
			 getche();
		      }
		    else
		       {    cout<<"This would have been the wrong answer"
			    <<"the correct answer is:"<<queans(rno);
			    getche();
			}
		  cout<<"\nso now the new question is";
		  getche();
		  qcounter=11;
		  break;
	       default:cout<<"Invalid.Enter Again:";
			goto fret;
	     }
       }
       break;
	default: cout<<"Wrong Selection.Enter Again:";
		goto reenter;
  }
}
int *order()
{       const int len=16;
	int s,r,temp,num[len],*arr;
	for(temp=0,s=1; temp<len; s++,temp++)
	{   num[temp]=s;        }
	srand(time(NULL));
	for(s=len-1;s>0;s--)
	{	r=rand()%s;
		temp=num[s];
		num[s]=num[r];
		num[r]=temp;
	}
	for(s=0;s<len;s++)
		*(arr+s)=num[s];
	return arr;
}
void victory()
{	++amt;
	if(strcmp(amount(amt),"1 Crore")==0)
	{    cout<<"\nYou Are A Crorepati Now.";
	     cout<<"\n\nBig Round of Applause and Should Not Stop";
	     getche();
	     winmoney();
	}
	else
	{    cout<<"This is the right answer";
	     cout<<"\nYou won Rs. "<<amount(amt)<<". Applauses should not stop.";
	     getche();
	}
}
void lose(int ansno)
{   cout<<"Oh This is the wrong answer.The correct answer is "<<queans(ansno);
    if(amt>=5)
    {	amt=5;
	cout<<"\n\nUnfortunately, "<<name<<" you will be taking home only Rs."<<amount(amt);
	winmoney();
    }
    else
    {	amt=0;
	cout<<"\n\nUnfortunately, "<<name<<" you won no money so you won't get any cheque";
	cout<<"\n\nGive a big round of applause for "<<name;
	getche();
	exit(1);
    }
}
void kbcgame()
{   rules();
    int *quesord=order(),i,j,k,len;
    char opt,rtoption,*qarr[5],optarr[]={'A','B','C','D'};
    for(i=0,j=0,amt;j<qcounter;++i,++j)
    {   system("cls");
	kbc();
	for(k=0;k<5;++k)
		qarr[k]=ques(*(quesord+i),k);
	cout<<"Question for Rs. "<<amount(amt+1)<<" on your computer screen is this\n";
	getche();
	for(int k=0;k<80;++k)
		cout<<"-";
	cout<<"-> "<<qarr[0]<<" <-\n";
	for(k=0;k<80;++k)
		cout<<"-";
	cout<<"Options are as follows:\n\n";
	getche();
	cout<<"\t>(a)"<<qarr[1];
	len=strlen(qarr[1]);
	for(k=0;k<26-len;++k)
		cout<<" ";
	cout<<"|>(b)"<<qarr[2]<<"\n\t";
	for(k=0;k<63;++k)
	{	cout<<"-";
		if(k==29)
			cout<<"|";
	}
	cout<<"\n\t>(c)"<<qarr[3];
	len=strlen(qarr[3]);
	for(k=0;k<26-len;++k)
		cout<<" ";
	cout<<"|>(d)"<<qarr[4];
	for(k=1;k<=4;++k)
	{       if(strcmp(qarr[k],queans(*(quesord+i)))==0)
		{	rtoption=optarr[k-1];
			break;
		}
	}
	if(lcount==0)
	   cout<<"\n\nYou Have no lifelines.";
	else
	   cout<<"\n\nYou have "<<lcount<<" life lines,press L for lifeline.";
	cout<<"Press A/B/C/D for answer choice, press Q to quit.";
	cout<<"Input Your Option:";
again:	cin>>opt;
	if(islower(opt))
		opt=toupper(opt);
	switch(opt)
	{       case 'A':case 'B':
		case 'C':case 'D':
			if(opt==rtoption)
			    victory();
			else
			    lose(*(quesord+i));
		   break;
		case 'Q': quitgame(rtoption,*(quesord+i));
		case 'L':if(lcount!=0)
			 {    lifelines(rtoption,*(quesord+i));
			      break;
			 }
			 else goto def;
	def:	default:cout<<"Invalid Enter Again:";
			goto again;
		}
    }
}
void quitgame(char qans,int qno)
{   	cout<<"Give a big round of applause for "<<name<<" You won Rs. "<<amount(amt);
	char tempans;
	cout<<"\nbut before leaving the game we have "
	<<"to tell our audience the correct answer."
	<<"\nSo if you have played which option you would have selected:";
  qent:	cin>>tempans;
	if(islower(tempans))
	       tempans=toupper(tempans);
	switch(tempans)
	{       case 'A':     case 'B':
		case 'C':     case 'D':
	     if(tempans==qans)
	     {    cout<<"Oh this would have been the right answer"
		  <<" if you would have played this question, "
		  <<" But no regrets.\nThanks for Playing.";
		  getche();
	     }
	     else
		 {   cout<<"This would have been the wrong answer."
		     <<"\nThe correct answer is:"<<queans(qno)
		     <<"\nNo doubts now, Thanks for Playing";
		     getche();
		 }
	     break;
	       default:cout<<"Inavlid.Enter Again:";
	       goto qent;
	}
	if(amt==0)
	      cout<<"\nYou won no money so no cheque.\nThanks for playing.";
	else
	      winmoney();
}
void winmoney()
{       int a,r,x[11];
	int namelen=strlen(name), amntlen=strlen(amount(amt));
	system("cls");
	kbc();
	cout<<setw(5)<<"|";
	for(a=0;a<59;++a)
		cout<<"-";
	cout<<"|\n"<<setw(35)<<"|\t**PROJECT 12.0 BANK**\t\t\tDate-"<<date;
	//gotoxy(65,5);// this function is obselete
	cout<<"|\n"<<setw(11)<<"|\tPay__"<<name;
	for(a=0;a<32-namelen;++a)
		cout<<"_";
	cout<<"Or Bearer";
	//gotoxy(65,6);//this function is obselete
	cout<<"|\n"<<setw(14)<<"|\tRupees__"<<amount(amt);
	for(a=0;a<32-amntlen;++a)
		cout<<"_";
	//gotoxy(65,7);
	cout<<"|\n"<<setw(6)<<"|\t";
	for(a=0;a<36;++a)
		cout<<"_";
	cout<<"Rs "<<amount(amt);
	//gotoxy(65,8); this function is obselete 
	cout<<"|\n"<<setw(14)<<"|\tA/C No.-";
	srand(time(NULL));
	for(a=0;a<11;++a)
	{	r=rand()%11;
		x[a]=r;
		cout<<x[a];
	}
	//gotoxy(65,9);
	cout<<"|\n"<<setw(43)<<"|\tPayable at None branches of any bank\t";
	cout<<"sign-Group:4\t|\n"<<setw(5)<<"|";
	for(a=0;a<59;++a)
		cout<<"-";
	cout<<"|";
	getche();
	cout<<"\n\n\nCongratulations "<<name<<" For Winning Rs"<<amount(amt);
	cout<<"\n\nGOVERNMENT WILL CUT 100% GST SO, You Get this fake cheque.";
	cout<<"\n\nYou can Take Out A print Out of it and enjoy.";
	cout<<"\n\nGive a big round of applause for "<<name;
	getche();
	exit(1);
}
int main()
{       system("cls");
	kbcgame();
	return 0;
}