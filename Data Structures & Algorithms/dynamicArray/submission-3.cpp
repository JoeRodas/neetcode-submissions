class DynamicArray {
    private:
        int* array;
        int length;
        int capacity;
    
    public:
        // Constructor to initialize the dynamic array
        DynamicArray(int capacity) : capacity(capacity), length(0) {
            array = new int[capacity];
        }

        // Get value at the i-th index
        int get(int i) {
            return array[i];
        }

        // Set value n at the i-th index
        void set(int i, int n) {
            array[i] = n;
        }
        
        // Insert n in the last position of the array 
        void pushback(int n) {
            if (length == capacity) {
                resize();
            }
            array[length] = n;
            length++;
        }

        // Remove the last element in the array
        int popback() {
            if (length > 0) {
                // soft delete the last element
                length--;
            }
            return array[length];
        }

        // Resize the array
        void resize() {
            capacity *= 2;
            int* newArr = new int[capacity];
            for (int i = 0; i < length; i++) {
                newArr[i] = array[i];
            }
            delete[] array;
            array = newArr;
        }

        // Get the size of the array
        int getSize() {
            return length;
        }

        // Get the capacity of the array
        int getCapacity() {
            return capacity;
        }

};