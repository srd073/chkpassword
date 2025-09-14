Last login: Sun Sep 14 11:49:58 on console
cde
The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
(base) Max-MacBook-Pro:~ max$ cd desktop
(base) Max-MacBook-Pro:desktop max$ cd chkpassword
(base) Max-MacBook-Pro:chkpassword max$ python chk.py
  File "/Users/max/Desktop/chkpassword/chk.py", line 8
    else:
         ^
IndentationError: unindent does not match any outer indentation level
(base) Max-MacBook-Pro:chkpassword max$ python chk.py
  File "/Users/max/Desktop/chkpassword/chk.py", line 8
    else:
         ^
IndentationError: unindent does not match any outer indentation level
(base) Max-MacBook-Pro:chkpassword max$ python chk.py
  File "/Users/max/Desktop/chkpassword/chk.py", line 8
    else:
         ^
IndentationError: unindent does not match any outer indentation level
(base) Max-MacBook-Pro:chkpassword max$ python chk.py
  File "/Users/max/Desktop/chkpassword/chk.py", line 8
    else:
         ^
IndentationError: unindent does not match any outer indentation level
(base) Max-MacBook-Pro:chkpassword max$ echo "# chkpassword" >> README.md
(base) Max-MacBook-Pro:chkpassword max$ git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint: 
hint: 	git config --global init.defaultBranch <name>
hint: 
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint: 
hint: 	git branch -m <name>
Initialized empty Git repository in /Users/max/Desktop/chkpassword/.git/
(base) Max-MacBook-Pro:chkpassword max$ git add README.md
(base) Max-MacBook-Pro:chkpassword max$ git commit -m "first commit"
[master (root-commit) baedb55] first commit
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
(base) Max-MacBook-Pro:chkpassword max$ git branch -M main
(base) Max-MacBook-Pro:chkpassword max$ git remote add origin https://github.com/srd073/chkpassword.git
(base) Max-MacBook-Pro:chkpassword max$ git push -u origin main
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 223 bytes | 223.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/srd073/chkpassword.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
(base) Max-MacBook-Pro:chkpassword max$ git add chk.py
(base) Max-MacBook-Pro:chkpassword max$ git commit -m "chkpassword"
[main 04115e9] chkpassword
 1 file changed, 10 insertions(+)
 create mode 100644 chk.py
(base) Max-MacBook-Pro:chkpassword max$ git push origin main
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 448 bytes | 448.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/srd073/chkpassword.git
   baedb55..04115e9  main -> main
(base) Max-MacBook-Pro:chkpassword max$ python chk.py
  File "/Users/max/Desktop/chkpassword/chk.py", line 8
    else:
         ^
IndentationError: unindent does not match any outer indentation level
(base) Max-MacBook-Pro:chkpassword max$ python chk.py
  File "/Users/max/Desktop/chkpassword/chk.py", line 8
    else:
         ^
IndentationError: unindent does not match any outer indentation level
(base) Max-MacBook-Pro:chkpassword max$ python chk.py
  File "/Users/max/Desktop/chkpassword/chk.py", line 8
    else:
         ^
IndentationError: unindent does not match any outer indentation level
(base) Max-MacBook-Pro:chkpassword max$ python chk.py
  File "/Users/max/Desktop/chkpassword/chk.py", line 8
    else:
         ^
IndentationError: unindent does not match any outer indentation level
(base) Max-MacBook-Pro:chkpassword max$ python chk.py
  File "/Users/max/Desktop/chkpassword/chk.py", line 8
    else:
         ^
IndentationError: unindent does not match any outer indentation level
(base) Max-MacBook-Pro:chkpassword max$ python chk.py
  File "/Users/max/Desktop/chkpassword/chk.py", line 8
    else:
         ^
IndentationError: unindent does not match any outer indentation level
(base) Max-MacBook-Pro:chkpassword max$ python chk.py
  File "/Users/max/Desktop/chkpassword/chk.py", line 9
    t = t-1
TabError: inconsistent use of tabs and spaces in indentation
(base) Max-MacBook-Pro:chkpassword max$ python chk.py
請輸入密碼：123456
登入成功！
(base) Max-MacBook-Pro:chkpassword max$ python chk.py
請輸入密碼：3
密碼錯誤, 還有 2 次機會
請輸入密碼：3
密碼錯誤, 還有 1 次機會
請輸入密碼：3
密碼錯誤, 還有 0 次機會
(base) Max-MacBook-Pro:chkpassword max$ git push origin main
Everything up-to-date
(base) Max-MacBook-Pro:chkpassword max$ git commit -m "second commit"
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   chk.py

no changes added to commit (use "git add" and/or "git commit -a")
(base) Max-MacBook-Pro:chkpassword max$ git push origin main
Everything up-to-date
(base) Max-MacBook-Pro:chkpassword max$ 
