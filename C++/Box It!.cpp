#include<bits/stdc++.h>

using namespace std;

//Overload operator < as specified
//bool operator<(Box& b)

//Overload operator << as specified
//ostream& operator<<(ostream& out, Box& B)

class Box {
    public:
    int l, b, h;
    Box() {
        l = 0;
        b = 0;
        h = 0;
    }

    Box(int a, int x, int c) {
        l = a;
        b = x;
        h = c;
    }

    Box(const Box& a) {
        l = a.l;
        b = a.b;
        h = a.h;
    }

    int getLength() {
        return l;
    }

    int getBreadth() {
        return b;
    }

    int getHeight() {
        return h;
    }

    long long CalculateVolume() {
        return (long long)l * b * h;
    }

    friend bool operator< (Box&a, Box& B) {
        if((a.h < B.h) && (a.b == B.b) && (a.l == B.l) || 
        (a.b < B.b) and (a.l == B.l) || 
        (a.l < B.l))
            return true;
        else
            return false;
    }

    friend ostream& operator<< (ostream& qw, Box& B) {
        qw << B.l << ' ' << B.b << ' ' << B.h;
        return qw;
    }
};


void check2()
{
	int n;
	cin>>n;
	Box temp;
	for(int i=0;i<n;i++)
	{
		int type;
		cin>>type;
		if(type ==1)
		{
			cout<<temp<<endl;
		}
		if(type == 2)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			temp=NewBox;
			cout<<temp<<endl;
		}
		if(type==3)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			if(NewBox<temp)
			{
				cout<<"Lesser\n";
			}
			else
			{
				cout<<"Greater\n";
			}
		}
		if(type==4)
		{
			cout<<temp.CalculateVolume()<<endl;
		}
		if(type==5)
		{
			Box NewBox(temp);
			cout<<NewBox<<endl;
		}

	}
}

int main()
{
	check2();
}
