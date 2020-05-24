#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


class Person {
    public:
    static int id;
    static int cur_id;
    int ids[1];
    int cur_ids[1];

    int age;
    string name;
    virtual void getdata(){};
    virtual void putdata(){};
};

int Person::id = 1;
int Person::cur_id = 1;
class Professor:public Person {
    public:
    int publications;
    void getdata() {
        cin >> name >> age >> publications;
        cur_ids[0] = cur_id;
        cur_id++;
    }

    void putdata() {
        cout << name << ' ' << age << ' ' << publications << ' ' << cur_ids[0] << endl;
    }
    
};

class Student:public Person {
    public:
    int marks[6];
    void getdata() {
        cin >> name >> age;
        for(int i = 0; i < 6; i++)
            cin >> marks[i];
            ids[0] = id;
            id++;
    }

    void putdata() {
        int sumi = 0;
        for(int i = 0; i < 6; i++)
        sumi += marks[i];
        cout << name << ' ' << age << ' ' << sumi << ' ' << ids[0] << endl;
    }
};

int main(){

    int n, val;
    cin>>n; //The number of objects that is going to be created.
    Person *per[n];

    for(int i = 0;i < n;i++){

        cin>>val;
        if(val == 1){
            // If val is 1 current object is of type Professor
            per[i] = new Professor;

        }
        else per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.

    }

    for(int i=0;i<n;i++)
        per[i]->putdata(); // Print the required output for each object.

    return 0;

}
