from random import randint

input_data = open("C:\\Projects\\Tasks\\MinTriangleTask\\input.txt", "w")

for s in [str(randint(1, 30000)) for _ in range(30)]:
    input_data.write(s + '\n')

input_data.close()
print('Done')