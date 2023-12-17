"""In a long career for Yorkshire, Geoffrey Boycott played 609 matches, batted 1014
times, was not out 162 times, and scored 48426 runs. Write a program to calculate
and display Boycott's batting average.
Note: A batting average is the number of runs scored divided by the number of
completed innings (i.e. the total times batted minus the times not out)."""
total_runs = 48426
total_balls_faced = 1014
total_matches = 609
total_not_outs = 162
innings = total_balls_faced - total_not_outs
avg = total_runs/innings
print("Boycott's Batting Average is", avg)