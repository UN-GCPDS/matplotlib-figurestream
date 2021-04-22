rm requirements.txt
pipreqs --savepath requirements.txt --force figurestream
sed -i 's/==.*//' requirements.txt
python -c "[print(f'\'{line[:-1]}\',') for line in open('requirements.txt').readlines()]"
