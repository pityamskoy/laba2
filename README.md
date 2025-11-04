<h1>Laba 2</h1>
<p>The second laboratiry work was done by Кекишев Андрей Сергеевич М80-106БВ-25</p>

<h3>Description</h3>
<p>
It is a terminal based program, which simulates run of some Bash commands, namely:
cd, ls, cat, cp, mv, rm, zip, tar, unzip, untar.
It also supports 'quit' command to stop executing of the program

These commands are made corresponding to the following assumption.
</p>
<h3>Assumption</h3>
<p>
1. All of the commands cannot be called more with more than 2 arguments.
2. All of the commands don't support flags, except -l for ls and -r for remove. It is important to notice that cp -r is implemented but for simplyfing string parser you shouldn't write it. It just copy recursively in the case if a directory was provided as a source, or copy natively in the case of a file.
3. Each command has their own specific syntax, which we provide next.
</p>

<h5>cd<h5>
<p>cd 'folder'. It doesn't support files for changing directory</p>
<h5>ls<h5>
<p>ls 'folder'. Folder is optional in this case. 'ls' will give you information about all files in the current dir. Supported flags: -l</p>
<h5>cat<h5>
<p>cat 'file'. It doesn't support folders</p>
<h5>cp<h5>
<p>cd 'file_or_folder' 'folder_to_copy'. It is implemented -r if a folder for copying was provided</p>
<h5>mv<h5>
<p>mv 'file_or_folder' 'folder_to_move'. 'folder_to_move' is optional. If you dont provide 'folder_to_move' it will move folder to the current directory</p>
<h5>rm<h5>
<p>rm 'file_or_folder'. Supported flags: -l. It will not delete folder to which it doesn't have access to. Restrictions: it won't delete parent folder '..' or root</p>
<h5>zip/tar<h5>
<p>zip/tar 'folder' 'archieve.zip'. First argument is the folder for archiving, second - folder to place the archive</p>
<h5>unzip/untar<h5>
<p>unzip/untar 'archieve.zip'. It extracts all files from an archive to the current folder</p>