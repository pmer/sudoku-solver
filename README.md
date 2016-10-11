# Sudoku Solver

Solves sudoku puzzles by simple process of elimination on each square.
If the process of elimination is not sufficient to solve the puzzle,
as much as possible is completed before being printed.


## Usage

```
$ ./sudoku.py example-input.txt
```


## Example session

```
$ cat example-input.txt
 65 13 9 
 89   731
   7 8   
  1  7  5
  85241  
5  1  3  
   2 9   
197   68 
 2 86 95 
$ ./sudoku.py example-input.txt
765413298
489652731
213798564
641937825
938524176
572186349
856279413
197345682
324861957
```


## Bugs & issues

Please file a GitHub issue and I'll do my best to respond in a timely
manner.


## License

MIT
