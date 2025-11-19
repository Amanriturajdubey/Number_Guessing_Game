import time
import random
sentance = ['Aman Rituraj Dubey Vimal Tormal Poddar College Gujrat Surat','Manju Rituraj Dubey Surat Gujrat']
test_sentance = random.choice(sentance)
print("Type the following sentence as fast as you can:\n")
print(f"\033[94m{test_sentance}\033[0m\n")

start_time = time.time()
type_sentance = input("Start typing Here\n")
end_time = time.time()


time_taken = end_time - start_time
time_taken_minute = time_taken / 60


num_char = len(type_sentance)
wpm = (num_char / 5) / time_taken


original_word = test_sentance.split()
type_word = type_sentance.split()

coreect_word = 0
for orig, typed in zip(original_word,type_word):
    if orig == typed:
        coreect_word += 1

accuracy = (coreect_word / len(original_word))*100


print("\n--Result--")
print(f"Time Taken : {round(time_taken,2)} Seconds")
print(f"Word per Minute (wpm) : {int(wpm)}")
print(f"Acuuracy : {round(accuracy,2)}%")


