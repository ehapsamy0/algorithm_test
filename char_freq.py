class CharFreq:
    def __init__(self, message) -> None:
        self.message = message

    def ASCII_method(self):
        print("Start ASCII Method")
        freq = [0] * 127
        for char in self.message:
            freq[ord(char)] += 1

        for index, count in enumerate(freq):
            if count > 0:
                print(f"{chr(index)} {count}")
        print("End ASCII Method")

    def any_code(self):
        print("Start Any Code Method")
        freq = {}
        for char in self.message:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        for char, count in freq.items():
            print(f"{char} {count}")
        self.sort_dec(freq)
        return freq

    def sort_dec(self, dic):
        freq_arr = [[ord(k), v] for k, v in dic.items()]  # Initialize array correctly
        self.sort(freq_arr, 0, len(freq_arr) - 1)
        for item in freq_arr:
            print(f"{chr(item[0])} {item[1]}")

    def sort(self, array, start, end):
        if start < end:
            mid = (start + end) // 2
            self.sort(array, start, mid)
            self.sort(array, mid + 1, end)
            self.merge_(array, start, mid, end)

    def merge_(self, array, start, mid, end):
        left_array = array[start:mid + 1]
        right_array = array[mid + 1:end + 1]

        i = j = 0
        k = start
        while i < len(left_array) and j < len(right_array):
            if left_array[i][1] <= right_array[j][1]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1

        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1

msg = "The output from Huffman's algorithm can be viewed as a variable length code table for encoding a source symbol. The algorithm derives this table from the estimated probability or frequency of occurrence for each possible value of the source symbol. as in other entropy encoding methods, more common symbols are generally represented using fewer bits than less common symbols. Huffman's method can be efficiently implemented, finding a code in time linear to the number of input weights if these weights are sorted. However, although optimal among methods encoding symbols separately, Huffman coding is not always optimal among all compression methods it is replaced with arithmetic coding or asymmetric numeral systems if better compression ratio is required."
message_freq = CharFreq(msg)
message_freq.any_code()
