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
<ol>
<li>
1. All the commands cannot be called more with more than 2 arguments.
</li>
<li>
2. All the commands don't support flags, except -l for ls and -r for remove. It is important to notice that cp -r is implemented but for simplyfing string parser you shouldn't write it. It just copy recursively in the case if a directory was provided as a source, or copy natively in the case of a file.
</li>
<li>
3. Each command has their own specific syntax, which we provide next.
</li>
</ol>
<h4>cd</h4>
<p>cd 'folder'. It doesn't support files for changing directory</p>
<h4>ls</h4>
<p>ls 'folder'. Folder is optional in this case. 'ls' will give you information about all files in the current dir. Supported flags: -l</p>
<h4>cat</h4>
<p>cat 'file'. It doesn't support folders</p>
<h4>cp</h4>
<p>cd 'file_or_folder' 'folder_to_copy'. It is implemented -r if a folder for copying was provided</p>
<h4>mv</h4>
<p>mv 'file_or_folder' 'folder_to_move'. 'folder_to_move' is optional. If you dont provide 'folder_to_move' it will move folder to the current directory</p>
<h4>rm</h4>
<p>rm 'file_or_folder'. Supported flags: -l. It will not delete folder to which it doesn't have access to. Restrictions: it won't delete parent folder '..' or root</p>
<h4>zip/tar</h4>
<p>zip/tar 'folder' 'archieve.zip'. First argument is the folder for archiving, second - folder to place the archive</p>
<h4>unzip/untar</h4>
<p>unzip/untar 'archieve.zip'. It extracts all files from an archive to the current folder</p>