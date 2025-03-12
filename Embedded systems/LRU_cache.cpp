#include <iostream>
#include <list>
#include <unordered_map>

using namespace std;

struct LRU {
    const int maxCapacity = 1000; // max. capacity of elements that our cache can hold
    int currentCount = 0; // count of elements currently stored in the LRU
    unordered_map<int, int> valueMap; // an unordered map that will hold key value pairs
    list<int> keys; // implemented using a w link list in C++; used to maintain the sequence of keys entered into LRU
    unordered_map<int, list<int>::iterator> iteratorMap; // keeping track of the position of each key will help us update the key position when they are accessed

    // returns value associated with given key of present
    // inputs: key - key to query and value - used to store associated value for this scheme
    bool getEntry(int key, int &value) {
        if (valueMap.find(key) != valueMap.end()){
            keys.erase(iteratorMap[key]);
            keys.push_front(key);
            iteratorMap[key] = keys.begin();
            value = valueMap[key];
            return true;
        }
        else{
            return false;
        }
    }

    //inserts a key-value pair into our LRU
    void insertPair(int key, int value) {
        if(valueMap.find(key) != valueMap.end()){
            keys.erase(iteratorMap[key]);
            keys.push_front(key);
            iteratorMap[key] = keys.begin();
            valueMap[key] = value;
        }
        else {
            if(currentCount>= maxCapacity){
                int LRUKey = keys.back();
                valueMap.erase(LRUKey);
                iteratorMap.erase(LRUKey);
                keys.pop_back();
                currentCount--;
            }
            valueMap[key] = value;
            keys.push_front(key);
            iteratorMap[key] = keys.begin();
            currentCount++;
        }
    }
};