# Music Note Practice

This Python program is designed to help users practice their music note recognition skills. It generates a group of random notes and asks the user to identify them. The user can specify the number of practice runs, the size of the note group, and the type of note names to use.

考虑到很多朋友没有开发基础，这里说一下详细的步骤。

Windows：

1. 首先你要安装python，用windows的朋友可以直接去商店里面搜python，下载安装最新版本就好。
2. 然后下载这个包，解压后，在有`music_note_practice.py`这个文件的文件夹里，右键点击空白处，选择`open in terminal`
3. 然后在命令行里输入
```
python music_note_practice.py
```
然后跟着屏幕上的提示输入对应信息就好了。需要你有一点英文基础。

Note: `type of node name` 输入`name`对应唱名，输入`CDE`对应级数。

Mac & Linux：

相信用mac或者linux都有一定的开发基础，具体步骤根上面类似，需要先安装python，然后在terminal里运行命令，注意文件路径。

## Features

- Generates a group of random notes without duplicates
- Checks the user's answers and provides feedback
- Calculates and displays the percentage of correct answers at the end of all runs
- Measure time spent for each run, and dispay average at the end of all runs

## Usage

1. Run the program. Example: 
```
python music_note_practice.py
```
2. Enter the number of practice runs.
3. Enter the size of the note group (between 1 and 7).
4. Enter the type of note names to use ('name' for 'do', 're', 'mi', etc., or 'CDE' for 'C', 'D', 'E', etc.).
5. For each run, the program will display a group of random notes. Enter your answers in one line, separated by spaces or commas.
6. The program will check your answers and provide feedback. If all answers are correct, it will print a message saying so. If any answer is incorrect, it will print the incorrect ones and the correct answers.
7. At the end of all runs, the program will calculate and print the percentage of correct answers.

## Note Mapping

The program uses the following mapping between numbers and note names:

1: ['do', 'C']
2: ['re', 'D']
3: ['mi', 'E']
4: ['fa', 'F']
5: ['sol', 'so', 'G']
6: ['la', 'A']
7: ['si', 'ti', 'B']
