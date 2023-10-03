with open('textfile.txt') as text_file :
    content= text_file.read();

print(content);

with open('textfile.txt',mode='w') as text_file:
    text_file.writelines([content,"\nanother interesting line","\nit's becoming more interesting"])

with open('textfile.txt',mode='a') as text_file:
    text_file.write("This is awesome!")

with open('vahram_grigoryan.txt',mode='w') as cv:
    cv.writelines(["\tVahram Grigoryan CV",'\n\tPosition: Developer','\n\tCurrent Company: Bostongene']) 