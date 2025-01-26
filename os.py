
import os
print(dir(os))

print(os.getcwd())

os.chdir('/Users/george/desktop/Python OOP')
print(os.getcwd())

#os.mkdir('OS-Demo-2/Sub-Dir-1') #will not create the middle sub levels
os.makedirs('OS-Demo-2/Sub-Dir-1') #Usually, because it can create multiple

print(os.listdir())

for dirpath,dirnames,filenames in os.walk('/Users/george/desktop/Python OOP'):
    print('Current Path:',dirpath)
    print('Directories:',dirnames)

print(os.environ.get('HOME'))# Get environment variables

#file_path = os.environ.get('Home') + 'text.txt' ez to forget

file_path = os.path.join(os.environ.get('HOME'),'test.txt')
print(file_path)


