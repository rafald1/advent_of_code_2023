## Advent of Code 2023 Solutions
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
This puzzle turned out to be harder than anticipated.

In Part 1, it took a significant amount of time to get it right due to numerous if statements addressing the proper direction change of beams. The code was challenging to read through, and refactoring proved time-consuming, with most changes not significantly improving readability. Eventually, a satisfactory version emerged.

For Part 2, adapting the code from Part 1 was relatively easy, but unfortunately, it was very slow, taking 3 minutes. Identifying the issue proved challenging, and it was a time-consuming lesson to discover that checking if an element is present in a list is costly when the list has a few thousand elements. Replacing the list with a set reduced the time to around 1 second. While it might still be slow for some, it felt like a significant improvement.

The 8 hours passed by like minutes.

### [Day 17](https://adventofcode.com/2023/day/17)
The previous day's experience made this puzzle easier to solve. I took the opportunity to refresh my knowledge of Dijkstra and the Uniform-Cost Search algorithms. An additional condition added complexity to the task, making it challenging.

The changes to conditions in Part 2 made modifying the code from Part 1 straightforward.

### [Day 18](https://adventofcode.com/2023/day/18)
At first, this seemed a little bit daunting because my initial thought was that I would have to build and expand a 2D array with every step. Fortunately, having been exposed to Pick’s theorem and the shoelace formula on Day 10 Part 2 steered me in the direction of creating a list of all points that are part of just a border. With this approach, the solution became straightforward to implement.

Part 2 revealed that my implementation was slow and needed refinement. Realizing that I didn't have to store all the points, but only the starting and ending points with every direction change, and finding a different way to calculate the border length, led to a new implementation that was super fast.

### [Day 19](https://adventofcode.com/2023/day/19)
Processing the input was a little bit tricky and required some thought. Part 1 involved sorting according to a set of rules and was straightforward.

In Part 2, a lot of thinking and drawing were involved because each part had four categories, each ranging from 1 to 4000. The process of sorting part ranges was similar to that in Day 5 Part 2. However, this time, I did a much better job refactoring and simplifying it.

### [Day 20](https://adventofcode.com/2023/day/20)
This puzzle wasn't straightforward at all. It started with processing the input and setting the states of every module. Properly reflecting the behavior of modules took time, and it was easy to make a mistake, making it challenging to pinpoint the issue.

Part 2 seemed easy at first. You were supposed to stop the process when a certain condition occurred. Unfortunately, it wasn't happening anytime soon. The solution required taking a closer look at the input and analyzing it. The required condition would only occur when a certain condition happened for all four different modules simultaneously. Using the least common multiple made finding the solution possible in a short time.

### [Day 21](https://adventofcode.com/2023/day/21)
Part 1 was straightforward. I quickly noticed that certain plots could only be reached on odd step numbers, while others could only be reached on even step numbers. I swiftly devised a concise solution that was satisfying.

Part 2 took me 20 hours, but I am content with the final result. I experimented with different approaches, some of which failed or became too messy to pursue. After taking a break and solving other puzzles, I returned to tackle this one.

To gain a better understanding of the problem, I created visual aids. The major challenge was the dissimilarity in structure between the test input and the puzzle input. The test input was solved using standard means of traversing gardens and counting plots, which for 5000 steps became time-consuming, taking 18 minutes to count plots.

The puzzle input was constructed in a way that the expansion of gardens was symmetrical in all directions, offering the opportunity for a different solution approach. I opted for a quadratic function, which seemed the most straightforward for me.
### [Day 22](https://adventofcode.com/2023/day/22)
It seemed simple, but I struggled. Firstly, with visualizing these 3D bricks falling down inside the 10 x 10 grid. Then, with choosing the way of checking where they would end up. I pondered whether to store them in a 3D array or if it was unnecessary. I ended up with a dictionary using grid indices as keys and the current z level as values. For every falling brick, I checked the highest z level for the correct x, y values, changed the z value of the brick, and updated my z levels dictionary. Disintegrating bricks wasn't any easier. I chose to remove every brick to check if the rest would start falling down or stay in place.

Part 2 required getting a count of falling bricks after removing each of the bricks one at a time. With some small changes, the solution was reached. In the end, I feel like I may have chosen wrong approach, and other solutions would be faster.

### [Day 23](https://adventofcode.com/2023/day/23)
It was another maze, and this time, finding the longest path was the challenge. I delved into different approaches for discovering the longest path. Initially, I attempted recursion, which worked well on test data but didn't complete on my puzzle input due to a RecursionError. Rather than changing the default limit, I opted to use a queue and try again. I invested time in transforming the input into a dictionary with cell indices as keys and valid neighbors as values. The algorithm for finding the longest path ended up being concise and easy to understand.

With the changes introduced in Part 2, my solution seemed to work on test data, but it either looped indefinitely on the full input puzzle or I didn't wait long enough to confirm if it actually solved it. I took the opportunity to further transform my data. First, I identified the vertices of this graph, along with the starting and ending nodes. Then, I calculated edge weights between all vertices. Finally, I began searching for all possible paths to find the longest one.

### [Day 24](https://adventofcode.com/2023/day/24)
This puzzle brought a welcomed change. To solve Part 1, some math came into play. Based on the starting point and velocity, the slope and intercept had to be found. Then, for every possible combination of two hailstones, the collision point (intersection of two lines) was determined, if any. Finally, a check was added to ensure that this intersection occurred in the future and not in the past.

Part 2 demanded a substantial amount of math. The goal was to find the starting point (px, py, pz) and velocity (vx, vy, vz) of a thrown rock that would collide with all hailstones. Six unknowns meant six equations were needed to find the solution. Forming these six equations required examining collisions of our rock with three different hailstones. Starting with nine equations and introducing three more unknowns representing the time when the collision occurred for each hailstone. Transforming this set of nine equations into a set of six equations involved eliminating the time of the collision. The choice of three hailstones became crucial, as they needed to have linearly independent velocity vectors. To assess that, I used Gaussian elimination. However, the issue with choosing Gaussian elimination was that the matrix created from velocity vectors sometimes couldn't be solved due to division by zero. First, attempting to re-sequence this matrix, and if unsuccessful, it meant the matrix was singular, and a different set of three hailstones had to be chosen, repeating the process.

To solve the equations, I utilized SymPy, as attempting to solve them by hand proved to be impractical. Although I tried to brush off the dust from my math skills, progress was limited even after a couple of hours. My approach of choosing three random hailstones revealed that checking if their velocity vectors are linearly independent isn't sufficient, as SymPy sometimes didn't produce a solution, especially on test data. In such cases, I repeat the process of choosing three hailstones again.

### [Day 25](https://adventofcode.com/2023/day/25)
This puzzle took me more time than expected, as I delved into studying minimum cuts in graphs. I ultimately implemented Karger's algorithm. However, I initially used sets to store neighbors, as I didn't fully grasp the algorithm's concept. I employed a variable to indicate how many nodes were "inside" each node after each edge contraction. It took time to realize that this algorithm should provide the probable minimum cut based on the number of neighbors left in the two final nodes, rather than the outcome of the minimum cut.

Changing the way I stored neighbors from a set to a list allowed me to end up with two nodes containing a list of repeated neighbors, and the count of these neighbors indicated the minimum cut. The final step involved running this algorithm until it produced the number 3 and then checking how many nodes each of the final two nodes was composed of. It was a solid lesson.

---

| Day | Challenge Info                                                                   | Solution                                                                                                                                                                                   |
|:---:|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 01  | [Trebuchet?!](https://adventofcode.com/2023/day/1)                               | [Part 1](./day_01_trebuchet/01_trebuchet.py) / [Part 2](./day_01_trebuchet/01_trebuchet_part_2.py)                                                                                         |
| 02  | [Cube Conundrum](https://adventofcode.com/2023/day/2)                            | [Part 1](./day_02_cube_conundrum/02_cube_conundrum.py) / [Part 2](./day_02_cube_conundrum/02_cube_conundrum_part_2.py)                                                                     |
| 03  | [Gear Ratios](https://adventofcode.com/2023/day/3)                               | [Part 1](./day_03_gear_ratios/03_gear_ratios.py) / [Part 2](./day_03_gear_ratios/03_gear_ratios_part_2.py)                                                                                 |
| 04  | [Scratchcards](https://adventofcode.com/2023/day/4)                              | [Part 1](./day_04_scratchcards/04_scratchcards.py) / [Part 2](./day_04_scratchcards/04_scratchcards_part_2.py)                                                                             |
| 05  | [If You Give A Seed A Fertilizer](https://adventofcode.com/2023/day/5)           | [Part 1](./day_05_if_you_give_a_seed_a_fertilizer/05_if_you_give_a_seed_a_fertilizer.py) / [Part 2](./day_05_if_you_give_a_seed_a_fertilizer/05_if_you_give_a_seed_a_fertilizer_part_2.py) |
| 06  | [Wait For It](https://adventofcode.com/2023/day/6)                               | [Part 1](./day_06_wait_for_it/06_wait_for_it.py) / [Part 2](./day_06_wait_for_it/06_wait_for_it_part_2.py)                                                                                 |
| 07  | [Camel Cards](https://adventofcode.com/2023/day/7)                               | [Part 1](./day_07_camel_cards/07_camel_cards.py) / [Part 2](./day_07_camel_cards/07_camel_cards_part_2.py)                                                                                 |
| 08  | [Haunted Wasteland](https://adventofcode.com/2023/day/8)                         | [Part 1](./day_08_haunted_wasteland/08_haunted_wasteland.py) / [Part 2](./day_08_haunted_wasteland/08_haunted_wasteland_part_2.py)                                                         |
| 09  | [Mirage Maintenance](https://adventofcode.com/2023/day/9)                        | [Part 1](./day_09_mirage_maintenance/09_mirage_maintenance.py) / [Part 2](./day_09_mirage_maintenance/09_mirage_maintenance_part_2.py)                                                     |
| 10  | [Pipe Maze](https://adventofcode.com/2023/day/10)                                | [Part 1](./day_10_pipe_maze/10_pipe_maze.py) / [Part 2](./day_10_pipe_maze/10_pipe_maze_part_2.py)                                                                                         |
| 11  | [Cosmic Expansion](https://adventofcode.com/2023/day/11)                         | [Part 1](./day_11_cosmic_expansion/11_cosmic_expansion.py) / [Part 2](./day_11_cosmic_expansion/11_cosmic_expansion_part_2.py)                                                             |
| 12  | [Hot Springs](https://adventofcode.com/2023/day/12)                              | [Part 1](./day_12_hot_springs/12_hot_springs.py) / [Part 2](./day_12_hot_springs/12_hot_springs_part_2.py)                                                                                 |
| 13  | [Point of Incidence](https://adventofcode.com/2023/day/13)                       | [Part 1](./day_13_point_of_incidence/13_point_of_incidence.py) / [Part 2](./day_13_point_of_incidence/13_point_of_incidence_part_2.py)                                                     |
| 14  | [Parabolic Reflector Dish](https://adventofcode.com/2023/day/14)                 | [Part 1](./day_14_parabolic_reflector_dish/14_parabolic_reflector_dish.py) / [Part 2](./day_14_parabolic_reflector_dish/14_parabolic_reflector_dish_part_2.py)                             |
| 15  | [Lens Library](https://adventofcode.com/2023/day/15)                             | [Part 1](./day_15_lens_library/15_lens_library.py) / [Part 2](./day_15_lens_library/15_lens_library_part_2.py)                                                                             |
| 16  | [The Floor Will Be Lava](https://adventofcode.com/2023/day/16)                   | [Part 1](./day_16_the_floor_will_be_lava/16_the_floor_will_be_lava.py) / [Part 2](./day_16_the_floor_will_be_lava/16_the_floor_will_be_lava_part_2.py)                                     |
| 17  | [Clumsy Crucible](https://adventofcode.com/2023/day/17)                          | [Part 1](./day_17_clumsy_crucible/17_clumsy_crucible.py) / [Part 2](./day_17_clumsy_crucible/17_clumsy_crucible_part_2.py)                                                                 |
| 18  | [Lavaduct Lagoon](https://adventofcode.com/2023/day/18)                          | [Part 1](./day_18_lavaduct_lagoon/18_lavaduct_lagoon.py) / [Part 2](./day_18_lavaduct_lagoon/18_lavaduct_lagoon_part_2.py)                                                                 |
| 19  | [Aplenty](https://adventofcode.com/2023/day/19)                                  | [Part 1](./day_19_aplenty/19_aplenty.py) / [Part 2](./day_19_aplenty/19_aplenty_part_2.py)                                                                                                 |
| 20  | [Pulse Propagation](https://adventofcode.com/2023/day/20)                        | [Part 1](./day_20_pulse_propagation/20_pulse_propagation.py) / [Part 2](./day_20_pulse_propagation/20_pulse_propagation_part_2.py)                                                         |
| 21  | [Step Counter](https://adventofcode.com/2023/day/21)                             | [Part 1](./day_21_step_counter/21_step_counter.py) / [Part 2](./day_21_step_counter/21_step_counter_part_2.py)                                                                             |
| 22  | [Sand Slabs](https://adventofcode.com/2023/day/22)                               | [Part 1](./day_22_sand_slabs/22_sand_slabs.py) / [Part 2](./day_22_sand_slabs/22_sand_slabs_part_2.py)                                                                                     |
| 23  | [A Long Walk](https://adventofcode.com/2023/day/23)                              | [Part 1](./day_23_a_long_walk/23_a_long_walk.py) / [Part 2](./day_23_a_long_walk/23_a_long_walk_part_2.py)                                                                                 |
| 24  | [Never Tell Me The Odds](https://adventofcode.com/2023/day/24)                   | [Part 1](./day_24_never_tell_me_the_odds/24_never_tell_me_the_odds.py) / [Part 2](./day_24_never_tell_me_the_odds/24_never_tell_me_the_odds_part_2.py)                                     |
| 25  | [Snowverload](https://adventofcode.com/2023/day/25)                              | [Part 1](./day_25_snowverload/25_snowverload.py)                                                                                                                                           |
