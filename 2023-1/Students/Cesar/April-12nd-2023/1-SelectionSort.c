#include <iostream>
#include <vector>

void selectionSort(std::vector<int> &arr) {
    // step 1: loop from the beginning of the array to the second to last item
    for (int currentIndex = 0; currentIndex < arr.size() - 1; currentIndex++) {
        // step 2: save a copy of the currentIndex
        int minIndex = currentIndex;
        // step 3: loop through all indexes that proceed the currentIndex
        for (int i = currentIndex + 1; i < arr.size(); i++) {
          /* step 4:  if the value of the index of the current loop is less
                      than the value of the item at minIndex, update minIndex
                      with the new lowest value index */
            if (arr[i] < arr[minIndex]) {
                // update minIndex with the new lowest value index
                minIndex = i;
            }
        }
        // step 5: if minIndex has been updated, swap the values at minIndex and currentIndex
        if (minIndex != currentIndex) {
            int temp = arr[currentIndex];
            arr[currentIndex] = arr[minIndex];
            arr[minIndex] = temp;
        }
    }
}

int main() {
    std::vector<int> arr = {12, 11, 15, 10, 9, 1, 2, 3, 13, 14, 4, 5, 6, 7, 8};
    selectionSort(arr);
    for (int i; i < arr.size(); i++) {
        std::cout << arr[i];
        if (i < arr.size() - 1) std::cout << ", ";
    }
}
