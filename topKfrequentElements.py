#neetcode #5

class Solution:
    def topKfrequent(self, nums, k):
        n = len(nums)
        count = {}

        for i in range(n):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1

        bucket = [[] for _ in range(0, n+1)]

        for num, freq in count.items():
            bucket[freq].append(num)

        result = []

        for i in reversed(range(0, n+1)):
            for num in bucket[i]:
                result.append(num)

            if len(result) == k:
                return result


if __name__ == "__main__":
    nums = [1,2,2,3,3,3]
    sol = Solution()
    k = 2
    answer = sol.topKfrequent(nums,k)
    print(answer)

    # Let's go step by step and break down the code **in layman's terms**, explaining each part with an example. We will also walk through the code **line by line** using an example to see how the values change as the program runs.

    # ---

    # ### **Problem Statement (Simple Explanation)**
    # We are given a list of numbers and a number `k`. Our goal is to find the `k` most frequent numbers in the list.

    # ---

    # ### **Example**
    # #### **Input:**
    # ```python
    # nums = [1, 2, 2, 3, 3, 3]
    # k = 2
    # ```
    # #### **Expected Output:**
    # ```python
    # [3, 2]
    # ```
    # Why?
    # - `3` appears **3 times** (most frequent).
    # - `2` appears **2 times** (second most frequent).
    # - `1` appears **1 time** (least frequent).
    # - Since `k = 2`, we return the **top 2** frequent numbers → `[3, 2]`.

    # ---

    # ## **Step-by-Step Code Breakdown with Execution**

    # ---

    # ### **Code:**
    # ```python
    # class Solution:
    #     def topKFrequent(self, nums, k):
    # ```
    # ✅ **Step 1: Function Definition**
    # - We define a function `topKFrequent` that takes **a list of numbers (`nums`)** and **an integer `k`**.
    # - The function will return the `k` most frequent numbers.

    # ---

    # ```python
    #         n = len(nums)  # Get the length of nums
    # ```
    # ✅ **Step 2: Get the Length of `nums`**
    # - `n = len(nums)` calculates the total number of elements in `nums`.

    # 🔹 **For our example:**
    # ```python
    # n = len([1, 2, 2, 3, 3, 3])  # n = 6
    # ```

    # ---

    # ```python
    #         count = {}  # Dictionary to store frequency of each number
    # ```
    # ✅ **Step 3: Create a Dictionary for Counting**
    # - We create an **empty dictionary** (`count`) that will store **each number as a key** and **how many times it appears as a value**.

    # ---

    # ### **Counting Occurrences**
    # ```python
    #         for i in range(n):
    #             if nums[i] in count:
    #                 count[nums[i]] += 1  # Increment count
    #             else:
    #                 count[nums[i]] = 1  # Initialize count
    # ```
    # ✅ **Step 4: Count the Frequency of Each Number**
    # - We loop through `nums` and count how many times each number appears.

    # 🔹 **For our example:**
    # | Iteration | `nums[i]` | `count` Dictionary |
    # |-----------|----------|---------------------|
    # | 1st (`i=0`) | `1` | `{1: 1}` |
    # | 2nd (`i=1`) | `2` | `{1: 1, 2: 1}` |
    # | 3rd (`i=2`) | `2` | `{1: 1, 2: 2}` |
    # | 4th (`i=3`) | `3` | `{1: 1, 2: 2, 3: 1}` |
    # | 5th (`i=4`) | `3` | `{1: 1, 2: 2, 3: 2}` |
    # | 6th (`i=5`) | `3` | `{1: 1, 2: 2, 3: 3}` |

    # 🔹 **Final `count` dictionary:**
    # ```python
    # {1: 1, 2: 2, 3: 3}
    # ```

    # ---

    # ### **Creating Buckets**
    # ```python
    #         bucket = [[] for _ in range(n + 1)]  # Index represents frequency
    # ```
    # ✅ **Step 5: Create Buckets**
    # - We create **a list of empty lists** (`bucket`) where **index = frequency**.
    # - Since the highest possible frequency is `n`, we make `n+1` empty lists.

    # 🔹 **For our example (`n = 6`)**:
    # ```python
    # bucket = [[], [], [], [], [], [], []]  # 7 empty lists (indices 0 to 6)
    # ```

    # ---

    # ### **Placing Numbers into Buckets**
    # ```python
    #         for num, freq in count.items():
    #             bucket[freq].append(num)  # Add numbers to their frequency index
    # ```
    # ✅ **Step 6: Place Each Number into the Correct Bucket**
    # - We **go through our `count` dictionary** and put each number into the list at **its frequency index**.

    # 🔹 **For our example (`count = {1: 1, 2: 2, 3: 3}`):**
    # | Number | Frequency | Placed in `bucket` at Index |
    # |--------|----------|----------------------|
    # | `1`    | `1`      | `bucket[1] = [1]`   |
    # | `2`    | `2`      | `bucket[2] = [2]`   |
    # | `3`    | `3`      | `bucket[3] = [3]`   |

    # 🔹 **Final `bucket` list:**
    # ```python
    # bucket = [[], [1], [2], [3], [], [], []]
    # ```
    # - **Index = Frequency**
    # - **Numbers are grouped by how many times they appear**

    # ---

    # ### **Selecting Top K Elements**
    # ```python
    #         result = []
    # ```
    # ✅ **Step 7: Create an Empty List to Store Result**

    # ---

    # ```python
    #         for i in reversed(range(n + 1)):  # Start from highest possible frequency
    # ```
    # ✅ **Step 8: Loop from the Highest Frequency**
    # - We start **from the end of the `bucket` list** (where the most frequent numbers are).

    # 🔹 **For our example (`bucket = [[], [1], [2], [3], [], [], []]`):**
    # ```python
    # for i in [6, 5, 4, 3, 2, 1, 0]:  # Loop from highest frequency
    # ```

    # ---

    # ```python
    #             for num in bucket[i]:
    #                 result.append(num)
    #                 if len(result) == k:  # Stop when we collect k elements
    #                     return result
    # ```
    # ✅ **Step 9: Pick the Top K Elements**
    # - **Loop through the numbers in the current `bucket[i]`** and **add them to `result`**.
    # - **If `result` has `k` elements, return it immediately**.

    # 🔹 **For our example (`k = 2`)**:
    # 1. **Start at `bucket[6]`** → `empty`
    # 2. **Go to `bucket[5]`** → `empty`
    # 3. **Go to `bucket[4]`** → `empty`
    # 4. **Go to `bucket[3]`** → contains `[3]`, so `result = [3]`
    # 5. **Go to `bucket[2]`** → contains `[2]`, so `result = [3, 2]`
    # 6. **`len(result) == k`, return `[3, 2]`**

    # ---

    # ### **Final Output**
    # ```python
    # [3, 2]
    # ```

    # ---

    # ## **🔹 Final Summary**
    # 1. **Count** how many times each number appears (**O(N)**).
    # 2. **Use buckets** to group numbers by frequency (**O(N)**).
    # 3. **Select the top K elements** from the highest frequency (**O(N)**).
    # 4. **Return the result in O(N) time, avoiding sorting (O(N log N))**.

    # ### **🚀 Time Complexity: O(N)**
    # - Counting numbers: **O(N)**
    # - Creating buckets: **O(N)**
    # - Picking `k` elements: **O(N)**

    # **Total: O(N)** → **Much better than sorting!** 🔥

    # ---

    # ### **Final Thoughts**
    # - ✅ **Fastest approach using bucket sort**
    # - ✅ **Avoids unnecessary sorting (O(N log N))**
    # - ✅ **Easy to understand & implement**

    # Hope this explanation makes it super clear!

    # ### **❓ Why are we using `num` instead of `i` in this line?**
    # ```python
    # for num in bucket[i]:
    #     result.append(num)
    # ```
    # - **`num` represents the actual numbers** from the input list (`nums`) that appear `i` times.
    # - **`i` is just an index** representing the frequency level.

    # ---

    # ### **🔹 What Happens If You Use `i` Instead of `num`?**
    # If you mistakenly write:
    # ```python
    # for i in bucket[i]:  # ❌ Incorrect
    #     result.append(i)
    # ```
    # You'll get an **error** because `bucket[i]` is a **list of numbers**, and `i` is just an index.

    # ---

    # ### **🔹 Let's Walk Through an Example**
    # #### **Input:**
    # ```python
    # nums = [1, 2, 2, 3, 3, 3]
    # k = 2
    # ```
    # #### **Step 1: Frequency Count**
    # ```python
    # count = {1: 1, 2: 2, 3: 3}
    # ```

    # #### **Step 2: Bucket Creation**
    # ```python
    # bucket = [[], [1], [2], [3], [], [], []]
    # ```
    # - `bucket[1] = [1]` → The number `1` appears **1 time**.
    # - `bucket[2] = [2]` → The number `2` appears **2 times**.
    # - `bucket[3] = [3]` → The number `3` appears **3 times**.

    # ---

    # #### **Step 3: Picking Top K Frequent Elements**
    # We loop **backward** from the highest frequency (`i`).

    # ```python
    # for i in reversed(range(n + 1)):  # i goes from 6 to 0
    #     for num in bucket[i]:  # Loop through numbers stored at this frequency
    #         result.append(num)
    #         if len(result) == k:
    #             return result
    # ```

    # **Looping through the `bucket` list:**
    # | `i` (frequency) | `bucket[i]` | Numbers Added to `result` |
    # |---------------|------------|------------------|
    # | `6`           | `[]`        | `[]` |
    # | `5`           | `[]`        | `[]` |
    # | `4`           | `[]`        | `[]` |
    # | `3`           | `[3]`       | `[3]` |
    # | `2`           | `[2]`       | `[3, 2]` (Stops here, since `k=2`) |

    # ✅ **Final Output: `[3, 2]`**

    # ---

    # ### **🔴 What If You Use `i` Instead of `num`?**
    # If you mistakenly write:
    # ```python
    # for i in bucket[i]:  # ❌ Incorrect
    #     result.append(i)
    # ```
    # Let's say `i = 3`, then `bucket[i] = [3]`. Now, `for i in bucket[i]:` is like saying:
    # ```python
    # for i in [3]:  # ❌ Now i is 3, but we needed the number stored in bucket[3]
    #     result.append(i)
    # ```
    # This **overwrites** `i` inside the loop, and it no longer refers to the frequency index.

    # 🔴 **Error:**
    # - If `bucket[i]` is empty (`[]`), it will crash.
    # - If `bucket[i]` contains `[3]`, then `i` will mistakenly become `3` again inside the loop, breaking the logic.

    # ---

    # ### **✅ Correct Usage**
    # ```python
    # for num in bucket[i]:  # ✅ Correct
    #     result.append(num)
    # ```
    # Here, `num` is the actual **number from `nums`**, **not the frequency index**.

    # ---

    # ### **🔹 Final Answer**
    # We **must** use `num` inside `for num in bucket[i]:` because:
    # 1. `bucket[i]` contains **numbers grouped by frequency**.
    # 2. `i` represents the **frequency index**, not the actual numbers.
    # 3. If we use `i`, it will break the loop logic.

    # ---

    # ### **🔥 Key Takeaway**
    # Use `num`, **not** `i`, because `bucket[i]` stores **numbers that appeared `i` times**, not `i` itself.

    # ---
    # I get what you're saying! Let's **simplify** this and break it down step by step so it makes perfect sense.

    # ---

    # ### **💡 The Original Code**
    # ```python
    # for num, freq in count.items():
    #     bucket[freq].append(num)
    # ```
    # ---

    # ### **🔹 What Does This Do?**
    # - `count.items()` gives us **key-value pairs** from the dictionary `count`.
    #   - **Key (`num`)** = The actual number from `nums`
    #   - **Value (`freq`)** = How many times that number appears in `nums`
    # - We then **add (`append`) that number into `bucket[freq]`**, which groups numbers based on their frequency.

    # ---

    # ### **🔹 Example Breakdown**
    # #### **Input:**
    # ```python
    # nums = [1, 2, 2, 3, 3, 3]
    # ```
    # #### **Step 1: Frequency Count**
    # ```python
    # count = {1: 1, 2: 2, 3: 3}
    # ```

    # #### **Step 2: Using Our Code**
    # We loop over `count.items()`:
    # ```python
    # for num, freq in count.items():
    #     bucket[freq].append(num)
    # ```
    # 🔹 **Loop Execution:**
    # | `num`  | `freq` | `bucket[freq].append(num)` |
    # |--------|--------|---------------------------|
    # | `1`    | `1`    | `bucket[1] = [1]`         |
    # | `2`    | `2`    | `bucket[2] = [2]`         |
    # | `3`    | `3`    | `bucket[3] = [3]`         |

    # After this loop, the `bucket` list looks like:
    # ```python
    # bucket = [[], [1], [2], [3], [], [], []]
    # ```
    # ---

    # ### **🔹 Simplified Version**
    # ```python
    # for key in count:
    #     bucket[count[key]].append(key)
    # ```
    # ✅ **This does the same thing but looks cleaner!**
    # - `key` represents the number (same as `num`).
    # - `count[key]` gives its frequency.
    # - We put the number (`key`) inside `bucket[count[key]]`.

    # ---

    # ### **🔹 Final Thoughts**
    # - The original `for num, freq in count.items():` **just loops over dictionary key-value pairs**.
    # - The **simplified version** `for key in count:` does the same thing in a more direct way.
    # - **Why `num` and `freq`?** Just names! They **could be anything**, like:
    #   ```python
    #   for number, frequency in count.items():
    #       bucket[frequency].append(number)
    #   ```
    #   This makes it even clearer. 🚀