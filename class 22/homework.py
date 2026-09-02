snack_box1 = {"chips", "juice", "cookies", "chips", "apple"}
snack_box2 = {"cookies", "sandwich", "juice", "sandwich"}
print("Snack Box 1:", snack_box1)
print("Snack Box 2:", snack_box2)
snack_box1.add("banana")
print(snack_box1)
common_snacks = snack_box1.intersection(snack_box2)
print(common_snacks)
import array as arr
snack_counts = arr.array('i', [4,6,3,5])
print(snack_counts)
snack_counts.insert(0, 2)
snack_counts.append(7)
print(snack_counts)
ghghgh = snack_counts.count(5)
print(ghghgh)
snack_counts.reverse()
print(snack_counts)
