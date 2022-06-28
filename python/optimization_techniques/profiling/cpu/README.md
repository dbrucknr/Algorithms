To see profile output type: `python -m cProfile prof.py` when line 28 = 1 instead of 0. Profiles entire file.

Otherwise just run `python prof.py` switch line 31 or 35 to 1, make the other 0.

if you have a `prof.out` file type: `python -m pstats prof.out`

- stats 10
- sort cumtime
- stats 10

pip install snakeviz or conda install

- then to see visualizations of performance type: `snakeviz prof.out`
