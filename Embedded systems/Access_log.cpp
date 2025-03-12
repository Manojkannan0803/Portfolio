#include <iostream>
using namespace std;

// imagine that creating a software of basic access log of building entrace
// the log should keep track of at most 256 integer IDs
// Memory resource is limited that is why 256 integer IDs could be stored

const int maxSize = 256;
int accessLog[maxSize];
int amtEntries = 0;

// Adds an entry to the log
// If the log reaches max capacity, start over-writing values from beginning
void addEntry(int entry){
    accessLog[amtEntries%maxSize] = entry;
    amtEntries++;
}

// Print out all values in our log
void printEntries(){
    cout << "Access Log Entries \n";
    for(int i=0;i<min(maxSize, amtEntries);i++){
        cout << "Entry of Index " << i << " : " << accessLog[i] << '\n';
    }
}

int main(){
    for(int i=1;i<=5;i++){
        addEntry(i);
    }
    printEntries();

    addEntry(6);
    addEntry(7);
    printEntries();
    return 0;
}