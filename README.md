## Advent of Code 2023 Solutions (WIP)
This repository contains my solutions for the [Advent of Code 2023](https://adventofcode.com/2023) challenge, implemented in Python 3.11. The primary purpose of this project is to showcase my problem-solving approach and to practice writing clear and readable code.

### Directory Structure
- `day_xx_puzzle_name/`: Contains Python scripts for each day's challenge.
- `input/`: Directory where input files are expected to be placed in format: xx.txt. Input files are not included.

### Error Handling
Please note that the solutions may not handle unexpected input gracefully. The code assumes input files are formatted as specified in each day's puzzle description.

### [Day 1](https://adventofcode.com/2023/day/1)
Part 1 was a straightforward warm-up challenge to get started.

Part 2 provided an opportunity to refresh regular expressions.


### [Day 2](https://adventofcode.com/2023/day/2)
It involved more practice with regular expressions.

### [Day 3](https://adventofcode.com/2023/day/3)
This puzzle proved challenging for me. In Part 1, I employed a straightforward solution that involved looping over each character, examining neighbors, and required numerous if statements. I enhanced code readability with comments.

For Part 2, I returned to regular expressions, traversing the input file twice. The first pass involved locating all gears and storing them. During the second pass, I identified numbers and checked if their neighbors appeared among the stored gears.

### [Day 4](https://adventofcode.com/2023/day/4)
Part 1 provided an opportunity to utilize sets for an easy solution.

Part 2 additionally required storing the number of copies of each card as they were multiplying.

### [Day 5](https://adventofcode.com/2023/day/5)
Another opportunity to practice regex presented itself.

Part 1 was relatively easy and involved converting individual numbers multiple times according to maps.

In Part 2, a simple change in requirements made it very challenging. Now, you operate on ranges of numbers that need to be split when necessary. I enhanced code readability with comments.

### [Day 6](https://adventofcode.com/2023/day/6)
Some calculations were necessary to determine traveled distances.

In Part 2, there was an opportunity to apply the quadratic formula.

### [Day 7](https://adventofcode.com/2023/day/7)
The solution required:

- Processing the hand to standardize it.
- Calculating the value of the hand (chance to utilize a match-case statement).
- Comparing hands, necessary for proper sorting.

In Part 2, the introduction of jokers allowed me to explore a match-case statement more extensively, leading to an elegant solution when calculating the value of the hand.

### [Day 8](https://adventofcode.com/2023/day/8)
Regex was used to process the input.

I took the opportunity to create an infinite generator for traversing all nodes between the start and end node.

In Part 2, numerous starting nodes were introduced, necessitating simultaneous traversal and stopping only after reaching all end nodes concurrently. The magic of least common multiple came to the rescue.

### [Day 9](https://adventofcode.com/2023/day/9)
Part 1 was straightforward, as predicting the next value simply required summing up values.

In Part 2, predicting the previous value was not straightforward. It took time to realize that transforming the expression x = a - (b - (c - (d - (e - f)))) could be beneficial. I ended up with x = a + (-b) + c + (-d) + e + (-f), and this transformation allowed for a concise solution.

### [Day 10](https://adventofcode.com/2023/day/10)
Another challenging puzzle for me.

I began by constructing a neighbors map for each cell, then refactored it twice to improve readability. Next, I identified the proper neighbors of the starting cell, completing the neighbors map. With such a map, it became possible to determine how many cells are part of this pipe maze.

For Part 2, finding the solution required me to scour the Internet and discover that Pick's theorem could be employed. To apply Pick's theorem, I needed to use the Shoelace formula, and with that, the puzzle was solved.

### [Day 11](https://adventofcode.com/2023/day/11)
In Part 1, the expansion of the universe is represented by inserting additional rows and columns into a list of lists. Galaxies ('#') are then identified, and distances between them are calculated.

In Part 2, with the increased expansion rate, a new approach was required. We begin by finding all galaxies and then identify the rows and columns that will expand. During distance calculation, expansion is applied for each row and column that is expanding between two galaxies.

### [Day 12](https://adventofcode.com/2023/day/12)
This puzzle proved to be extremely challenging for me.
Once again, I utilized regex to process the input file.

In Part 1, I opted to generate every possible combination and check for validity, anticipating that Part 2 would necessitate a different approach to solving the problem.

Part 2 proved to be a formidable task, taking more than 10 hours to solve over 2 days. I experimented with various ideas to tackle the puzzle, encountering difficulties in devising a working solution. Eventually, my approach involved:

- Simplifying the input record, which, on its own, couldn't be enough. In the end, it only sped up the process by a few percent, but it was a result of staring at the input for an extended period.
- Building the recursion function, which proved to be challenging for me. I enhanced its readability with comments.
- Using the @cache decorator to expedite recursion since some records required a significant amount of time to be solved, ranging from a split second to ... it's been 2 hours and record number 31 out of 1000 is still not computed. I've decided to stop my attempt to determine the difference between not using and using the @cache decorator, as the difference is simply overwhelming.

### [Day 13](https://adventofcode.com/2023/day/13)
This was a straightforward puzzle.

In Part 1, a concise solution was found after some refactoring.

For Part 2, after experimenting with different approaches, I ultimately utilized 'chain' from itertools to convert my list of lists into a single list. This allowed me to maintain a concise solution.

### [Day 14](https://adventofcode.com/2023/day/14)
Another straightforward puzzle for me, even in Part 2.

Using 'zip' on a list of lists helps keep the code concise. Zip, now your columns are rows, do what you have to do and zip back.

Part 2 required more zipping and predicting an outcome after so many cycles that it wasn't feasible to go through the whole process. I ended up recording a platform layout, and after finding a repeated layout, I calculated the cycle length and offset to predict the final outcome.

### [Day 15](https://adventofcode.com/2023/day/15)
Part 1 was straightforward.

In Part 2, I had to do some tinkering to determine the proper way of storing data, enabling the removal of some data when requested, and modification when needed. Accessing a value based on a part of its value proved to be an unexpected challenge.

### [Day 16](https://adventofcode.com/2023/day/16)
### [Day 17](https://adventofcode.com/2023/day/17)
### [Day 18](https://adventofcode.com/2023/day/18)
### [Day 19](https://adventofcode.com/2023/day/19)
### [Day 20](https://adventofcode.com/2023/day/20)
### [Day 21](https://adventofcode.com/2023/day/21)
### [Day 22](https://adventofcode.com/2023/day/22)
### [Day 23](https://adventofcode.com/2023/day/23)
### [Day 24](https://adventofcode.com/2023/day/24)
### [Day 25](https://adventofcode.com/2023/day/25)



---

| Day | Challenge Info                                                         | Solution                                                                                                                                                                                   |
|:---:|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 01  | [Trebuchet?!](https://adventofcode.com/2023/day/1)                     | [Part 1](./day_01_trebuchet/01_trebuchet.py) / [Part 2](./day_01_trebuchet/01_trebuchet_part_2.py)                                                                                         |
| 02  | [Cube Conundrum](https://adventofcode.com/2023/day/2)                  | [Part 1](./day_02_cube_conundrum/02_cube_conundrum.py) / [Part 2](./day_02_cube_conundrum/02_cube_conundrum_part_2.py)                                                                     |
| 03  | [Gear Ratios](https://adventofcode.com/2023/day/3)                     | [Part 1](./day_03_gear_ratios/03_gear_ratios.py) / [Part 2](./day_03_gear_ratios/03_gear_ratios_part_2.py)                                                                                 |
| 04  | [Scratchcards](https://adventofcode.com/2023/day/4)                    | [Part 1](./day_04_scratchcards/04_scratchcards.py) / [Part 2](./day_04_scratchcards/04_scratchcards_part_2.py)                                                                             |
| 05  | [If You Give A Seed A Fertilizer](https://adventofcode.com/2023/day/5) | [Part 1](./day_05_if_you_give_a_seed_a_fertilizer/05_if_you_give_a_seed_a_fertilizer.py) / [Part 2](./day_05_if_you_give_a_seed_a_fertilizer/05_if_you_give_a_seed_a_fertilizer_part_2.py) |
| 06  | [Wait For It](https://adventofcode.com/2023/day/6)                     | [Part 1](./day_06_wait_for_it/06_wait_for_it.py) / [Part 2](./day_06_wait_for_it/06_wait_for_it_part_2.py)                                                                                 |
| 07  | [Camel Cards](https://adventofcode.com/2023/day/7)                     | [Part 1](./day_07_camel_cards/07_camel_cards.py) / [Part 2](./day_07_camel_cards/07_camel_cards_part_2.py)                                                                                 |
| 08  | [Haunted Wasteland](https://adventofcode.com/2023/day/8)               | [Part 1](./day_08_haunted_wasteland/08_haunted_wasteland.py) / [Part 2](./day_08_haunted_wasteland/08_haunted_wasteland_part_2.py)                                                         |
| 09  | [Mirage Maintenance](https://adventofcode.com/2023/day/9)              | [Part 1](./day_09_mirage_maintenance/09_mirage_maintenance.py) / [Part 2](./day_09_mirage_maintenance/09_mirage_maintenance_part_2.py)                                                     |
| 10  | [Pipe Maze](https://adventofcode.com/2023/day/10)                      | [Part 1](./day_10_pipe_maze/10_pipe_maze.py) / [Part 2](./day_10_pipe_maze/10_pipe_maze_part_2.py)                                                                                         |
| 11  | [Cosmic Expansion](https://adventofcode.com/2023/day/11)               | [Part 1](./day_11_cosmic_expansion/11_cosmic_expansion.py) / [Part 2](./day_11_cosmic_expansion/11_cosmic_expansion_part_2.py)                                                             |
| 12  | [Hot Springs](https://adventofcode.com/2023/day/12)                    | [Part 1](./day_12_hot_springs/12_hot_springs.py) / [Part 2](./day_12_hot_springs/12_hot_springs_part_2.py)                                                                                 |
| 13  | [Point of Incidence](https://adventofcode.com/2023/day/13)             | [Part 1](./day_13_point_of_incidence/13_point_of_incidence.py) / [Part 2](./day_13_point_of_incidence/13_point_of_incidence_part_2.py)                                                     |
| 14  | [Parabolic Reflector Dish](https://adventofcode.com/2023/day/14)       | [Part 1](./day_14_parabolic_reflector_dish/14_parabolic_reflector_dish.py) / [Part 2](./day_14_parabolic_reflector_dish/14_parabolic_reflector_dish_part_2.py)                             |
| 15  | [Lens Library](https://adventofcode.com/2023/day/15)                   | [Part 1](./day_15_lens_library/15_lens_library.py) / [Part 2](./day_15_lens_library/15_lens_library_part_2.py)                                                                             |
| 16  | [The Floor Will Be Lava](https://adventofcode.com/2023/day/16)         |                                                                                                                                                                                            |
| 17  | [Clumsy Crucible](https://adventofcode.com/2023/day/17)                |                                                                                                                                                                                            |
| 18  | [Lavaduct Lagoon](https://adventofcode.com/2023/day/18)                |                                                                                                                                                                                            |
| 19  | [Aplenty](https://adventofcode.com/2023/day/19)                        |                                                                                                                                                                                            |
| 20  | [Pulse Propagation](https://adventofcode.com/2023/day/20)              |                                                                                                                                                                                            |
| 21  | [Step Counter](https://adventofcode.com/2023/day/21)                   |                                                                                                                                                                                            |
| 22  | [Sand Slabs](https://adventofcode.com/2023/day/22)                     |                                                                                                                                                                                            |
| 23  | [A Long Walk](https://adventofcode.com/2023/day/23)                    |                                                                                                                                                                                            |
| 24  | [Never Tell Me The Odds](https://adventofcode.com/2023/day/24)         |                                                                                                                                                                                            |
| 25  | [Snowverload](https://adventofcode.com/2023/day/25)                    |                                                                                                                                                                                            |
