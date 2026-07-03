# ⭐ LeetCode 678 — Valid Parenthesis String

<p align="center">

<img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white">

<img src="https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge">

<img src="https://img.shields.io/badge/Pattern-Greedy%20%7C%20String-success?style=for-the-badge">

<img src="https://img.shields.io/badge/Status-Solved-brightgreen?style=for-the-badge">

</p>

---

# 📖 Problem Statement

Given a string `s` containing:

* `'('`
* `')'`
* `'*'`

The character `'*'` can represent:

* `'('`
* `')'`
* An empty string `""`

Return **`True`** if the string can be interpreted as a valid parentheses string; otherwise, return **`False`**.

---

# 🧠 Pattern Used

* Greedy
* String

---

# 💡 Intuition

Trying every possible interpretation of `'*'` would require checking up to **3ⁿ** combinations, which is too slow.

Instead, maintain a **range** of possible unmatched opening parentheses:

* `leftMin` → Minimum possible unmatched `'('`
* `leftMax` → Maximum possible unmatched `'('`

This range changes as each character is processed.

---

# 🚀 Key Insight

Process each character as follows:

### `'('`

```text id="klmk4j"
leftMin += 1
leftMax += 1
```

---

### `')'`

```text id="u5mf8m"
leftMin -= 1
leftMax -= 1
```

---

### `'*'`

```text id="jlwm82"
leftMin -= 1
leftMax += 1
```

Treat `'*'` as:

* `')'` for the minimum possible unmatched `'('`
* `'('` for the maximum possible unmatched `'('`

---

### Additional Rules

If:

```text id="y1owwx"
leftMax < 0
```

Return **False** immediately.

After every character:

```text id="06krbf"
leftMin = max(leftMin, 0)
```

At the end:

```text id="wfeayg"
leftMin == 0
```

means at least one valid interpretation exists.

---

# 🏗️ Example

Input

```text id="1b5bql"
s = "(*))"
```

Traversal

| Character | leftMin | leftMax |
| --------- | ------: | ------: |
| `(`       |       1 |       1 |
| `*`       |       0 |       2 |
| `)`       |       0 |       1 |
| `)`       |       0 |       0 |

Output

```text id="0fd7me"
True
```

---

# ⚙️ Algorithm

```text id="um1oh9"
Initialize

leftMin = 0
leftMax = 0

Traverse every character

    Update leftMin and leftMax

    If leftMax < 0
        Return False

    leftMin = max(leftMin, 0)

Return leftMin == 0
```

---

# 💻 Python Solution

```python id="2zngf5"
class Solution(object):
    def checkValidString(self, s):

        leftMin = 0
        leftMax = 0

        for ch in s:

            if ch == "(":
                leftMin += 1
                leftMax += 1

            elif ch == ")":
                leftMin -= 1
                leftMax -= 1

            else:
                leftMin -= 1
                leftMax += 1

            if leftMax < 0:
                return False

            leftMin = max(leftMin, 0)

        return leftMin == 0
```

---

# 🔍 Dry Run

Input

```python id="jsn8z5"
s = "(*"
```

Processing

```text id="o2pjxa"
(

leftMin = 1
leftMax = 1

-----------------

*

leftMin = 0
leftMax = 2
```

Final Check

```text id="t7gqgc"
leftMin == 0
```

Output

```text id="zvvjlwm"
True
```

---

# 📊 Complexity Analysis

| Operation            | Complexity |
| -------------------- | ---------: |
| String Traversal     |       O(n) |
| **Time Complexity**  |   **O(n)** |
| **Space Complexity** |   **O(1)** |

---

# 🎯 Key Learning

* ✅ Learned the **Greedy Range** technique.
* ✅ Understood why brute force (`3ⁿ`) is impractical.
* ✅ Used `leftMin` and `leftMax` to represent all possible interpretations.
* ✅ Solved the problem in linear time with constant extra space.
* ✅ Strengthened Greedy reasoning for string problems.

---

# 🔗 Related Problems

* Valid Parentheses
* Generate Parentheses
* Minimum Remove to Make Valid Parentheses
* Longest Valid Parentheses
* Remove Invalid Parentheses

---

# ⭐ Conclusion

Valid Parenthesis String is one of the most elegant Greedy problems. Instead of exploring every possible interpretation of `'*'`, the algorithm maintains the minimum and maximum possible number of unmatched opening parentheses throughout the traversal. This clever range-based approach reduces an exponential search into an optimal **O(n)** solution with **O(1)** extra space.
